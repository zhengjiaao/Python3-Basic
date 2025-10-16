# demo_move.py
import shutil
import os

def move_file_example():
    """
    演示使用 shutil.move 移动文件
    """
    # 设置根目录为 tmp
    root_dir = "tmp"
    from_dir = os.path.join(root_dir, "from_dir")
    source_file = os.path.join(from_dir, "move_me.txt")
    destination_file = os.path.join(root_dir, "move_me.txt")

    try:
        # 创建源目录和文件
        os.makedirs(from_dir, exist_ok=True)
        with open(source_file, "w", encoding="utf-8") as f:
            f.write("move me")

        # 确保目标文件不存在，避免冲突
        if os.path.exists(destination_file):
            os.remove(destination_file)

        # 移动文件
        shutil.move(source_file, destination_file)

        # 验证移动结果
        print("移动成功")
        print("移动后目录文件：", [x for x in os.listdir(root_dir) if x.startswith("move_me")])
        print(f"目标文件内容：{open(destination_file, 'r', encoding='utf-8').read()}")

        # 检查源目录是否为空
        if not os.listdir(from_dir):
            print("源目录已为空")

    except Exception as e:
        print(f"移动过程中出现错误：{e}")
    finally:
        # 可选：清理临时目录
        # cleanup_temp_dirs([from_dir])
        pass

def cleanup_temp_dirs(directories):
    """
    清理临时目录
    """
    for directory in directories:
        if os.path.exists(directory):
            shutil.rmtree(directory)
            print(f"已删除临时目录：{directory}")

if __name__ == "__main__":
    move_file_example()
