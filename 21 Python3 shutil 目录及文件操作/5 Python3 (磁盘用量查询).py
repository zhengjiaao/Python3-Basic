# demo_disk_usage.py
import shutil
import os

def get_disk_usage(path="."):
    """
    获取指定路径的磁盘使用情况

    Args:
        path (str): 要检查的路径，默认为当前目录

    Returns:
        tuple: (total, used, free) 磁盘空间信息（字节）
    """
    try:
        total, used, free = shutil.disk_usage(path)
        return total, used, free
    except Exception as e:
        print(f"获取磁盘使用情况失败: {e}")
        return None, None, None

def format_bytes(bytes_value):
    """
    将字节数格式化为人类可读的格式

    Args:
        bytes_value (int): 字节数

    Returns:
        str: 格式化后的字符串
    """
    if bytes_value is None:
        return "N/A"

    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_value < 1024.0:
            return f"{bytes_value:.2f}{unit}"
        bytes_value /= 1024.0
    return f"{bytes_value:.2f}PB"

def display_disk_usage(path="."):
    """
    显示磁盘使用情况的详细信息

    Args:
        path (str): 要检查的路径
    """
    total, used, free = get_disk_usage(path)

    if total is None:
        return

    # 计算使用率
    usage_percent = (used / total) * 100 if total > 0 else 0

    print(f"磁盘使用情况 ({os.path.abspath(path)}):")
    print("-" * 50)
    print(f"总空间: {format_bytes(total)}")
    print(f"已使用: {format_bytes(used)}")
    print(f"可用空间: {format_bytes(free)}")
    print(f"使用率: {usage_percent:.2f}%")
    print("-" * 50)

def check_multiple_paths():
    """
    检查多个路径的磁盘使用情况
    """
    paths = [".", os.path.expanduser("~")]

    # 根据操作系统添加系统路径
    if os.name == "nt":  # Windows
        paths.append("C:\\")
    else:  # Unix-like systems
        paths.extend(["/", "/home", "/tmp"])

    for path in paths:
        if os.path.exists(path):
            print(f"\n检查路径: {path}")
            display_disk_usage(path)

if __name__ == "__main__":
    # 原始功能：显示当前目录磁盘使用情况
    display_disk_usage(".")

    # 扩展功能：检查多个路径
    print("\n" + "="*60)
    print("多路径磁盘使用情况检查:")
    check_multiple_paths()
