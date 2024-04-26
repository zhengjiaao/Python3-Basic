import unittest
import uuid
import shortuuid
from hashids import Hashids


class MyTestCase(unittest.TestCase):

    # shortuuid 是一个第三方库，用于生成短的、可读性好的唯一 ID。它基于 UUID 实现，但生成的 ID 更短、更易读。
    def test_1(self):
        # 生成短的、可读性好的唯一 ID
        id = shortuuid.uuid()
        # 生成短的、可读性好的唯一 ID
        print(id)  # 9xMPjNKAnwRjJNghhmoc9G

        # 生成短的、可读性好的纯数字 ID
        id = shortuuid.uuid(name="your_namespace")

        print(id)  # your_namespace=R9z7K6wAHXgGeM3V75XJ28

    # Python 标准库中的 uuid 模块提供了生成 UUID（通用唯一标识符）的功能。UUID 是由 32 个十六进制数字组成的 128 位数值，具有非常低的重复概率。
    def test_2(self):
        # 生成一个随机的 UUID
        id = uuid.uuid4()

        print(id)  # 6514c4b9-75f1-4759-9e66-12b5ab7bb4e9

    # hashids 是一个第三方库，用于生成短的、可逆的、不重复的 ID。你可以自定义加密和解密的算法。
    def test_3(self):
        # 创建 Hashids 对象
        hashids = Hashids()

        # 加密整数 ID
        # id = hashids.encode(123)
        id = hashids.encode(88888888)

        print(id)  # 123=Mj3、88888888=gE0PoY
