# flask
# pymysql
# flask_jwt_extended

from flask import Flask, request, render_template, send_from_directory, jsonify
from database import database_manager
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
import datetime
import hashlib
import random
import string
import base64
import datetime
import urllib.parse

app = Flask(__name__)

md5 = hashlib.md5()
md5.update("sample".encode())
app.config["JWT_SECRET_KEY"] = md5.hexdigest()
jwt = JWTManager(app)

db = None


# 토큰 검증
def accessCheck(sid, token):
    try:
        result = db.execute("""
        SELECT UserIDSeq 
        FROM UserLogin 
        WHERE UserIDSeq = %s 
              AND Token = %s
        """, (sid, token))
        if result:
            return True
        else:
            return False
    except:
        return False

# length 길이의 임의의 랜덤문자 생성
def randString(length):
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase +\
    string.ascii_lowercase +\
    string.digits) for _ in range(length))


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


"""
응답코드
0: 성공
2: 인증 실패
3: 해당 투표 없음
4: 투표 참여 가능 인원 초과
5: 참여자 명단에 없음
40: 투표 해시 불일치
50: 이미 참여한 유저
60: 투표 참여 기간 종료
97: 투표 데이터 추가 실패
98: 투표 항목 없음
99: 알 수 없는 오류
"""
# 투표 제출
@app.route("/info/send/vote", methods=["POST"])
@jwt_required
def vote():
    try:
        req = request.get_json()
        sid = get_jwt_identity()

        if not accessCheck(sid, request.headers["Authorization"].split()[1]):
            return jsonify({"success": False, "code": 2}), 401

        vote_undecode = req["vote"]
        vote = urllib.parse.unquote(base64.b64decode(req["vote"]).decode())
        currentTime = req["currentTime"]
        voteCode = req["voteCode"]
        nonce = req["nonce"]

        vote_info = db.execute("""
        SELECT VotePermission, 
               VoteLimit, 
               VoteStart, 
               VoteEnd 
        FROM Vote_Information 
        WHERE UniqueNumberSeq = %s
        """, (voteCode))

        if (datetime.datetime.now() >= vote_info[0]["VoteEnd"]):
            print("해당 투표 참여 기간이 끝났습니다")
            return jsonify({"success": False, "code": 60}), 401

        # 투표가 없는 경우
        if len(vote_info) == 0:
            print("투표를 찾을 수 없습니다")
            return jsonify({"success": False, "code": 3}), 404

        vote_limit = db.execute("""
        SELECT COUNT(*) AS COUNT 
        FROM Vote_User 
        WHERE JoinAlready = 1 
              AND UniqueNumberSeq = %s
        """, (voteCode))

        # 참여 가능 인원이 초과된 경우
        if vote_info[0]["VoteLimit"] <= vote_limit[0]["COUNT"]:
            print("해당 투표는 참여가능 인원이 가득 찼습니다")
            return jsonify({"success": False, "code": 4}), 401

        alreadyCheck = db.execute("""
        SELECT UserIDSeq 
        FROM Vote_User 
        WHERE UserIDSeq = %s 
              AND UniqueNumberSeq = %s 
              AND JoinAlready = 1
        """, (sid, voteCode))

        # 투표 참여했는지 확인
        if len(alreadyCheck) != 0:
            print("User: {} 이미 참여한 유저입니다".format(sid))
            return jsonify({"success": False, "code": 50}), 403

        # 해당 유저가 투표에 참여했는지 확인/참여자 명단에 있는지 확인
        if vote_info[0]["VotePermission"] == 1:
            user_list = db.execute("""
            SELECT UserIDSeq 
            FROM Vote_User 
            WHERE UserIDSeq = %s 
                  AND UniqueNumberSeq = %s 
                  AND JoinAlready = 0
            """, (sid, voteCode))

            if len(user_list) == 0:
                print("User: {} 투표 참여자 명단에 존재하지 않습니다".format(sid))
                return jsonify({"success": False, "code": 5}), 401
        else:
            db.update("""
            INSERT INTO Vote_User 
            VALUES (%s, %s, 0)
            """, (sid, voteCode))
            print("User: {} 투표 참여자로 기록 됨".format(sid))

        hashingData = (str(vote_undecode) + str(currentTime) + str(voteCode) + str(nonce)).encode("utf-8")
        checkHash = hashlib.sha256(hashingData).hexdigest()

        if checkHash != req["hash"]:
            print("투표 데이터 해시가 일치하지 않습니다")
            return jsonify({"success": False, "code": 40}), 403

        vote_item = db.execute("""
        SELECT Vote_Item 
        FROM Vote_Item 
        WHERE UniqueNumberSeq = %s
        """, (voteCode))[0]["Vote_Item"]

        # 투표한 항목이 투표에 존재하는지 확인
        if vote in vote_item.split(","):
            inserted = db.update("""
            INSERT INTO Vote_Data 
            (UniqueNumberSeq, UserIDSeq, Vote_JoinDate, Vote_Item, nonce, Hash, Prev_Hash) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (voteCode, sid, currentTime, vote, nonce, req["hash"], "prev_hash"))
            print("User: {} 투표 데이터 추가".format(sid))

            if inserted == 0:
                print("User: {} 투표 데이터 추가 실패".format(sid))
                db.update("""
                DELETE FROM Vote_User 
                WHERE UserIDSeq = %s 
                      AND UniqueNumberSeq = %s
                """, (sid, voteCode))
                return jsonify({"success": False, "code": 97}), 500

            result = db.update("""
            UPDATE Vote_User 
            SET JoinAlready = 1 
            WHERE UserIDSeq = %s 
                  AND UniqueNumberSeq = %s
            """, (sid, voteCode))
            print("User: {} 투표 참여 완료 설정".format(sid))

            if result and inserted:
                print("User: {} 참여 완료".format(sid))
                return jsonify({"success": True, "code": 0}), 200
            else:
                print("User: {} 참여 실패".format(sid))
                return jsonify({"success": False, "code": 99}), 404
        else:
            return jsonify({"success": False, "code": 98}), 404
    except Exception as e:
        print(e)
        return jsonify({"success": False, "code": 99}), 500


# 회원가입 라우팅
@app.route("/info/login/regist", methods=["POST"])
def regist():
    try:
        req = request.get_json()

        salt = randString(16)

        # 중복되지않는 SID 생성
        while True:
            s_id = randString(20)
            r = db.execute("""
            SELECT COUNT(*) AS COUNT 
            FROM UserTable 
            WHERE UserIDSeq = %s
            """, (s_id))
            if r.pop()["COUNT"] == 0:
                break


        id_ = req["id"]
        password = req["password"]
        name = req["name"]
        sex = req["sex"]

        already = True if len(db.execute("""
        SELECT UserID 
        FROM UserTable 
        WHERE UserID = %s
        """, (id_))) > 0 else False

        if already:
            return jsonify({"success": False, "already": True}), 200
        
        result = db.update("""
        INSERT INTO UserTable 
        VALUES (%s, %s, HEX(AES_ENCRYPT(%s, SHA2(%s, 256))),
            %s, %s, %s)
        """, (s_id, id_, password, salt, salt, name, sex))

        if result is 0:
            return jsonify({"success": False, "already": False}), 200
        
        print("User registered:", s_id)

        return jsonify({"success": True, "already": False})
    except:
        return jsonify({"success": False, "already": False})


# 로그인
@app.route("/login", methods=["POST"])
def login():
    try:
        req = request.get_json()
        id_ = req["id"]
        password = req["password"]

        result = db.execute(
        """
        SELECT UserIDSeq 
        FROM UserTable
        WHERE UserID = %s
        AND AES_DECRYPT(UNHEX(Userpw), SHA2(
            (SELECT Salt FROM UserTable
            WHERE UserID = %s),
        256)) = %s
        """, (id_, id_, password))

        if len(result) == 0:
            print("Unknown user")
            return jsonify({"msg": "아이디와 비밀번호를 확인해주세요"}), 404
        elif len(result) > 1:
            return jsonify({"msg": "유저 데이터 에러, 관리자에게 문의하세요"}), 500

        db.update("""
        DELETE FROM UserLogin 
        WHERE UserIDSeq = %s
        """, (result[0]["UserIDSeq"]))

        # 토큰 유효시간 1시간
        expire = datetime.timedelta(hours=1)
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 유저 고유 ID로 토큰 발행
        access_token = create_access_token(identity=result[0]["UserIDSeq"], expires_delta=expire)

        db.update("""
        INSERT INTO UserLogin 
        VALUES (%s, %s, %s)
        """, (result[0]["UserIDSeq"], access_token, current_time))

        print(current_time, "User logged in:", access_token)
        return jsonify({"token": access_token}), 200
    except:
        return jsonify({"msg": "알 수 없는 오류", "token": ""}), 500


@app.route("/logout", methods=["POST"])
@jwt_required
def logout():
    try:
        current_user = get_jwt_identity()
        if db.update("""
        DELETE FROM UserLogin 
        WHERE UserIDSeq = %s
        """, (current_user)) == 0:
            return jsonify(False), 500
        print("User logout")
        return jsonify(True), 200
    except:
        return jsonify(False), 500


# 토큰 엑세스 확인 라우팅
@app.route("/access", methods=["GET"])
@jwt_required
def access():
    try:
        sid = get_jwt_identity()
        if accessCheck(sid, request.headers["Authorization"].split()[1]):
            # 클라이언트에게 성공 전달
            return jsonify(True), 200
        else:
            return jsonify(False), 401
    except:
        return jsonify(False), 500


# 토큰 만료 핸들링
@jwt.expired_token_loader
def expired_token():
    print("토큰 만료 됨")
    return jsonify({"msg": "토큰 만료 됨"}), 401


"""
응답코드
0: 성공
2: 인증 실패
70: 투표 정보 추가 실패
99: 알 수 없는 오류
"""
# 투표 생성 라우팅
@app.route("/create/vote", methods=["POST"])
@jwt_required
def create():
    try:
        if not accessCheck(get_jwt_identity(), request.headers["Authorization"].split()[1]):
            return jsonify({"code": 2}), 401

        req = request.get_json()
        
        # 중복되지않는 투표 고유 ID 생성
        while True:
            vote_id = randString(20)
            count = db.execute("""
            SELECT COUNT(*) AS COUNT 
            FROM Vote_Information 
            WHERE UniqueNumberSeq = %s
            """, (vote_id))
            if count.pop()["COUNT"] == 0:
                break

        # 중복되지않는 투표 참여 코드 생성
        while True:
            vote_code = randString(10)
            count = db.execute("""
            SELECT COUNT(*) AS COUNT 
            FROM Vote_Information 
            WHERE Vote_JoinCode = %s
            """, (vote_code))
            if count.pop()["COUNT"] == 0:
                break

        # 투표 명
        namev = req["vote_name"]

        # 투표 시작시간
        startv = "%s %s:00:00" % (req["vote_start"], str(req["vote_start_time"]).rjust(2, "0"))

        # 투표 종료시간
        endv = "%s %s:00:00" % (req["vote_end"], str(req["vote_end_time"]).rjust(2, "0"))

        # 투표 참여 권한 (0: 아무나, 1: 지정)
        permissionv = req["vote_permission"]

        # 투표 참여자ID 목록
        targetv = req["vote_target"]

        # 투표 참여 인원
        limit = req["vote_limit"]

        # 투표 항목
        itemv = ",".join(req["vote_item"])

        # 투표 생성
        affected = db.update("""
        INSERT INTO Vote_Information 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (vote_id, namev, get_jwt_identity(), vote_code, startv, endv, permissionv, limit, 0))
        
        affected_item = db.update("""
        INSERT INTO Vote_Item 
        VALUES (%s, %s)
        """, (vote_id, itemv))

        # 지정된 투표자만 투표가 가능할 경우 명단에 ID 추가
        if permissionv == 1:
            for target in targetv:
                try:
                    db.update("""
                    INSERT INTO Vote_User VALUES (%s, %s, %s)
                    """, (target, vote_id, 0))
                except Exception as e:
                    print(e)

        affected += db.update("""
            UPDATE Vote_Information 
            SET VoteCreated = 1 
            WHERE UniqueNumberSeq = %s
            """, (vote_id))

        # 투표 정보 추가 또는 투표 항목 추가를 실패한 경우
        if affected == 0 or affected_item == 0:
            return jsonify({"code": 70}), 500

        # 정상적으로 처리 됨
        return jsonify({"code": 0, "vote_code": vote_code}), 200
    except Exception as e:
        print(e)
        return jsonify({"code": 99}), 500


