from django.http import HttpResponse
from django.http import JsonResponse
import json

from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view


# 无参 GET 请求
@api_view(['GET'])
@extend_schema(  # todo 无效
    tags=['Module 1'],
    description='This is the API description',
    responses={200: 'Success response'},
)
def get(request):
    if request.method == 'GET':
        # 处理 GET 请求逻辑

        # 返回字符串数据格式
        # return HttpResponse('This is a GET request without parameters.')

        # 返回json数据格式
        data = {
            'key1': 'value1',
            'key2': 'value2',
            'key3': 'This is a GET request without parameters.',
        }

        return JsonResponse(data)


# 带参数的 GET 请求
def get_with_param(request):
    if request.method == 'GET':
        # 获取查询字符串参数
        param1 = request.GET.get('param1')
        param2 = request.GET.get('param2')

        # 处理带参数的 GET 请求逻辑
        return HttpResponse(f'This is a GET request with parameters: param1={param1}, param2={param2}.')


# 无参 POST 请求
def post(request):
    if request.method == 'POST':
        # 处理 POST 请求逻辑

        # 返回字符串数据格式
        # return HttpResponse('This is a POST request without parameters.')

        # 返回json数据格式
        data = {
            'key1': 'value1',
            'key2': 'value2',
            'key3': 'This is a POST request without parameters.',
        }

        return JsonResponse(data)


# 带参数的 POST 请求：参数在form表单中
# 注：请求头中设置了正确的 Content-Type，即 "multipart/form-data"。
def post_with_param(request):
    if request.method == 'POST':
        # 获取 POST 请求体参数
        param1 = request.POST.get('param1')
        param2 = request.POST.get('param2')

        # 处理带参数的 POST 请求逻辑
        return HttpResponse(f'This is a POST request with parameters: param1={param1}, param2={param2}.')


# 带参数的 POST 请求：在视图函数中使用 request.body 属性来获取请求体中的原始数据，并使用 json 模块解析 JSON 对象。
# 注：请求头中设置了正确的 Content-Type，即 "application/json"。
def post_with_param_json(request):
    if request.method == 'POST':
        try:
            # 从请求体中获取原始数据
            request_data = request.body.decode('utf-8')
            # 将原始数据解析为 JSON 对象
            json_data = json.loads(request_data)

            # 处理带有 JSON 对象参数的 POST 请求逻辑
            param1 = json_data.get('param1')
            param2 = json_data.get('param2')

            return HttpResponse(f'This is a POST request with JSON parameters: param1={param1}, param2={param2}.')
        except json.JSONDecodeError:
            return HttpResponse('Invalid JSON data.', status=400)


# 无参 DELETE 请求
def delete(request):
    if request.method == 'DELETE':
        # 处理 DELETE 请求逻辑
        return HttpResponse('This is a DELETE request without parameters.')


# # 无参 PUT 请求
def put(request):
    if request.method == 'PUT':
        # 处理 PUT 请求逻辑
        return HttpResponse('This is a PUT request without parameters.')
