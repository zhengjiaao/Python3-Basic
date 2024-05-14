from flask import Flask
from index_routes import index_app
from user_routes import user_app
from role_routes import role_app

app = Flask(__name__)
# 中文乱码
app.json.ensure_ascii = False
app.config['JSON_AS_ASCII'] = False
# DEBUG
app.config['DEBUG'] = True

app.register_blueprint(index_app)
app.register_blueprint(user_app)
app.register_blueprint(role_app)

# 运行方式：python hello.py
# 启动 Flask 服务器 , 默认访问： http://127.0.0.1:5000
if __name__ == '__main__':
    app.run()
    # app.run(port=5000) # 默认端口号设置为 5000
    # app.run(debug=False, host="0.0.0.0", port=5000)

# 用户访问：http://127.0.0.1:5000/users
# 角色访问：http://127.0.0.1:5000/roles
