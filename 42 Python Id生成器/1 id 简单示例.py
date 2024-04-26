import unittest
import uuid
import time


class MyTestCase(unittest.TestCase):

    def test_1(self):
        # 生成一个随机的 UUID
        id = uuid.uuid4()

        print(id)  # 56605e31-1e9d-4bea-ac5a-e91084512852

    def test_2(self):
        # 生成基于时间戳的 ID
        id = int(time.time())

        print(id)  # 1714120404

    def test_3(self):
        # 使用计数器生成 ID：适用于在程序内部生成递增的 ID
        class IdGenerator:
            def __init__(self):
                self.counter = 0

            def generate_id(self):
                self.counter += 1
                return self.counter

        # 创建 ID 生成器对象
        generator = IdGenerator()

        # 生成 ID
        id = generator.generate_id()

        print(id)  # 1
