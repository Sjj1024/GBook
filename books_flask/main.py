from flask import Flask


# 集成配置类，添加到项目中
class Config(object):
    DEBUG = True


app = Flask(__name__)

# 项目导入配置类
app.config.from_object(Config)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    return "第二次简单视图"


if __name__ == '__main__':
    app.run()