from flask import Flask


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello_world():
    return "第二次简单视图"


if __name__ == '__main__':
    app.run()