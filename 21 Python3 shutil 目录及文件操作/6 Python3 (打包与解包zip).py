# demo_archive.py
import shutil
import os

def create_test_files(root_dir="tmp"):
    """
    创建测试文件用于打包演示

    Args:
        root_dir (str): 根目录路径

    Returns:
        str: package目录的完整路径
    """
    package_dir = os.path.join(root_dir, "package")
    src_dir = os.path.join(package_dir, "src")

    # 创建目录结构
    os.makedirs(src_dir, exist_ok=True)

    # 创建测试文件
    for i in range(3):
        file_path = os.path.join(src_dir, f"{i}.txt")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"This is file {i}\nContent: {i}")

    # 创建一个额外的文件
    with open(os.path.join(package_dir, "README.txt"), "w", encoding="utf-8") as f:
        f.write("This is a test package for archive demonstration")

    return package_dir

def create_archive_demo():
    """
    演示使用 shutil.make_archive 创建压缩包
    """
    # 设置根目录为 tmp
    root_dir = "tmp"
    package_dir = os.path.join(root_dir, "package")
    backup_name = os.path.join(root_dir, "backup")

    try:
        # 创建测试文件
        created_package_dir = create_test_files(root_dir)
        print(f"测试文件创建完成，位于: {created_package_dir}")

        # 显示原始目录结构
        print("\n原始目录结构:")
        display_directory_tree(package_dir)

        # 打包 - 支持多种格式
        formats = ["zip", "tar", "gztar"]
        archive_paths = []

        for fmt in formats:
            try:
                archive_path = shutil.make_archive(backup_name, fmt, package_dir)
                archive_paths.append(archive_path)
                print(f"✓ {fmt.upper()} 打包完成: {archive_path}")
            except Exception as e:
                print(f"✗ {fmt.upper()} 打包失败: {e}")

        return archive_paths, root_dir

    except Exception as e:
        print(f"创建测试文件或打包过程中出现错误: {e}")
        return [], root_dir

def unpack_archive_demo(archive_paths, root_dir="tmp"):
    """
    演示使用 shutil.unpack_archive 解压压缩包

    Args:
        archive_paths (list): 压缩包路径列表
        root_dir (str): 根目录路径
    """
    try:
        for archive_path in archive_paths:
            if os.path.exists(archive_path):
                # 生成解压目录名
                base_name = os.path.splitext(os.path.basename(archive_path))[0]
                unpack_dir = os.path.join(root_dir, f"unpacked_{base_name}")

                # 解包
                shutil.unpack_archive(archive_path, unpack_dir)
                print(f"✓ {archive_path} 解包完成: {unpack_dir}")

                # 显示解包后的内容
                src_dir = os.path.join(unpack_dir, "src")
                if os.path.exists(src_dir):
                    print(f"  解包后 src 目录文件: {sorted(os.listdir(src_dir))}")

    except Exception as e:
        print(f"解包过程中出现错误: {e}")

def display_directory_tree(directory):
    """
    显示目录树结构

    Args:
        directory (str): 要显示的目录路径
    """
    for root, dirs, files in os.walk(directory):
        level = root.replace(directory, '').count(os.sep)
        indent = ' ' * 2 * level
        print(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 2 * (level + 1)
        for file in files:
            print(f"{subindent}{file}")

def cleanup_temp_files(root_dir="tmp"):
    """
    清理临时文件和目录

    Args:
        root_dir (str): 根目录路径
    """
    temp_items = ["package", "backup.zip", "backup.tar", "backup.tar.gz",
                  "unpacked_backup"]

    for item in temp_items:
        item_path = os.path.join(root_dir, item)
        if os.path.exists(item_path):
            if os.path.isfile(item_path):
                os.remove(item_path)
                print(f"已删除临时文件: {item_path}")
            else:
                shutil.rmtree(item_path)
                print(f"已删除临时目录: {item_path}")

if __name__ == "__main__":
    # 执行打包演示
    archive_paths, root_dir = create_archive_demo()

    # 执行解包演示
    if archive_paths:
        print("\n" + "="*50)
        print("解包演示:")
        unpack_archive_demo(archive_paths, root_dir)

    # 可选：清理临时文件
    # cleanup_temp_files(root_dir)
