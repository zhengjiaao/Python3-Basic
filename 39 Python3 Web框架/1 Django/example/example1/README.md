# Django 项目架构

- [Django](https://www.djangoproject.com/)
- [drf-yasg API官网](https://drf-yasg.readthedocs.io/en/stable/)

下面是一个简单的 Django 项目架构示例，用于实现一个基本的项目管理功能。这个示例包括项目、任务和用户的基本管理。

## 项目架构

1.项目结构

```text
    project_management/
    ├── manage.py
    ├── project_management/
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── projects/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations/
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    └── requirements.txt
    
```

2.主要功能模块

* 项目（Project）：包含项目的基本信息。
* 任务（Task）：包含任务的基本信息，关联到项目。
* 用户（User）：使用 Django 自带的 User 模型。

## 项目依赖

```shell
# 全局安装
python -m pip install Django djangorestframework drf-yasg
```

swagger：`drf-yasg` 是一个用于生成和渲染 OpenAPI 3.0 规范的 Django 应用。

## 代码实现

1.创建 Django 项目和应用

```shell
django-admin startproject project_management
cd project_management
python manage.py startapp projects
```

2.配置 settings.py

在 project_management/settings.py 中添加 projects 应用：

```python
INSTALLED_APPS = [
    ...
    'projects',
]

```

3.定义模型 models.py

在 projects/models.py 中定义项目和任务模型：

```python
from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Task(models.Model):
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

```

4.创建和应用迁移

```shell
python manage.py makemigrations projects
python manage.py migrate

```

5.注册模型到管理后台 admin.py

在 projects/admin.py 中注册项目和任务模型：

```python
from django.contrib import admin
from .models import Project, Task

admin.site.register(Project)
admin.site.register(Task)

```

6.创建视图 views.py

在 projects/views.py 中创建视图函数：

```python
from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Task
from .forms import ProjectForm, TaskForm


def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/project_detail.html', {'project': project})


def task_list(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    tasks = project.tasks.all()
    return render(request, 'projects/task_list.html', {'project': project, 'tasks': tasks})


def task_detail(request, project_pk, task_pk):
    project = get_object_or_404(Project, pk=project_pk)
    task = get_object_or_404(Task, pk=task_pk)
    return render(request, 'projects/task_detail.html', {'project': project, 'task': task})


def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm()
    return render(request, 'projects/project_form.html', {'form': form})


def task_create(request, project_pk):
    project = get_object_or_404(Project, pk=project_pk)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect('task_detail', project_pk=project.pk, task_pk=task.pk)
    else:
        form = TaskForm()
    return render(request, 'projects/task_form.html', {'form': form})

```

7.创建表单 forms.py
在 projects/forms.py 中创建表单：

```python
from django import forms
from .models import Project, Task


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'start_date', 'end_date']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'due_date', 'completed', 'assigned_to']

```

8.配置 URL urls.py

在 projects/urls.py 中配置 URL 路由：

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('project/<int:project_pk>/tasks/', views.task_list, name='task_list'),
    path('project/<int:project_pk>/task/<int:task_pk>/', views.task_detail, name='task_detail'),
    path('project/new/', views.project_create, name='project_create'),
    path('project/<int:project_pk>/task/new/', views.task_create, name='task_create'),
]

```

在 project_management/urls.py 中包含 projects 应用的 URL：

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('projects.urls')),
]

```

9.创建模板

在 projects/templates/projects/ 目录下创建模板文件：

* project_list.html
* project_detail.html
* task_list.html
* task_detail.html
* project_form.html
* task_form.html

示例模板 project_list.html：

```html
<!DOCTYPE html>
<html>
<head>
    <title>Projects</title>
</head>
<body>
<h1>Projects</h1>
<a href="{% url 'project_create' %}">Create New Project</a>
<ul>
    {% for project in projects %}
    <li>
        <a href="{% url 'project_detail' pk=project.pk %}">{{ project.name }}</a>
    </li>
    {% endfor %}
</ul>
</body>
</html>

```

运行项目

```shell
# 数据迁移: 创建数据库表
python manage.py migrate
# 创建超级用户: admin/pass 123@qq.com
python manage.py createsuperuser
# 运行项目: 启动服务器
python manage.py runserver
```

访问 http://127.0.0.1:8000/

查看项目列表，访问 http://127.0.0.1:8000/admin/ 使用超级用户登录管理后台。管理员账户：zhengja/pass

## 集成swagger3

1.确认 drf-yasg 已安装

```shell
pip install Django djangorestframework drf-yasg
```

2.配置 settings.py

在 user_management/settings.py 中进行以下配置：

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'drf_yasg',
    'users',
]

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'basic': {
            'type': 'basic'
        }
    },
    'USE_SESSION_AUTH': False,  # 禁用会话认证，使用 API 密钥或其他认证方式
    'DOC_EXPANSION': 'list',  # 展开所有 API 文档
    'SHOW_REQUEST_HEADERS': True,  # 显示请求头
    'SHOW_COMMON_ERROR_CODES': True,  # 显示常见错误代码
}
```

3.配置 URL urls.py

在 user_management/urls.py 中配置 Swagger 和 ReDoc 文档的 URL：

```python
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="User Management API",
        default_version='v1',
        description="API for managing users",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourdomain.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

```

4.运行项目

确保您的项目已经迁移并创建了超级用户：

```shell
# 数据迁移: 创建数据库表
python manage.py migrate
# 创建超级用户: admin/pass 123@qq.com
python manage.py createsuperuser
# 运行项目: 启动服务器
python manage.py runserver
```

5.查看 API 文档

访问 http://127.0.0.1:8000/swagger/ 查看 Swagger 文档。Swagger UI 提供了一个交互式的界面，您可以直接在浏览器中测试 API 请求。

ReDoc:

访问 http://127.0.0.1:8000/redoc/ 查看 ReDoc 文档。ReDoc 提供了一个简洁且易于阅读的文档界面。

6.配置多个应用的 API 文档

如果您有多个应用，每个应用都可以有自己的视图集（ViewSet）。drf-yasg 会自动收集所有注册的视图集并生成完整的 API 文档。

例如，假设您还有另一个应用 projects，其视图集配置如下：

projects/views.py

```python
from rest_framework import viewsets, permissions
from .models import Project
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('name')
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

```

在 projects/urls.py 中注册视图集：
```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

```

user_management/urls.py

确保在主 urls.py 中包含 projects 应用的 URL：

```python
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="User Management API",
      default_version='v1',
      description="API for managing users and projects",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@yourdomain.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/projects/', include('projects.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

```

7.查看完整的 API 文档

现在，访问 http://127.0.0.1:8000/swagger/ 或 http://127.0.0.1:8000/redoc/ 将会显示包含 users 和 projects 应用的所有 API 文档。