# 투표 결과 라우팅
@app.route("/info/vote/result", methods=["GET"])
@jwt_required
def result():
    result = accessCheck(get_jwt_identity(), request.headers["Authorization"].split()[1])
    return "<h1>Hello {}</h1>".format(str(result))


"""
응답코드
0: 성공
2: 인증 실패
99: 알 수 없는 아이디
"""
# 생성한 투표 데이터 조회
@app.route("/info/vote/created", methods=["GET"])
@jwt_required
def created_vote():
    try:
        sid = get_jwt_identity()
        if not accessCheck(sid, request.headers["Authorization"].split()[1]):
            return jsonify({"code": 2}), 401

        # 해당 유저가 생성한 투표 정보 조회
        vote = db.execute("""
        SELECT VoteName AS name, 
               Vote_JoinCode as code, 
               VoteStart AS start, 
               VoteEnd as end, 
               VotePermission AS permission, 
               VoteLimit as lim
        FROM Vote_Information 
        WHERE UserID = %s
        """, (sid))

        return jsonify({"code": 0, "vote": vote}), 200
    except Exception as e:
        print(e)
        return jsonify({"code": 99}), 500


"""
응답코드
0: 성공
2: 인증 실패
6: 해당 투표가 없거나 확인할 권한이 없음
99: 알 수 없는 아이디
"""
# 투표 상세 정보 조회 (참여자 수, 참여자 명단 등..)
@app.route("/info/vote/detail/<code>", methods=["GET"])
@jwt_required
def vote_detail(code):
    try:
        sid = get_jwt_identity()
        if not accessCheck(sid, request.headers["Authorization"].split()[1]):
            return jsonify({"code": 2}), 401

        # 투표 조회
        vote = db.execute("""
        SELECT UniqueNumberSeq
        FROM Vote_Information
        WHERE Vote_JoinCode = %s
              AND UserID = %s
        """, (code, sid))

        if not vote:
            return jsonify({"code": 6}), 404

        vote_id = vote[0]["UniqueNumberSeq"]

        vote_join_user_count = db.execute("""
        SELECT COUNT(*) AS users
        FROM Vote_Data
        WHERE UniqueNumberSeq = %s
        """, (vote_id))[0]["users"]

        vote_data_time = db.execute("""
        SELECT HOUR(Vote_JoinDate) AS hour,
               COUNT(*) AS count
        FROM Vote_Data
        WHERE UniqueNumberSeq = %s
        GROUP BY HOUR(Vote_JoinDate)
        """, (vote_id))

        # db.execute("""
        # SELECT COUNT(*) 
        # FROM Vote_Data
        # WHERE Uniqe
        # """)

        return jsonify({"code": 0, "vote": {
            "users": vote_join_user_count,
            "time": vote_data_time
        }}), 200
    except Exception as e:
        print(e)
        return jsonify({"code": 99}), 500


