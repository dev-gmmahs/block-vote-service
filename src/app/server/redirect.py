from flask import Flask, redirect

app = Flask(__name__)


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def main(path):
    return redirect("https://www.coidroid.com", code=302)


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port="7779")