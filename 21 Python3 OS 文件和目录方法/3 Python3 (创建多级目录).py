# os.makedirs() 方法用于递归创建多层目录。
# 如果子目录创建失败或者已经存在，会抛出一个 OSError 的异常，Windows上Error 183 即为目录已经存在的异常错误。
# 如果第一个参数 path 只有一级，即只创建一层目录，则与 mkdir() 函数相同。


# !/usr/bin/python3

import os, sys

# 创建的目录
path = "./tmp/home/monthly/daily"

os.makedirs(path, exist_ok=True)


# 创建数据集目录
def creat_datasets_dir(dir):
    # 创建图片文件夹
    images_path = os.path.join(dir, 'images')
    os.makedirs(os.path.join(images_path, 'train'), exist_ok=True)
    os.makedirs(os.path.join(images_path, 'val'), exist_ok=True)


creat_datasets_dir("./tmp")


def setup_directories(dir_paths):
    """确保所有指定的目录存在"""
    for dir_path in dir_paths:
        os.makedirs(dir_path, exist_ok=True)


datasets_dir = "./tmp/datasets"

# 定义输出目录路径
output_dirs = {
    'train': {'images': os.path.join(datasets_dir, 'train', 'images'),
              'labels': os.path.join(datasets_dir, 'train', 'labels')},
    'val': {'images': os.path.join(datasets_dir, 'val', 'images'),
            'labels': os.path.join(datasets_dir, 'val', 'labels')},
    'test': {'images': os.path.join(datasets_dir, 'test', 'images'),
             'labels': os.path.join(datasets_dir, 'test', 'labels')}
}

# 确保所有输出目录存在
setup_directories([dir_path for sub_dict in output_dirs.values() for dir_path in sub_dict.values()])
