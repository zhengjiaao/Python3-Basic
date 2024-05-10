# web19000

## 创建应用服务流程

创建Django web框架应用:

* 应该名称：web19000
* 根路径：web19000
* 端口为：19000

要创建一个名为 "web19000" 的 Django Web 框架，你可以按照以下步骤进行操作：

1. 创建 Django 项目：
   打开终端或命令行工具，并导航到你想创建项目的目录。然后运行以下命令来创建 Django 项目：

   ```shell
   django-admin startproject web19000
   ```

   这将创建一个名为 "web19000" 的 Django 项目文件夹。

2. 进入项目目录：
   使用以下命令进入项目文件夹：

   ```shell
   cd web19000
   ```

3. 创建 Django 应用：
   在项目文件夹中，你可以创建一个 Django 应用来承载你的 Web 框架。运行以下命令创建应用：

   ```shell
   python manage.py startapp webapp
   ```

   这将在项目文件夹中创建一个名为 "webapp" 的应用。

4. 配置根路径和端口：
   打开 `web19000` 文件夹下的 `web19000/settings.py` 文件，并找到 `ALLOWED_HOSTS` 和 `PORT` 设置。将它们的值更改为以下内容：

   ```python
   ALLOWED_HOSTS = ['*']
   PORT = 19000
   ```

   这将允许所有的主机访问你的应用，并将应用的端口设置为 19000。

5. 配置路由：
   5.1 打开 `web19000` 文件夹下的 `web19000/urls.py` 文件，并添加以下代码：

   ```python
   from django.contrib import admin
   from django.urls import include, path
   
   # 配置路由
   urlpatterns = [
       path("web19000/", include("webapp.urls"))
   ]
   ```

   5.2 在 `web19000` 项目文件夹下 **新增** `webapp/urls.py` 文件，配置路由修改如下：

   ```python
   from django.urls import path
   
   from . import views
   
   # 配置路由
   urlpatterns = [
       path("", views.index, name="index"),
   ]
   ```

   这将将根路径映射到名为 `index` 的视图函数，你需要在后面的步骤中创建该视图函数。

6. 创建视图函数：
   打开 `web19000` 文件夹下的 `webapp/views.py` 文件，并添加以下代码：

   ```python
   from django.http import HttpResponse
   
   def index(request):
       return HttpResponse("Hello, web19000!")
   ```

   这是一个简单的视图函数，它返回一个包含 "Hello, web19000!" 的 HTTP 响应。

7. 运行开发服务器：
   在终端或命令行工具中，确保你仍然在 `web19000` 项目文件夹中，然后运行以下命令来启动 Django 开发服务器：

   ```shell
   python manage.py runserver 0.0.0.0:19000
   ```

   这将在指定的端口（19000）上启动开发服务器。

现在，你的 "web19000" Django Web 框架已经创建并运行了。你可以在浏览器中访问 `http://localhost:19000/web19000` 来查看 "
Hello,
web19000!" 的消息。

请注意，这只是一个简单的示例，你可以根据需要进行更复杂的配置和功能开发。

### 修改访问根路径

如果你希望在 Django 项目中访问根路径 `/web19000`，而不是默认的根路径 `/`，你可以按照以下步骤进行操作：

1. 在 `web19000` 项目文件夹下的 `web19000/urls.py` 文件中，将代码修改如下：

```python
from django.urls import include, path

# 配置路由
urlpatterns = [
    path("web19000/", include("webapp.urls"))
]
```

2. 在 `web19000` 项目文件夹下 新增 `webapp/urls.py` 文件，配置路由修改如下：

```python
from django.urls import path

from . import views

# 配置路由
urlpatterns = [
    path("", views.index, name="index"),
]
```

3. 在 `web19000` 项目文件夹下的 `webapp/views.py` 文件中，将 `index` 视图函数的代码修改如下：

```python
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, web19000 root!")
```

在上面的代码中，我们将视图函数返回的消息修改为 "Hello, web19000 root!"。

4. 运行开发服务器：
   在终端或命令行工具中，确保你仍然在 `web19000` 项目文件夹中，然后运行以下命令来启动 Django 开发服务器：

```shell
python manage.py runserver 0.0.0.0:19000
```

这将在指定的端口（19000）上启动开发服务器。

现在，你可以在浏览器中访问 `http://localhost:19000/web19000/` 来查看 "Hello, web19000 root!" 的消息。

请注意，这只是一个示例，你可以根据需求进行更复杂的路由设置和视图函数的开发。

## Django 模块或文件

