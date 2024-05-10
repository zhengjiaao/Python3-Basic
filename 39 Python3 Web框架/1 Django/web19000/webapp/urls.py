from django.urls import path

from . import views
from . import views_http_file
from . import views_http
from . import views_user

# 静态资源
from django.conf import settings
from django.conf.urls.static import static

# 配置路由
urlpatterns = [
    path("index", views.index, name="index"),
    path("example", views.example, name="example"),
    path("hello", views.hello, name="hello"),

    # http请求：get、post、put、delete等带参数和不带参数
    path("http/get", views_http.get, name="get"),
    path("http/get/param", views_http.get_with_param, name="get_with_param"),
    path("http/post", views_http.post, name="post"),
    path("http/post/param", views_http.post_with_param, name="post_with_param"),
    path("http/post/param/json", views_http.post_with_param_json, name="post_with_param_json"),
    path("http/delete", views_http.delete, name="delete"),
    path("http/put", views_http.put, name="put"),

    # http file请求：文件上传、下载
    path('http/upload/single/file', views_http_file.upload_single_file, name='upload_single_file'),
    path('http/upload/single/file/param', views_http_file.upload_single_file_with_param,
         name='upload_single_file_with_param'),
    path('http/upload/multiple/files', views_http_file.upload_multiple_files,
         name='upload_multiple_files'),
    path('http/upload/multiple/files/param', views_http_file.upload_multiple_files_with_param,
         name='upload_multiple_files_with_param'),
    path('http/download/file/url', views_http_file.download_file_url, name='download_file_url'),
    path('http/download/file/stream', views_http_file.download_file_stream, name='download_file_stream'),
    path('http/preview/file', views_http_file.download_file_stream, name='preview_file'),

    # 用户管理模块
    path('user/register/', views_user.register, name='register'),
    path('user/login/', views_user.login_view, name='login'),
    path('user/logout/', views_user.logout_view, name='logout'),
    path('user/profile/', views_user.profile, name='profile'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
