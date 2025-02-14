# Django 项目架构

- [Django](https://www.djangoproject.com/)
- [drf-yasg API官网](https://drf-yasg.readthedocs.io/en/stable/)

下面是一个简单的 Django 项目架构示例:

提供了一个基本的用户管理功能，包括用户的增删改查以及分页查询，并通过 Swagger3 生成了 API 文档。您可以根据需求进一步扩展和优化。

## 项目架构

1.项目结构

```text
    user_management/
    ├── manage.py
    ├── user_management/
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── users/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations/
    │   ├── models.py
    │   ├── serializers.py
    │   ├── tests.py
    │   ├── urls.py
    │   ├── views.py
    │   └── templates/
    │       └── users/
    │           ├── user_list.html
    │           ├── user_detail.html
    │           ├── user_form.html
    │           └── user_confirm_delete.html
    └── requirements.txt
    
```

2.主要功能模块

* 用户（User）：使用 Django 自带的 User 模型。
* 视图（Views）：实现用户的增删改查和分页查询。
* 模板（Templates）：用于展示用户信息。
* 序列化器（Serializers）：用于将 Django 模型转换为 JSON 格式。
* API 文档（Swagger3）：使用 drf-yasg 生成 API 文档。

## 项目依赖

```shell
# 全局安装
python -m pip install Django djangorestframework drf-yasg
```

swagger：`drf-yasg` 是一个用于生成和渲染 OpenAPI 3.0 规范的 Django 应用。

## 代码实现

1.创建 Django 项目和应用

```shell
django-admin startproject user_management
cd user_management
python manage.py startapp users
```

2.配置 settings.py

在 project_management/settings.py 中添加 projects 应用：

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'drf_yasg',
    'users',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}

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
}

```

3.定义序列化器 serializers.py

在 users/serializers.py 中定义用户序列化器：

```python
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active']

```

4.forms.py

```python
from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'is_staff', 'is_active']

```

5.创建视图 views.py

在 users/views.py 中创建视图函数：

```python
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from .forms import UserForm
from rest_framework import viewsets, permissions
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

def user_list(request):
    user_list = User.objects.all().order_by('username')
    paginator = Paginator(user_list, 10)  # 每页显示10个用户
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'users/user_list.html', {'page_obj': page_obj})

def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'users/user_detail.html', {'user': user})

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('user_detail', pk=user.pk)
    else:
        form = UserForm()
    return render(request, 'users/user_form.html', {'form': form, 'title': 'Create User'})

def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('user_detail', pk=user.pk)
    else:
        form = UserForm(instance=user)
    return render(request, 'users/user_form.html', {'form': form, 'title': 'Update User'})

def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'users/user_confirm_delete.html', {'object': user, 'object_type': 'User'})

```

6.配置 URL urls.py

在 users/urls.py 中配置 URL 路由：

```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


from django.urls import path
from .views import user_list, user_detail, user_create, user_update, user_delete

urlpatterns = [
    path('', user_list, name='user_list'),
    path('<int:pk>/', user_detail, name='user_detail'),
    path('create/', user_create, name='user_create'),
    path('<int:pk>/update/', user_update, name='user_update'),
    path('<int:pk>/delete/', user_delete, name='user_delete'),
]
```

在 user_management/urls.py 中包含 users 应用的 URL 和 Swagger 文档：

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
    path('', include('users.urls')),
    path('api/', include('users.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

```

7.创建模板

在 users/templates/users/ 目录下创建模板文件（与之前相同）：

* user_list.html: 显示用户列表，并提供分页功能。
* user_detail.html: 显示单个用户详细信息，并提供编辑和删除选项。
* user_form.html: 用于创建和编辑用户。
* user_confirm_delete.html: 用于确认删除用户。

示例模板 user_list.html：

```html
<!DOCTYPE html>
<html>
<head>
    <title>User List</title>
</head>
<body>
<h1>User List</h1>
<a href="{% url 'user_create' %}">Create New User</a>
<ul>
    {% for user in page_obj %}
    <li>
        <a href="{% url 'user_detail' pk=user.pk %}">{{ user.username }}</a>
        <a href="{% url 'user_update' pk=user.pk %}">Edit</a>
        <a href="{% url 'user_delete' pk=user.pk %}">Delete</a>
    </li>
    {% endfor %}
</ul>
<div>
        <span class="step-links">
            {% if page_obj.has_previous %}
                <a href="?page=1">&laquo; first</a>
                <a href="?page={{ page_obj.previous_page_number }}">previous</a>
            {% endif %}

            <span class="current">
                Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}.
            </span>

            {% if page_obj.has_next %}
                <a href="?page={{ page_obj.next_page_number }}">next</a>
                <a href="?page={{ page_obj.paginator.num_pages }}">last &raquo;</a>
            {% endif %}
        </span>
</div>
</body>
</html>

```

8.运行项目

```shell
# 数据迁移: 创建数据库表
python manage.py migrate
# 创建超级用户: admin/pass 123@qq.com
python manage.py createsuperuser
# 运行项目: 启动服务器
python manage.py runserver
```

* 访问 http://127.0.0.1:8000/ 查看用户列表
* 访问 http://127.0.0.1:8000/api/users/ 查看用户 API
* 访问 http://127.0.0.1:8000/swagger/ 查看 Swagger 文档
* 访问 http://127.0.0.1:8000/redoc/ 查看 ReDoc 文档
* 访问 http://127.0.0.1:8000/admin/ 登录管理后台
* 访问 http://127.0.0.1:8000/admin/auth/user/ 查看用户列表
