from flask import Flask
import redis
# 集成配置类，添加到项目中
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf.csrf import CSRFProtect

class Config(object):
    DEBUG = True
    # 为数据库添加配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@127.0.0.1:3306/information27"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 配置Redis扩展
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

app = Flask(__name__)

# 项目导入配置类
app.config.from_object(Config)

# 配置数据库信息
db = SQLAlchemy(app)
# 初始化redis存储对象
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
# 开启CSRF保护
CSRFProtect(app)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    return "第二次简单视图"


if __name__ == '__main__':
    app.run()