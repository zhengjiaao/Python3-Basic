# demo_rmtree.py
import shutil
import os

def remove_directory_tree_example():
    """
    演示使用 shutil.rmtree 彻底删除目录树
    """
    # 设置根目录为 tmp
    root_dir = "tmp"
    trash_dir = os.path.join(root_dir, "trash_dir")
    inside_dir = os.path.join(trash_dir, "inside")

    try:
        # 创建测试目录结构
        os.makedirs(inside_dir, exist_ok=True)

        # 在目录中创建一些测试文件
        with open(os.path.join(trash_dir, "file1.txt"), "w", encoding="utf-8") as f:
            f.write("test file 1")
        with open(os.path.join(inside_dir, "file2.txt"), "w", encoding="utf-8") as f:
            f.write("test file 2")

        print(f"删除前 {trash_dir} 存在？", os.path.exists(trash_dir))
        if os.path.exists(trash_dir):
            print(f"删除前目录内容：{os.listdir(trash_dir)}")

        # 彻底删除目录树
        shutil.rmtree(trash_dir)

        # 验证删除结果
        exists = os.path.exists(trash_dir)
        print(f"删除后 {trash_dir} 存在？", exists)

        if not exists:
            print("目录树删除成功")
        else:
            print("目录树删除失败")

    except Exception as e:
        print(f"删除过程中出现错误：{e}")
    finally:
        # 确保清理工作完成
        if 'trash_dir' in locals() and os.path.exists(trash_dir):
            try:
                shutil.rmtree(trash_dir)
            except:
                pass

def safe_remove_directory_tree(directory_path):
    """
    安全地删除目录树

    Args:
        directory_path (str): 要删除的目录路径
    """
    if os.path.exists(directory_path):
        try:
            shutil.rmtree(directory_path)
            print(f"成功删除目录：{directory_path}")
        except Exception as e:
            print(f"删除目录 {directory_path} 失败：{e}")
    else:
        print(f"目录不存在：{directory_path}")

if __name__ == "__main__":
    remove_directory_tree_example()
