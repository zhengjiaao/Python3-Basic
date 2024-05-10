from django.http import FileResponse
from django.templatetags.static import static
from django.conf import settings
from django.http import HttpResponse, Http404
import os
from pathlib import Path


# 创建目录
def create_dir(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


# 文件删除和下载

# =============文件上传==============
def upload_single_file(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']

        # 处理上传的文件
        # ...
        # 输出文件信息
        file_name = file.name
        file_size = file.size
        file_content = file.read()  # 读取文件内容

        print("File Name:", file_name)
        print("File Size:", file_size)
        # print("File Content:", file_content)

        # 保存文件到本地目录
        create_dir('path/to/save')
        with open(f'path/to/save/{file_name}', 'wb') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        return HttpResponse('File uploaded successfully.')
    return HttpResponse('File upload failed.')


def upload_single_file_with_param(request):
    if request.method == 'POST' and request.FILES.get('file') and request.POST.get('param'):
        file = request.FILES['file']
        param = request.POST['param']
        # 处理上传的文件和参数
        # ...
        # 输出文件信息
        file_name = file.name
        file_size = file.size
        file_content = file.read()  # 读取文件内容

        print("File Name:", file_name)
        print("File Size:", file_size)
        # print("File Content:", file_content)
        print("param:", param)

        # 保存文件到本地目录
        create_dir('path/to/save')
        with open(f'path/to/save/{file_name}', 'wb') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        return HttpResponse('File uploaded with parameter.')
    return HttpResponse('File upload failed.')


def upload_multiple_files(request):
    if request.method == 'POST' and request.FILES.getlist('files'):
        files = request.FILES.getlist('files')

        # 处理上传的多个文件
        # ...
        for file in files:
            # 输出文件信息
            file_name = file.name
            file_size = file.size
            file_content = file.read()  # 读取文件内容

            print("File Name:", file_name)
            print("File Size:", file_size)
            # print("File Content:", file_content)

            # 保存文件到本地目录
            with open(f'path/to/save/{file_name}', 'wb') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)

        return HttpResponse('Multiple files uploaded successfully.')
    return HttpResponse('File upload failed.')


def upload_multiple_files_with_param(request):
    if request.method == 'POST' and request.FILES.getlist('files') and request.POST.get('param'):
        files = request.FILES.getlist('files')
        param = request.POST['param']
        # 处理上传的多个文件和参数
        # ...
        for file in files:
            # 输出文件信息
            file_name = file.name
            file_size = file.size
            file_content = file.read()  # 读取文件内容

            print("File Name:", file_name)
            print("File Size:", file_size)
            # print("File Content:", file_content)
            print("param:", param)

            # 保存文件到本地目录
            with open(f'path/to/save/{file_name}', 'wb') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
        return HttpResponse('Multiple files uploaded with parameter.')
    return HttpResponse('File upload failed.')


# =============文件下载==============

# 按url下载
def download_file_url(request):
    # 假设要下载的资源文件路径是 settings.STATIC_ROOT 目录下的文件
    file_path = '/path/to/file.pdf'  # 替换为实际的资源文件路径

    # 获取项目根路径URL
    project_root_url = request.build_absolute_uri('/')
    print(project_root_url)  # http://127.0.0.1:19000

    # 构建资源文件的完整 URL
    file_url = request.build_absolute_uri(static(file_path))

    print(file_url)  # http://127.0.0.1:19000/static/path/to/file.pdf

    file_url = project_root_url + 'web19000' + static(file_path)

    return HttpResponse(file_url)

    # 渲染包含文件 URL 的模板
    # return render(request, 'download.html', {'file_url': file_url})

    # 返回包含文件 URL 的 JSON 响应
    # response_data = {
    #     'file_url': file_url
    # }
    #
    # # return HttpResponse(file_url)
    # return JsonResponse(response_data)


# 按url下载
def download_file_url(request):
    # 假设要下载的资源文件路径是 settings.STATIC_ROOT 目录下的文件
    file_path = '/path/to/file.pdf'  # 替换为实际的资源文件路径

    # 获取项目根路径URL
    project_root_url = request.build_absolute_uri('/')
    print(project_root_url)  # http://127.0.0.1:19000

    # 构建资源文件的完整 URL
    # file_url = request.build_absolute_uri(static(file_path))
    # print(file_url) # http://127.0.0.1:19000/static/path/to/file.pdf

    file_url = project_root_url + 'web19000' + static(file_path)

    print(file_url)  # http://127.0.0.1:19000/web19000/static/path/to/file.pdf

    return HttpResponse(file_url)


# 按文件流下载
def download_file_stream(request):
    # 假设要下载的文件路径是 settings.STATIC_ROOT 目录下的文件
    file_path = '/path/to/file.pdf'  # 替换为实际的文件路径

    # 构建资源文件的完整路径
    full_path = settings.STATIC_ROOT + file_path
    print(full_path)

    # 检查文件是否存在
    if not os.path.isfile(full_path):
        # raise Http404
        return HttpResponse('File not found.', status=404)

    # 打开文件并读取数据
    with open(full_path, 'rb') as file:
        file_data = file.read()

    # 创建HTTP响应对象，并设置文件流
    response = HttpResponse(file_data, content_type='application/octet-stream')
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(os.path.basename(full_path))

    return response


# def preview_file(request):
#     # 假设要下载的资源文件路径是 settings.STATIC_ROOT 目录下的文件
#     file_path = '/path/to/file.pdf'
#
#     # 构建资源文件的完整路径
#     full_path = settings.STATIC_ROOT + file_path
#     print(full_path)
#
#     # 检查文件是否存在
#     if not os.path.exists(full_path):
#         return HttpResponse('File not found.', status=404)
#
#     # 打开资源文件并创建 FileResponse 对象
#     try:
#         file = open(full_path, 'rb')
#         response = FileResponse(file)
#
#         # 设置响应的内容类型为资源文件的 MIME 类型
#         content_type = 'application/pdf'  # 替换为实际的资源文件 MIME 类型
#         response['Content-Type'] = content_type
#
#         # response = FileResponse(file, as_attachment=True, filename='file.pdf')
#
#         return response
#     except FileNotFoundError:
#         return HttpResponse('Resource not found.', status=404)


def is_safe_path(file_path):
    """
    验证文件路径是否安全，防止路径遍历攻击。
    """
    safe_path = Path(file_path)
    if safe_path.is_absolute() or '..' in safe_path.parts:
        return False
    return True


def preview_file(request):
    # 假设要下载的资源文件路径是 settings.STATIC_ROOT 目录下的文件
    file_path = '/path/to/file.pdf'

    # 使用 pathlib 提高代码可读性
    static_root_path = Path(settings.STATIC_ROOT)
    full_path = static_root_path / file_path

    # 日志代替print
    print(f"Attempting to open file: {full_path}")

    # 边界条件和输入验证
    if not is_safe_path(str(file_path)):
        return HttpResponse('Invalid file path.', status=400)

    # 检查文件是否存在
    if not full_path.exists():
        return HttpResponse('File not found.', status=404)

    # 尝试打开文件并处理
    try:
        with open(full_path, 'rb') as file:
            response = FileResponse(file, content_type='application/pdf')
            # 设置响应头，以附件形式下载文件
            # response['Content-Disposition'] = 'attachment; filename="file.pdf"'

            # todo 无效设置，设置响应头，以内联形式预览文件
            # response['Content-Disposition'] = 'inline; filename="file.pdf"'
            # 设置Content-Disposition和Content-Type头部
            # response['Content-Disposition'] = f'inline; filename="file.pdf"'
            # response['Content-Type'] = 'application/pdf'

            return response
    except FileNotFoundError:
        return HttpResponse('Resource not found.', status=404)
    except IOError as e:
        # 增加对文件读取异常的处理
        print(f"Error opening file: {e}")
        return HttpResponse('Error opening file.', status=500)