### Django 模块或文件简要说明：

在 Django 中，admin、models、apps、views、tests 和 urls 是常见的命名模块或文件，它们在开发 Django
应用程序时具有不同的功能和作用。下面是对每个模块或文件的简要说明：

1. admin： admin 模块用于创建后台管理界面，使你能够轻松管理你的应用程序的数据和功能。你可以在 admin.py
   文件中注册模型，并定义模型在后台管理界面中的显示和操作方式。通过 Django 的后台管理系统，你可以执行诸如创建、编辑、删除对象等操作。
2. models： models 模块用于定义应用程序的数据模型，也就是数据库中的表结构。你可以在 models.py
   文件中定义模型类，每个模型类代表数据库中的一个表。模型类的字段定义了表中的列，以及与其他模型之间的关联关系。通过使用
   Django 的模型类，你可以轻松地进行数据库操作和数据验证。
3. apps： apps 模块用于管理 Django 项目中的应用程序。在 apps.py 文件中，你可以配置应用程序的元数据，例如应用程序的名称、标签和配置信息。此外，你还可以在
   apps.py 文件中定义应用程序的配置类，用于自定义应用程序的行为。
4. views： views 模块用于处理用户请求并生成响应。在 Django 中，视图函数负责处理 URL 映射到的特定页面或资源。你可以在
   views.py 文件中定义视图函数，通过接收请求对象并返回响应对象来实现特定的业务逻辑。视图函数通常与模板（Templates）一起使用，以渲染
   HTML 页面或返回 JSON 数据。
5. tests： tests 模块用于编写和运行测试代码，以验证应用程序的功能和行为是否正确。你可以在 tests.py
   文件中编写单元测试用例，涵盖模型、视图、表单等不同组件的测试。通过编写测试用例，你可以确保代码的正确性，并在进行更改或添加新功能时避免引入错误。
6. urls： urls 模块用于定义 URL 路由和视图之间的映射关系。在 Django 中，你可以在 urls.py 文件中定义 URL 模式，指定 URL
   路径与相应的视图函数或类之间的关联。这样，当用户访问特定 URL 时，Django 将根据配置的 URL 模式将请求分发给相应的视图进行处理。

这些模块和文件在 Django 应用程序开发中扮演着重要的角色，帮助你组织和实现应用程序的不同方面。它们之间有着密切的联系和依赖关系，共同构成了一个完整的
Django 应用程序。

### Django 模块或文件使用示例：

1. Django Admin 示例：
   `admin.py` 文件示例，用于在后台管理界面注册模型（如 `Book`）：

   ```python
   from django.contrib import admin
   from .models import Book
   
   admin.site.register(Book)
   ```

2. Django Models 示例：
   `models.py` 文件示例，定义了一个 `Book` 模型类，表示图书：

   ```python
   from django.db import models
   
   class Book(models.Model):
       title = models.CharField(max_length=100)
       author = models.CharField(max_length=100)
       publication_date = models.DateField()
   
       def __str__(self):
           return self.title
   ```

3. Django Apps 示例：
   `apps.py` 文件示例，定义了一个应用程序的配置类：

   ```python
   from django.apps import AppConfig
   
   class MyAppConfig(AppConfig):
       name = 'myapp'
       verbose_name = 'My Application'
   ```

4. Django Views 示例：
   `views.py` 文件示例，定义了一个简单的视图函数，用于处理 HTTP 请求并返回响应：

   ```python
   from django.shortcuts import render
   from django.http import HttpResponse
   
   def index(request):
       return HttpResponse("Hello, World!")
   ```

5. Django Tests 示例：
   `tests.py` 文件示例，包含一个简单的测试用例，验证某个功能的正确性：

   ```python
   from django.test import TestCase
   
   class MyTestCase(TestCase):
       def test_something(self):
           response = self.client.get('/myapp/')
           self.assertEqual(response.status_code, 200)
   ```

6. Django URLs 示例：
   `urls.py` 文件示例，定义了 URL 路由和对应的视图函数关联：

   ```python
   from django.urls import path
   from . import views
   
   urlpatterns = [
       path('', views.index, name='index'),
   ]
   ```

以上示例仅提供了每个部分的基本示例，实际应用程序可能会更复杂，并涉及更多的模型、视图、URL 配置和测试用例。你可以根据你的应用程序需求进行进一步的定制和扩展。

## Django加载static静态资源文件

在 Django 中加载静态资源文件（例如 CSS、JavaScript 和图像文件）需要进行以下配置：

