# Django Web框架

- [Django](https://www.djangoproject.com/)
- [drf-yasg API官网](https://drf-yasg.readthedocs.io/en/stable/)

## Django 安装

### 全局安装

```shell
# 全局安装
python -m pip install Django

# 查看版本
python -m django --version
4.2.5
```

### 在项目中使用

```python
import django

print(django.get_version())
```

## django 创建web框架

创建项目

```shell
django-admin startproject mysite

http://127.0.0.1:8000/
```

startproject 框架结构

```shell
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

启动服务

```shell
python manage.py runserver

# 也可以更改端口
python manage.py runserver 8080
python manage.py runserver 0.0.0.0:8000
```

### 创建一个  Polls app

创建 Polls app

要创建您的应用程序，请确保您与manage.py位于同一目录中，然后键入以下命令：

```shell
python manage.py startapp polls
```

框架结构

```shell
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

编写第一个 view

polls/views.py

```python
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

polls/urls.py

```python
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
```

mysite/urls.py

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
```

运行服务

```shell
python manage.py runserver

http://localhost:8000/polls/
# not
http://localhost:8000/
```
