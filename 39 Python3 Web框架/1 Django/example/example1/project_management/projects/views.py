# 导入Django模块
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator

# 导入自定义模块
from .models import Project, Task
from .forms import ProjectForm, TaskForm
from .serializers import ProjectSerializer

# 导入DRF模块
from rest_framework import viewsets, permissions


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all().order_by('name')
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


def project_list(request):
    project_list = Project.objects.all().order_by('name')
    paginator = Paginator(project_list, 10)  # 每页显示10个项目
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'projects/project_list.html', {'page_obj': page_obj})


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
    return render(request, 'projects/project_form.html', {'form': form, 'title': 'Create Project'})


def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'projects/project_form.html', {'form': form, 'title': 'Update Project'})


def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    return render(request, 'projects/user_confirm_delete.html', {'object': project, 'object_type': 'Project'})


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
    return render(request, 'projects/task_form.html', {'form': form, 'title': 'Create Task', 'project': project})


def task_update(request, project_pk, task_pk):
    project = get_object_or_404(Project, pk=project_pk)
    task = get_object_or_404(Task, pk=task_pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', project_pk=project.pk, task_pk=task.pk)
    else:
        form = TaskForm(instance=task)
    return render(request, 'projects/task_form.html', {'form': form, 'title': 'Update Task', 'project': project})


def task_delete(request, project_pk, task_pk):
    project = get_object_or_404(Project, pk=project_pk)
    task = get_object_or_404(Task, pk=task_pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list', project_pk=project.pk)
    return render(request, 'projects/user_confirm_delete.html', {'object': task, 'object_type': 'Task'})
