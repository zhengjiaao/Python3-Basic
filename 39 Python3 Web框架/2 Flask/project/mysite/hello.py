from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route("/hello")
def hello_world2():
    return "<p>Hello, World!</p>"


@app.route('/about')
def about():
    return 'About page'


# 运行方式：python hello.py
# 启动 Flask 服务器 , 默认访问： http://127.0.0.1:5000
if __name__ == '__main__':
    app.run()
    # app.run(debug=True)
    # app.run(port=5000) # 默认端口号设置为 5000