1. 在项目的根目录中创建一个名为 static 的目录。可以使用以下命令创建：

```shell
mkdir static
```

2. 将您的静态资源文件（例如 CSS、JavaScript 文件和图像文件）放置在 static 目录中。您可以根据需要进行组织和子目录嵌套。

```text
your_project/
├── your_app/
│   ├── ...
├── static/
│   ├── css/
│   │   └── styles.css
│   ├── js/
│   │   └── script.js
│   └── images/
│       └── logo.png
├── ...
```

3. 在 settings.py 文件中，确保以下设置正确配置：

```python
# settings.py

# ...

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# ...
```

* STATIC_URL：指定静态文件的URL前缀，一般为 '/static/'。
* STATICFILES_DIRS：指定要查找静态文件的目录列表。在上述示例中，我们将 STATICFILES_DIRS 设置为包含项目根目录下的 static 目录。

4. 在模板中加载静态文件。在您的模板文件中，使用 {% load static %} 模板标签加载静态文件，并使用 static 模板标签来引用静态文件的URL。

```html
<!-- example.html -->

{% load static %}

<link rel="stylesheet" type="text/css" href="{% static 'css/styles.css' %}">
<script src="{% static 'js/script.js' %}"></script>
<img src="{% static 'images/logo.png' %}" alt="Logo">
```

在上述示例中，我们使用了 {% static '...' %} 模板标签来引用静态文件的URL。这将根据 STATIC_URL 设置自动生成正确的URL路径。

5. 运行开发服务器。启动 Django 开发服务器，确保静态文件的URL正确解析和加载。

```shell
python manage.py runserver

#or 把静态文件从各个应用程序的 static 目录复制到指定的静态文件目录中。然后，Django 可以正确提供这些静态文件。
python manage.py collectstatic
```

## Django加载index.html模板

按照以下步骤进行操作：

1. 确认模板文件位置：确保index.html模板文件位于您的Django项目中的正确位置。根据Django的默认设置，它应该位于应用程序的templates目录中。
2. 创建正确的模板路径：根据您的项目结构，创建正确的模板路径。例如，如果您的项目结构如下所示：

```angular2html
your_project/
├── your_app/
│   ├── templates/
│   │   └── index.html
│   ├── ...
│   └── ...
├── ...
└── ...
```

您的index.html模板文件应该位于your_project/your_app/templates/index.html路径下。

3. 重新运行开发服务器：如果您已经移动了模板文件或进行了其他更改，请确保重新启动Django开发服务器，以便Django能够检测到更改并正确加载模板文件。

4. 在 Django 的 settings.py 文件中，确保正确配置了 INSTALLED_APPS 和 TEMPLATES 设置，以便 Django 能够正确加载模板。以下是一个示例配置：

```python
# settings.py

# ...

INSTALLED_APPS = [
    # 其他应用...
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'your_app',  # 将您的应用程序添加到这里
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            # 可选的模板引擎选项
            # ...
        },
    },
]

# ...
```

在上面的示例中，确保在 INSTALLED_APPS 列表中包含了您的应用程序，用 'your_app' 表示。这使得 Django 知道要加载您应用程序中的模板。

在 TEMPLATES 列表中，设置 'APP_DIRS': True，以便 Django 在应用程序的 templates
目录中查找模板。如果您的模板位于其他目录，可以通过 'DIRS' 设置添加这些目录的路径。

## Django配置swagger3

1. 安装 drf-spectacular 库：

```shell
pip install drf-spectacular
```

2. 在 Django 项目的设置文件（settings.py）中添加以下配置：

```python
INSTALLED_APPS = [
    # Other installed apps
    'drf_spectacular',
    'rest_framework',
]

# 配置 REST framework
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

# 配置 drf-spectacular
SPECTACULAR_SETTINGS = {
    'TITLE': 'API Documentation',
    'DESCRIPTION': 'Your API description',
    # 其他配置选项...
}
```

3. 在项目的 URL 配置文件（urls.py）中添加以下代码：

```python
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    # 其他 URL 配置...
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
```

4. 在您的 API 视图中，使用 @extend_schema 装饰器来配置 Swagger 文档。例如：

```python
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
@extend_schema(
    description='This is the API description',
    responses={200: 'Success response'},
)
def my_api_view(request):
    # Your code here
    return Response('Success')
```

5. 运行您的 Django 项目，并访问 /api/schema/swagger-ui/ 或 /api/schema/redoc/，您将看到相应的 Swagger UI 或 ReDoc
   页面，其中包含了您配置的 API 文档信息。
