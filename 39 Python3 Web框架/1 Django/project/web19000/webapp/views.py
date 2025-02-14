from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# 创建视图函数

# templates模版示例
def index(request):
    context = {
        'name': 'John',  # 可以是动态数据
    }
    return render(request, 'index.html', context)

def example(request):
    context = {}
    return render(request, 'example.html', context)

# 请求示例

def hello(request):
    return HttpResponse("Hello, web19000!")
