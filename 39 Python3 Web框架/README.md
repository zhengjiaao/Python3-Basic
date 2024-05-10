# Python3 Web框架

## uWSGI 安装配置

### Python 安装 uWSGI

```shell
pip install uwsgi
```

### 第一个 WSGI 应用

创建文件 foobar.py

```python
def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b"Hello World"]
```

uWSGI Python 加载器将会搜索的默认函数 application.
启动 uWSGI 来运行一个 HTTP 服务器，将程序部署在HTTP端口 9090 上：

```shell
uwsgi --http :9090 --wsgi-file foobar.py
```

## Python Web 常用框架汇总

| 框架      | 官网                                               | 推荐  | 介绍                                                                                                                   | 优缺点                                                                         |
|---------|--------------------------------------------------|-----|----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| Django  | [github](https://github.com/django/django.git)   | 强推荐 | Django 是最容易上手的框架。Django是一个功能强大且拥有丰富生态系统的全栈框架。它提供了大量的内置功能和工具，包括ORM、模板引擎、表单处理、用户认证等。Django的设计理念是开发效率和代码复用性，适合中大型项目的开发。 | Django的缺点是它相对较重，需要一些学习成本。同时，Django的ORM系统在处理复杂的多表关联查询时存在一些性能问题。              |
| Flask   | [flask](https://flask.palletsprojects.com/en)    | 推荐  | Flask 框架是python中的一个轻量级的前后端开发框架，flask只提供基础的功能，其他的功能需要安装各种插件。大型工程也可以使用flask框架，但是就需要安装很多插件。                             | Flask的缺点是它相对较轻，缺少一些常用的工具和插件，需要自己去寻找和配置。同时，Flask的灵活性也可能导致代码结构不够清晰，需要开发者自己规范。 |
| Tornado | [tornado](https://www.tornadoweb.org/en/stable/) | 不推荐 | Tornado 是一个Python web框架和异步网络库，通过使用非阻塞网络I/O, Tornado可以扩展到数以万计的开放连接，非常适合长轮询、WebSockets和其他需要与每个用户进行长时间连接的应用程序。          | Tornado的优点在于它的高性能和并发处理能力，适合处理大量的请求。Tornado的缺点在于它相对较难学习，需要一定的异步编程经验。         |
| Pyramid | [pyramid](https://github.com/Pylons/pyramid)     | 不推荐 | Pyramid 是一个灵活且可扩展的 Web 框架，适用于构建任何规模的 Web 应用程序。                                                                       | 灵活和可扩展，导致上手难度高                                                              |

### Django：

1. Django 是一个强大的全功能 Web 框架，适用于构建大型和复杂的 Web 应用程序。
2. 它提供了完整的 MVC（模型-视图-控制器）架构、ORM（对象关系映射）、表单处理、用户身份验证等功能。
3. Django 具备强大的安全性和自动化特性，包括自动生成管理界面和表单验证等功能。

### Flask：

1. Flask 是一个轻量级的 Web 框架，易于学习和使用。
2. 它具有简洁的核心，提供了基本的路由、请求处理和模板渲染功能，同时支持扩展以满足更复杂的需求。
3. Flask 拥有活跃的社区和丰富的扩展生态系统，可通过第三方库添加数据库支持、身份验证、表单处理等功能。

### Pyramid：

1. Pyramid 是一个灵活且可扩展的 Web 框架，适用于构建任何规模的 Web 应用程序。
2. 它提供了一个简单的核心，并支持选择性地添加更高级的功能，如 URL 路由、视图处理、会话管理等。
3. Pyramid 的设计理念是松散耦合的组件化架构，使开发人员能够根据需求选择和组合所需的功能。