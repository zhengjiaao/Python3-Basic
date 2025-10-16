# demo_copytree.py
import shutil
import os

def copy_directory_tree():
    """
    演示使用 shutil.copytree 复制整个目录树
    """
    # 设置根目录为 tmp
    root_dir = "tmp"
    src_dir = os.path.join(root_dir, "src_tree")
    dst_dir = os.path.join(root_dir, "dst_tree")

    try:
        # 创建源目录结构
        os.makedirs(os.path.join(src_dir, "sub"), exist_ok=True)

        # 创建多个测试文件
        with open(os.path.join(src_dir, "sub", "a.txt"), "w", encoding="utf-8") as f:
            f.write("This is file a")

        with open(os.path.join(src_dir, "b.txt"), "w", encoding="utf-8") as f:
            f.write("This is file b")

        # 如果目标目录已存在，先删除它
        if os.path.exists(dst_dir):
            shutil.rmtree(dst_dir)

        # 复制整个目录树
        shutil.copytree(src_dir, dst_dir)

        # 验证复制结果
        print("目录树复制完成")
        print(f"源目录结构: {os.listdir(src_dir)}")
        print(f"目标目录结构: {os.listdir(dst_dir)}")
        print(f"子目录文件: {os.listdir(os.path.join(dst_dir, 'sub'))}")

    except FileExistsError:
        print(f"目标目录 {dst_dir} 已存在")
    except Exception as e:
        print(f"复制过程中出现错误: {e}")
    finally:
        # 可选：清理临时目录
        # cleanup_directories([src_dir, dst_dir])
        pass

def cleanup_directories(directories):
    """
    清理临时目录
    """
    for directory in directories:
        if os.path.exists(directory):
            shutil.rmtree(directory)
            print(f"已删除临时目录: {directory}")

if __name__ == "__main__":
    copy_directory_tree()
