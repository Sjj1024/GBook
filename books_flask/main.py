from flask import Flask


# 集成配置类，添加到项目中
from flask_sqlalchemy import SQLAlchemy


class Config(object):
    DEBUG = True
    # 为数据库添加配置
    SQLALCHEMY_DATABASE_URL = "mysql://root:root@127.0.0.1:3306/information27"
    SQLALCHEMY_TRACK_MODIFICSTIONS = False

app = Flask(__name__)

# 项目导入配置类
app.config.from_object(Config)

# 配置数据库信息
db = SQLAlchemy(app)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    return "第二次简单视图"


if __name__ == '__main__':
    app.run()