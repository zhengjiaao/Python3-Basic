from django.urls import path

from . import views
from . import views_http_file
from . import views_http
from . import views_user
from . import views_swagger3

# 静态资源
from django.conf import settings
from django.conf.urls.static import static

# swagger3
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    # swagger3 路径配置
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),


    # 其他URL配置...
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

    # swagger3
    path('test/get/1', views_swagger3.MyAPIView.my_api_view1, name='my-api1'),
    path('test/get/2', views_swagger3.MyAPIView.my_api_view2, name='my-api2'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
