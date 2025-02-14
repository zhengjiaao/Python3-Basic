# Create your views here.
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
