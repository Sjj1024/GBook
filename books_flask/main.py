from flask import Flask, session
# 集成配置类，添加到项目中
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session

class Config(object):
    DEBUG = True
    # 为数据库添加配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@127.0.0.1:3306/information27"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 配置redis
    REDIS_HOST = '127.0.0.1'  # 项目上线以后，这个地址就会被替换成真实IP地址，mysql也是
    REDIS_PORT = 6379

    # 设置密钥，可以通过 base64.b64encode(os.urandom(48)) 来生成一个指定长度的随机字符串
    SECRET_KEY = "ghhBljAa0uzw2afLqJOXrukORE4BlkTY/1vaMuDh6opQ3uwGYtsDUyxcH62Aw3ju"

    # flask_session的配置信息
    SESSION_TYPE = "redis"  # 指定 session 保存到 redis 中
    SESSION_USE_SIGNER = True  # 让 cookie 中的 session_id 被加密签名处理
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT, password="xiaoshen")  # 使用 redis 的实例
    PERMANENT_SESSION_LIFETIME = 24 * 60 * 60  # session 的有效期，单位是秒
    SESSION_PERMANENZT = False # 永久的，不过期的



app = Flask(__name__)

# 项目导入配置类
app.config.from_object(Config)

# 配置数据库信息
db = SQLAlchemy(app)
# 初始化redis存储对象
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
# 开启CSRF保护
CSRFProtect(app)
# 设置session保存指定位置
Session(app)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    # 将数据存储到redis
    session["name"] = "黑马培训版"
    return "第二次简单视图"


if __name__ == '__main__':
    app.run()