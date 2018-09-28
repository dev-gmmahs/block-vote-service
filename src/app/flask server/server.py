from flask import Flask, request, render_template, send_from_directory, jsonify
from database import database_manager
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
import datetime
import hashlib
import random
import string
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

md5 = hashlib.md5()
md5.update("sample".encode())
app.config["JWT_SECRET_KEY"] = md5.hexdigest()
jwt = JWTManager(app)

db = None



# 토큰 검증
def accessCheck(sid, token):
    try:
        result = db.execute("SELECT UserIDSeq FROM UserLogin WHERE UserIDSeq = %s AND Token = %s", (sid, token))
        if result:
            return True
        else:
            return False
    except:
        return False



@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")



# 투표 제출
@app.route("/info/send/vote", methods=["POST"])
@jwt_required
def vote():
    try:
        if not accessCheck(get_jwt_identity(), request.headers["Authorization"].split()[1]):
            return jsonify({"success": False, "code": ""}), 401
        return jsonify({"success": False, "code": ""}), 200
    except:
        return jsonify({"success": False, "code": ""}), 500



# 회원가입 라우팅
@app.route("/info/login/regist", methods=["POST"])
def regist():
    try:
        req = request.get_json()

        salt = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(16))

        # 중복되지않는 SID 생성
        while True:
            s_id = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(20))
            r = db.execute("SELECT COUNT(*) AS COUNT FROM UserTable WHERE UserIDSeq = %s", (s_id))
            if r.pop()["COUNT"] == 0:
                break


        id_ = req["id"]
        password = req["password"]
        name = req["name"]
        resident = req["resident"]

        already = True if len(db.execute("SELECT UserID FROM UserTable WHERE UserID = %s", (id_))) > 0 else False

        if already:
            return jsonify({"success": False, "already": True}), 200
        
        result = db.update("""
        INSERT INTO UserTable VALUES (
            %s, %s,
            HEX(AES_ENCRYPT(%s, SHA2(%s, 256))),
            %s, %s, %s)
        """, (s_id, id_, password, salt, salt, name, resident))

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
        SELECT UserIDSeq FROM UserTable
        WHERE UserID = %s
        AND AES_DECRYPT(UNHEX(Userpw), SHA2(
            (SELECT Salt FROM UserTable
            WHERE UserID = %s),
        256)) = %s
        """, (id_, id_, password))

        if len(result) == 0:
            print("Unknown user")
            return jsonify({"msg": "Unknown user"}), 400
        elif len(result) > 1:
            return jsonify({"msg": "User data error"}), 500

        db.update("DELETE FROM UserLogin WHERE UserIDSeq = %s", (result[0]["UserIDSeq"]))

        # 토큰 유효시간 1시간
        expire = datetime.timedelta(hours=1)
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 유저 고유 ID로 토큰 발행
        access_token = create_access_token(identity=result[0]["UserIDSeq"], expires_delta=expire)

        db.update("INSERT INTO UserLogin VALUES (%s, %s, %s)", (result[0]["UserIDSeq"], access_token, current_time))

        print(current_time, "User logged in:", access_token)
        return jsonify({"token": access_token})
    except:
        return jsonify({"token": ""})



@app.route("/logout", methods=["POST"])
@jwt_required
def logout():
    try:
        current_user = get_jwt_identity()
        if db.update("DELETE FROM UserLogin WHERE UserIDSeq = %s", (current_user)) == 0:
            return jsonify(False), 500
        print("User logout")
        return jsonify(True), 200
    except:
        return jsonify(False), 500



# 토큰 엑세스 확인 라우팅
@app.route("/access", methods=["POST"])
@jwt_required
def access():
    try:
        if accessCheck(get_jwt_identity(), request.headers["Authorization"].split()[1]):
            return jsonify(True), 200
        else:
            return jsonify(False), 401
    except:
        # 클라이언트에게 성공 전달
        return jsonify(False), 401



# 토큰 만료 핸들링
@jwt.expired_token_loader
def expired_token():
    return jsonify({"msg": "토큰 만료 됨"}), 401



# 투표 생성 라우팅
@app.route("/create/vote", methods=["POST"])
@jwt_required
def create():
    try:
        if not accessCheck(get_jwt_identity(), request.headers["Authorization"].split()[1]):
            return jsonify({"success": False, "code": ""}), 401

        req = request.get_json()
        
        # 중복되지않는 투표 고유 ID 생성
        while True:
            vote_id = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(20))
            count = db.execute("SELECT COUNT(*) AS COUNT FROM Vote_Information WHERE UniqueNumberSeq = %s", (vote_id))
            if count.pop()["COUNT"] == 0:
                break

        # 중복되지않는 투표 참여 코드 생성
        while True:
            vote_code = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))
            count = db.execute("SELECT COUNT(*) AS COUNT FROM Vote_Information WHERE Vote_JoinCode = %s", (vote_code))
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
        INSERT INTO Vote_Information VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (vote_id, namev, get_jwt_identity(), vote_code, startv, endv, permissionv, limit, 0))
        
        affected_item = db.update("""
        INSERT INTO Vote_Item VALUES (%s, %s)
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

        # 투표 정보 추가 또는 투표 항목 추가를 실패한 경우
        if affected == 0 or affected_item == 0:
            return jsonify({"success": False, "code": ""}), 500

        # 정상적으로 처리 됨
        return jsonify({"success": True, "code": vote_code}), 200
    except Exception as e:
        print(e)
        return jsonify({"success": False, "code": ""}), 500



