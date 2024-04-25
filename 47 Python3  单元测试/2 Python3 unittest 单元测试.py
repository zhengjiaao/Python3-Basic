import unittest


# 单元测试 ，测试类中可以创建多个单元测试方法
class MyTestCase(unittest.TestCase):

    def test_method1(self):
        # 测试方法1的代码和断言
        print("test_method1")
        pass

    def test_method2(self):
        # 测试方法2的代码和断言
        print("test_method2")
        pass

    def test_method3(self):
        # 测试方法3的代码和断言
        print("test_method3")
        pass


if __name__ == '__main__':
    unittest.main()
