from flask import Flask, request, render_template, send_from_directory, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# 투표 제출
@app.route('/info/send/vote',method=["POST"])
def vote():
    return '<h1>Hello vote<h1>'

# 회원가입 라우팅
@app.route('/info/login/regist',method=["POST"])
def regist():
    return '<h1>Hello regist<h1>'

# 투표 제출
@app.route('/login',method=["POST"])
def login():
    return jsonify({"token": "test_token", "name": "Jiho"})

# 투표 생성 라우팅
@app.route('/create/vote',method=["POST"])
def create():
	return '<h1>Hello create</h1>'


# 투표 생성 라우팅
@app.route('/info/vote/result',method=["GET"])
def result():
	return '<h1>Hello result</h1>'

# js이미지
@app.route('/img/<name>')
def img(name):
	return send_from_directory('img', name)

# 투표 참여 동적 라우팅
@app.route('/join/<code>')
def join(code):
	return '<h1>Hello, %s!</h1>' % code

if __name__ == '__main__':
	app.run(debug=True)
