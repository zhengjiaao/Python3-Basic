from django.urls import path, include
from .views import user_list, user_detail, user_create, user_update, user_delete

urlpatterns = [
    path('', user_list, name='user_list'),  # 访问用户列表
    path('<int:pk>/', user_detail, name='user_detail'),  # 访问单个用户详情
    path('create/', user_create, name='user_create'),  # 创建用户
    path('<int:pk>/update/', user_update, name='user_update'),  # 更新用户
    path('<int:pk>/delete/', user_delete, name='user_delete'),  # 删除用户
]
