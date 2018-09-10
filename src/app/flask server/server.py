from flask import Flask, request, render_template, send_from_directory, jsonify
from database import database_manager
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
import datetime
import hashlib

app = Flask(__name__)

md5 = hashlib.md5()
md5.update("sample".encode())
app.config["JWT_SECRET_KEY"] = md5.hexdigest()
jwt = JWTManager(app)

db = None

# 토큰 검증
def accessCheck(sid, token):
    result = db.execute("SELECT UserIDSeq FROM UserLogin WHERE UserIDSeq = %s AND Token = %s", (sid, token))
    if result:
        return True
    else:
        return False

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# 투표 제출
@app.route("/info/send/vote", methods=["POST"])
@jwt_required
def vote():
    return "<h1>Hello vote<h1>"

# 회원가입 라우팅
@app.route("/info/login/regist", methods=["POST"])
def regist():
    req = request.get_json()

    s_id = "test"
    salt = "test"

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
    
    print("User registered")

    return jsonify({"success": True, "already": False})

# 로그인
@app.route("/login", methods=["POST"])
def login():
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

@app.route("/logout", methods=["POST"])
@jwt_required
def logout():
    current_user = get_jwt_identity()
    db.update("DELETE FROM UserLogin WHERE UserIDSeq = %s", (current_user))
    print("User logout")
    return jsonify(True), 200

# 토큰 엑세스 확인 라우팅
@app.route("/access", methods=["POST"])
@jwt_required
def access():
    # 클라이언트에게 성공 전달
    return jsonify(True), 200

# 토큰 만료 핸들링
@jwt.expired_token_loader
def expired_token():
    return jsonify({"status": 401, "msg": "토큰 만료 됨"}), 401

# 투표 생성 라우팅
@app.route("/create/vote", methods=["POST"])
@jwt_required
def create():
	return "<h1>Hello create</h1>"

# 투표 결과 라우팅
@app.route("/info/vote/result", methods=["GET"])
@jwt_required
def result():
    result = accessCheck(get_jwt_identity(), request.headers["Authorization"].split()[1])
    return "<h1>Hello {}</h1>".format(str(result))

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

# 투표 참여 동적 라우팅
@app.route("/join/<code>")
@jwt_required
def join(code):
	return "<h1>Hello, %s!</h1>" % code

if __name__ == "__main__":
    # 데이터베이스 인스턴스 생성
	db = database_manager("localhost", 3306, "root", "1234", "vote")
	app.run(debug=True)