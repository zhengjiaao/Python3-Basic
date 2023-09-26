# Flask

# 安装

激活环境

```shell
mkdir myproject
cd myproject
py -3 -m venv .venv
```

安装

```shell
pip install Flask
```

## 简单示例

创建 hello.py

```python
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```

运行服务

```shell
flask --app hello.py run

http://127.0.0.1:5000
```

debug 模式运行服务

```shell
flask --app hello run --debug
```

## 其他示例

### HTML转义

```python
from markupsafe import escape


@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"
```

### Routing

```python
@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    return 'Hello, World'
```

可变的路由

```python
from markupsafe import escape


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'
```

### 唯一URL/重定向行为

```python
@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'
```

### URL 构建

```python
from flask import url_for


@app.route('/')
def index():
    return 'index'


@app.route('/login')
def login():
    return 'login'


@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'


with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
```

```shell
/
/login
/login?next=/
/user/John%20Doe
```

### HTTP Methods

默认情况下，路由只回答GET请求。

```python
from flask import request


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
```

get 和 post 方法示例

```python
@app.get('/login')
def login_get():
    return show_the_login_form()


@app.post('/login')
def login_post():
    return do_the_login()
```

### 静态文件

```python
url_for('static', filename='style.css')
```

文件必须以static/style.css的形式存储在文件系统中。

### 渲染模板

Flask会自动为您配置Jinja2模板引擎。
模板可以用于生成任何类型的文本文件。

```python
from flask import render_template


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
```

Flask将在templates文件夹中查找模板。
如果你的应用程序是一个模块，这个文件夹就在该模块旁边，如果它是一个包，它实际上就在你的包中：
module:

```shell
/application.py
/templates
    /hello.html
```

package:

```shell
/application
    /__init__.py
    /templates
        /hello.html
```

example template:

```shell
<!doctype html>
<title>Hello from Flask</title>
{% if name %}
  <h1>Hello {{ name }}!</h1>
{% else %}
  <h1>Hello, World!</h1>
{% endif %}
```

### 访问请求数据

```python
from flask import request

with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST'
```

### 请求对象

```python
from flask import request


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)
```

### 文件上传

上传文件示例

```python
from flask import request


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')
    ...
```

保存文件，并重命名文件

```python
from werkzeug.utils import secure_filename


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['the_file']
        file.save(f"/var/www/uploads/{secure_filename(file.filename)}")
    ...
```

### Cookies

读取 cookies:

```python
from flask import request


@app.route('/')
def index():
    username = request.cookies.get('username')
    # use cookies.get(key) instead of cookies[key] to not get a
    # KeyError if the cookie is missing.
```

存储 cookies:

```python
from flask import make_response


@app.route('/')
def index():
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp
```


### 重定向和错误
```python
from flask import abort, redirect, url_for


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login')
def login():
    abort(401)
    this_is_never_executed()
```

```python
from flask import render_template

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
```

### 关于 Responses

```python
from flask import render_template

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404
```

```python
from flask import make_response

@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp
```

### API JSON

编写API时，常见的响应格式是JSON。
如果您从视图返回dict或列表，它将被转换为JSON响应。
```python
@app.route("/me")
def me_api():
    user = get_current_user()
    return {
        "username": user.username,
        "theme": user.theme,
        "image": url_for("user_image", filename=user.image),
    }

@app.route("/users")
def users_api():
    users = get_all_users()
    return [user.to_json() for user in users]
```

### Sessions

为了使用会话，您必须设置一个密钥。以下是会话的工作方式：

```python
from flask import session

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    if 'username' in session:
        return f'Logged in as {session["username"]}'
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))
```

如何生成一个随机的秘钥
```shell
python -c 'import secrets; print(secrets.token_hex())'
```

### Logging 日志

```python
app.logger.debug('A value for debugging')
app.logger.warning('A warning occurred (%d apples)', 42)
app.logger.error('An error occurred')
```



