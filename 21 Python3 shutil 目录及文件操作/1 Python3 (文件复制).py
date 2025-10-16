import shutil
import os


def copy_file_example():
    """
    演示使用 shutil.copy 进行文件复制
    """
    try:
        # 创建临时目录
        os.makedirs("tmp", exist_ok=True)

        # 创建源文件
        source_file = "tmp/hello.txt"
        with open(source_file, "w", encoding="utf-8") as f:
            f.write("hello shutil 你好呀！")

        # 复制文件
        destination_file = "tmp/hello_copy.txt"
        dst = shutil.copy(source_file, destination_file)

        # 验证复制结果
        if os.path.exists(destination_file):
            print("复制成功：", dst)
            print(f"源文件内容：{open(source_file, 'r', encoding='utf-8').read()}")
            print(f"目标文件内容：{open(destination_file, 'r', encoding='utf-8').read()}")
        else:
            print("复制失败")

    except Exception as e:
        print(f"复制过程中出现错误：{e}")
    finally:
        # 可选：清理临时文件
        # cleanup_temp_files(["tmp/hello.txt", "tmp/hello_copy.txt"])
        pass


def cleanup_temp_files(files):
    """
    清理临时文件
    """
    for file in files:
        if os.path.exists(file):
            os.remove(file)
            print(f"已删除临时文件：{file}")


if __name__ == "__main__":
    copy_file_example()
