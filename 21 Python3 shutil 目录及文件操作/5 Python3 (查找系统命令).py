# demo_which.py
import shutil
import os
import sys

def find_executable_commands():
    """
    演示使用 shutil.which 查找系统可执行命令
    """
    # 要查找的常用命令列表
    commands = [
        "python3",
        "python",
        "git",
        "pip",
        "pip3",
        "ls" if os.name != "nt" else "dir",  # Unix vs Windows
        "echo",
        "mkdir"
    ]

    print("系统可执行命令查找结果：")
    print("-" * 50)

    found_commands = []
    for command in commands:
        path = shutil.which(command)
        if path:
            found_commands.append((command, path))
            print(f"✓ {command:<10}: {path}")
        else:
            print(f"✗ {command:<10}: 未找到")

    print("-" * 50)
    print(f"总共找到 {len(found_commands)} 个可用命令")

    return found_commands

def find_specific_command(command_name):
    """
    查找特定命令的路径

    Args:
        command_name (str): 要查找的命令名称

    Returns:
        str or None: 命令路径，如果未找到则返回None
    """
    path = shutil.which(command_name)
    if path:
        print(f"找到命令 '{command_name}' 在: {path}")
    else:
        print(f"未找到命令 '{command_name}'")
    return path

def get_system_info():
    """
    获取系统相关信息
    """
    print("\n系统信息:")
    print(f"操作系统: {os.name}")
    print(f"Python版本: {sys.version}")
    print(f"Python可执行文件路径: {sys.executable}")

if __name__ == "__main__":
    # 查找常用命令
    find_executable_commands()

    # 查找Python命令（原始功能）
    print("\nPython命令查找:")
    python_path = shutil.which("python3") or shutil.which("python")
    print("python 可执行文件路径：", python_path)

    # 获取系统信息
    get_system_info()