"""
응답코드
0: 성공
51: 이미 존재하는 아이디
99: 알 수 없는 아이디
"""
# 아이디 중복확인
@app.route("/check/id", methods=["POST"])
def check_id():
    try:
        req = request.get_json()
        print(req["id"])
        result = db.execute("""
        SELECT COUNT(*) AS COUNT 
        FROM UserTable 
        WHERE UserID = %s
        """, (req["id"]))

        if result[0]["COUNT"] == 0:
            return jsonify({"success": True, "code": 0}), 200
        else:
            return jsonify({"success": False, "code": 51}), 409
    except Exception as e:
        print(e)
        return jsonify({"success": False, "code": 99}), 500


"""
응답코드
0: 성공
2: 인증 실패
3: 해당 투표 없음
4: 참여 가능 인원 초과
5: 참여 명단에 없음
60: 투표 참여 기간 만료
"""
# 투표 정보조회 라우팅
@app.route("/join/<code>", methods=["GET"])
@jwt_required
def vote_info(code):
    print(code)
    try:
        sid = get_jwt_identity()
        if not accessCheck(sid, request.headers["Authorization"].split()[1]):
            return jsonify({"code": 2, "data": {}}), 401

        vote_data = db.execute("""
        SELECT UniqueNumberSeq, 
               VoteName, 
               u.UserID AS UserID, 
               u.UserName AS UserName, 
               VoteStart, 
               VoteEnd, 
               VotePermission, 
               VoteLimit, 
               VoteCreated 
        FROM 
               Vote_Information i, 
               UserTable u 
        WHERE Vote_JoinCode = %s AND u.UserIDSeq = i.UserID
        """, (code))

        # 만약 조회된 투표가 없을 경우
        if len(vote_data) == 0:
            print("투표가 존재하지 않습니다")
            return jsonify({"code": 3, "data": {}}), 404

        if (datetime.datetime.now() >= vote_data[0]["VoteEnd"]):
            print("해당 투표 참여 기간이 끝났습니다")
            return jsonify({"code": 60, "data": {}}), 403
        

        # 지정한 유저만 투표할 수 있는 경우 ID가 등록되어있는지 확인
        if vote_data[0]["VotePermission"] == 1:
            check = db.execute("""
            SELECT COUNT(*) AS COUNT 
            FROM Vote_User 
            WHERE UniqueNumberSeq = %s 
                  AND UserID = (SELECT UserID FROM UserTable WHERE UserIDSeq = %s) 
                  AND JoinAlready = 0
            """, (vote_data[0]["UniqueNumberSeq"], sid))

            # 참여자 명단에 ID가 없을 경우
            if check.pop()["COUNT"] is not 1:
                return jsonify({"code": 5, "data": {}}), 401
        # 아무나 참여 가능한 투표인 경우
        else:
            pass

        # 전체 참여자 수 제한
        total = db.execute("""
        SELECT VoteLimit 
        FROM Vote_Information 
        WHERE UniqueNumberSeq = %s
        """, (vote_data[0]["UniqueNumberSeq"]))

        # 참여자 제한이 0인 경우 제한 없음, 5 이상인 경우 제한 있음
        if total[0]["VoteLimit"] >= 5:
            # 현재 참여자 수
            participated = db.execute("""
            SELECT COUNT(*) AS COUNT 
            FROM Vote_User 
            WHERE UniqueNumberSeq = %s 
                  AND JoinAlready = 1
            """, (vote_data[0]["UniqueNumberSeq"]))

            # 만약 현재 참여자 수가 전체 참여자수보다 크거나 같을 경우 더이상 참여 불가능
            if total[0]["VoteLimit"] <= participated[0]["COUNT"]:
                return jsonify({"code": 4, "data": {}}), 200

        item_data = db.execute("""
        SELECT Vote_Item 
        FROM Vote_Item 
        WHERE UniqueNumberSeq = %s
        """, (vote_data[0]["UniqueNumberSeq"]))[0]

        items = item_data["Vote_Item"].split(",")

        res_data = {
            "name": vote_data[0]["VoteName"],
            "founder": "{}({})".format(vote_data[0]["UserName"], vote_data[0]["UserID"]),
            "start": vote_data[0]["VoteStart"],
            "end": vote_data[0]["VoteEnd"],
            "vote_code": vote_data[0]["UniqueNumberSeq"],
            "items": items
        }

        return jsonify({"code": 0, "data": res_data}), 200
    except Exception as e:
        print(e)
        return jsonify({"code": 99, "data": {}}), 500


# 이미지
@app.route("/img/<name>", methods=["GET"])
def img(name):
	return send_from_directory("img", name)


# JS
@app.route("/js/<name>", methods=["GET"])
def js(name):
	return send_from_directory("js", name)


# CSS
@app.route("/css/<name>", methods=["GET"])
def css(name):
	return send_from_directory("css", name)


@app.route("/<name>", methods=["GET"])
def redirect(name):
    return render_template("index.html")


if __name__ == "__main__":
    # 데이터베이스 인스턴스 생성
	db = database_manager("localhost", 3306, "root", "1234", "vote")
	app.run(debug=True, host='0.0.0.0', port='80')
