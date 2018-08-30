# pip install flask flask_jwt_extended
"""
Flask 토큰 인증 예제입니다.
2018-08-30 이근혁
"""

from flask import Flask, jsonify, request, render_template
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
import datetime

app = Flask(__name__)

# Flask-JWT-Extended 설정
app.config['JWT_SECRET_KEY'] = 'super-secret'  # 서버 비밀 키 (서비스 시 변경!)
jwt = JWTManager(app)

print()

@app.route('/', methods=['GET'])
def main():
    return render_template("index.html")


# POST /login 라우팅
@app.route('/login', methods=['POST'])
def login():

    # username, password 필드 데이터 조회
    username = request.form['username']
    password = request.form['password']

    # username 또는 password가 없을 경우 에러메시지 전달
    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    # 토큰 유효시간 10초로 지정
    expire = datetime.timedelta(seconds=10)

    # Identity는 JSON으로 직렬화가능한 데이터로 지정가능
    access_token = create_access_token(identity=username, expires_delta=expire)

    # 출력
    print("아이디: {}, 비밀번호: {}\n엑세스 토큰: {}\n".format(username, password, access_token))

    # 엑세스 토큰 클라이언트에게 반환
    return jsonify(access_token=access_token), 200


# /protected 올바른 엑세스 토큰이 있어야 조회 가능
# 클라이언트에서 엑세스 토큰을 서버로 함께 전달해야 함
@app.route('/protected', methods=['GET'])
@jwt_required
def protected():
    # get_jwt_identity를 사용하여 현재 사용자의 ID에 액세스합니다.
    current_user = get_jwt_identity()

    # 출력
    print("{} 접근 성공".format(current_user))

    # 클라이언트에게 사용자 ID 전달
    return jsonify(logged_in_as=current_user), 200


# 토큰이 만료되었을 경우
@jwt.expired_token_loader
def expired_token():
    return jsonify({
        'status': 401,
        'sub_status': 42,
        'msg': '토큰 만료 됨'
    }), 401


if __name__ == '__main__':
    app.run(debug=True)