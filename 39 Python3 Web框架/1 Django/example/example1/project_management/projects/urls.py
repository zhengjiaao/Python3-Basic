from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)

# urlpatterns = [
#     path('', views.project_list, name='project_list'),
#     path('project/<int:pk>/', views.project_detail, name='project_detail'),
#     path('project/<int:project_pk>/tasks/', views.task_list, name='task_list'),
#     path('project/<int:project_pk>/task/<int:task_pk>/', views.task_detail, name='task_detail'),
#     path('project/new/', views.project_create, name='project_create'),
#     path('project/<int:project_pk>/task/new/', views.task_create, name='task_create'),
# ]

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.project_list, name='project_list'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
    path('project/<int:project_pk>/tasks/', views.task_list, name='task_list'),
    path('project/<int:project_pk>/task/<int:task_pk>/', views.task_detail, name='task_detail'),
    path('project/new/', views.project_create, name='project_create'),
    path('project/<int:pk>/edit/', views.project_update, name='project_update'),
    path('project/<int:pk>/delete/', views.project_delete, name='project_delete'),
    path('project/<int:project_pk>/task/new/', views.task_create, name='task_create'),
    path('project/<int:project_pk>/task/<int:task_pk>/edit/', views.task_update, name='task_update'),
    path('project/<int:project_pk>/task/<int:task_pk>/delete/', views.task_delete, name='task_delete'),
]
