# backup_tool.py
import shutil
import os
import datetime

def backup(src_dir, dst_dir="tmp/backups"):
    """
    将指定目录打包为zip备份文件

    Args:
        src_dir (str): 要备份的源目录
        dst_dir (str): 备份文件存储目录，默认为 tmp/backups

    Returns:
        str: 备份文件路径，如果失败则返回 None
    """
    try:
        # 确保源目录存在
        if not os.path.exists(src_dir):
            print(f"错误：源目录 {src_dir} 不存在")
            return None

        # 确保目标目录存在
        os.makedirs(dst_dir, exist_ok=True)

        # 生成时间戳
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        base_name = os.path.join(dst_dir, f"backup_{timestamp}")

        # 创建备份
        archive_path = shutil.make_archive(base_name, "zip", src_dir)
        print("备份成功 ->", archive_path)

        # 显示备份文件信息
        if os.path.exists(archive_path):
            file_size = os.path.getsize(archive_path)
            print(f"备份文件大小: {file_size} 字节")

        return archive_path

    except Exception as e:
        print(f"备份失败: {e}")
        return None

def create_sample_project(root_dir="tmp"):
    """
    创建示例项目用于备份演示

    Args:
        root_dir (str): 根目录路径
    """
    project_dir = os.path.join(root_dir, "my_project")
    os.makedirs(project_dir, exist_ok=True)

    # 创建多个示例文件
    with open(os.path.join(project_dir, "main.py"), "w", encoding="utf-8") as f:
        f.write("# Main application file\nprint('Hello, World!')\n")

    with open(os.path.join(project_dir, "README.md"), "w", encoding="utf-8") as f:
        f.write("# My Project\nThis is a sample project for backup demonstration.")

    os.makedirs(os.path.join(project_dir, "src"), exist_ok=True)
    with open(os.path.join(project_dir, "src", "utils.py"), "w", encoding="utf-8") as f:
        f.write("# Utility functions\ndef hello():\n    return 'Hello from utils!'\n")

    print(f"示例项目创建完成: {project_dir}")
    return project_dir

def list_backups(backup_dir="tmp/backups"):
    """
    列出所有备份文件

    Args:
        backup_dir (str): 备份目录路径
    """
    if not os.path.exists(backup_dir):
        print(f"备份目录 {backup_dir} 不存在")
        return

    backups = [f for f in os.listdir(backup_dir) if f.endswith('.zip')]
    if backups:
        print(f"\n找到 {len(backups)} 个备份文件:")
        for backup in sorted(backups):
            print(f"  - {backup}")
    else:
        print("未找到备份文件")

if __name__ == "__main__":
    # 创建示例项目
    project_dir = create_sample_project("tmp")

    # 执行备份
    backup_path = backup(project_dir)

    # 列出备份文件
    list_backups()
