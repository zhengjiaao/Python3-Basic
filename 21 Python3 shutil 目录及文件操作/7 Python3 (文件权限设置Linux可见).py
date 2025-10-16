# demo_chown.py
import shutil
import os
import getpass
import stat

def create_test_file(root_dir="tmp"):
    """
    在指定根目录下创建测试文件

    Args:
        root_dir (str): 根目录路径

    Returns:
        str: 测试文件的完整路径
    """
    # 确保根目录存在
    os.makedirs(root_dir, exist_ok=True)

    # 创建测试文件路径
    file_path = os.path.join(root_dir, "own_me.txt")

    # 创建测试文件
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("This is a test file for chown demonstration")

    return file_path

def demonstrate_chown():
    """
    演示使用 shutil.chown 设置文件属主
    """
    # 设置根目录为 tmp
    root_dir = "tmp"

    try:
        # 创建测试文件
        file_path = create_test_file(root_dir)
        print(f"测试文件创建完成: {file_path}")

        # 显示文件当前权限信息
        display_file_permissions(file_path)

        # 获取当前用户
        current_user = getpass.getuser()
        print(f"当前用户: {current_user}")

        # 尝试设置文件属主
        try:
            shutil.chown(file_path, user=current_user)
            print(f"✓ chown 成功，属主设为: {current_user}")

            # 显示更新后的权限信息
            display_file_permissions(file_path)

        except PermissionError:
            print("✗ chown 失败：权限不足（需要 root 权限或在 Windows 上）")
        except LookupError as e:
            print(f"✗ chown 失败：用户不存在 - {e}")
        except Exception as e:
            print(f"✗ chown 失败：{e}")

    except Exception as e:
        print(f"创建测试文件或设置属主过程中出现错误: {e}")
    finally:
        # 可选：清理测试文件
        # cleanup_test_file(file_path)
        pass

def display_file_permissions(file_path):
    """
    显示文件的权限和属主信息

    Args:
        file_path (str): 文件路径
    """
    try:
        file_stat = os.stat(file_path)
        print(f"文件权限信息:")
        print(f"  - 路径: {file_path}")
        print(f"  - 属主 UID: {file_stat.st_uid}")
        print(f"  - 属组 GID: {file_stat.st_gid}")
        print(f"  - 权限: {oct(stat.S_IMODE(file_stat.st_mode))}")
        print(f"  - 创建时间: {file_stat.st_ctime}")
    except Exception as e:
        print(f"获取文件权限信息失败: {e}")

def demonstrate_chmod(file_path):
    """
    演示使用 os.chmod 设置文件权限

    Args:
        file_path (str): 文件路径
    """
    try:
        # 设置文件权限为 644 (rw-r--r--)
        os.chmod(file_path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
        print("✓ chmod 成功，权限设为 644")

        # 显示更新后的权限
        display_file_permissions(file_path)

    except Exception as e:
        print(f"chmod 失败: {e}")

def cleanup_test_file(file_path):
    """
    清理测试文件

    Args:
        file_path (str): 要删除的文件路径
    """
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            print(f"已删除测试文件: {file_path}")
        except Exception as e:
            print(f"删除测试文件失败: {e}")

if __name__ == "__main__":
    demonstrate_chown()