# 투표 결과 라우팅
@app.route("/info/vote/result", methods=["GET"])
@jwt_required
def result():
    result = accessCheck(get_jwt_identity(), request.headers["Authorization"].split()[1])
    return "<h1>Hello {}</h1>".format(str(result))



# 투표 정보조회 라우팅
@app.route("/join/<code>", methods=["GET"])
@jwt_required
def vote_info(code):
    print(code)
    try:
        sid = get_jwt_identity()
        if not accessCheck(sid, request.headers["Authorization"].split()[1]):
            return jsonify({"permission": False, "overlimit": False, "data": {}}), 401

        vote_data = db.execute("""
        SELECT UniqueNumberSeq, VoteName, u.UserID, u.UserName, VoteStart, VoteEnd, VotePermission, VoteLimit, VoteCreated 
        FROM Vote_Information i, UserTable u WHERE Vote_JoinCode = %s
        """, (code))

        # 만약 조회된 투표가 없을 경우
        if len(vote_data) == 0:
            return jsonify({"permission": False, "overlimit": False, "data": {}}), 404

        # 지정한 유저만 투표할 수 있는 경우 ID가 등록되어있는지 확인
        if vote_data[0]["VotePermission"] == 1:
            check = db.execute("""
            SELECT COUNT(*) AS COUNT FROM Vote_User 
            WHERE UniqueNumberSeq = %s AND UserID = (SELECT UserID FROM UserTable WHERE UserIDSeq = %s) AND JoinAlready = 0
            """, (vote_data[0]["UniqueNumberSeq"], sid))

            # 참여자 명단에 ID가 없을 경우
            if check.pop()["COUNT"] is not 1:
                return jsonify({"permission": False, "overlimit": False, "data": {}}), 401
        # 아무나 참여 가능한 투표인 경우
        else:
            pass

        # 전체 참여자 수 제한
        total = db.execute("""
        SELECT VoteLimit FROM Vote_Information WHERE UniqueNumberSeq = %s
        """, (vote_data[0]["UniqueNumberSeq"]))

        # 참여자 제한이 0인 경우 제한 없음, 5 이상인 경우 제한 있음
        if total[0]["VoteLimit"] >= 5:
            # 현재 참여자 수
            participated = db.execute("""
            SELECT COUNT(*) AS COUNT FROM Vote_User WHERE UniqueNumberSeq = %s AND JoinAlready = 1
            """, (vote_data[0]["UniqueNumberSeq"]))

            # 만약 현재 참여자 수가 전체 참여자수보다 크거나 같을 경우 더이상 참여 불가능
            if total[0]["VoteLimit"] <= participated[0]["COUNT"]:
                return jsonify({"permission": True, "overlimit": True, "data": {}}), 200

        return jsonify({"permission": True, "overlimit": False, "data": vote_data[0]}), 200
    except Exception as e:
        print(e)
        return jsonify({"permission": False, "overlimit": False, "data": {}}), 500



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



if __name__ == "__main__":
    # 데이터베이스 인스턴스 생성
	db = database_manager("localhost", 3306, "root", "1234", "vote")
	app.run(debug=True, host='0.0.0.0', port='80')
