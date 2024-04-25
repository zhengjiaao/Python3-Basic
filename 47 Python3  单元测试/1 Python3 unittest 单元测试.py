import unittest


# 在测试类中，我们可以定义多个测试方法，每个测试方法都应以 test_ 开头，并在方法中编写要测试的代码和断言。
# setUp() 和 tearDown() 方法分别在每个测试方法之前和之后执行，用于设置前置条件和清理测试环境。

# 通过 unittest.main() 方法运行测试。这将自动发现并执行测试类中的所有测试方法，并提供测试结果的输出。

# 当测试中的断言失败时，会引发 AssertionError 异常。
# unittest.TestCase 类提供了许多其他的断言方法，如 assertEqual()、assertNotEqual()、assertTrue()、assertFalse() 等，用于验证测试结果。

# 创建测试类
class MyTestCase(unittest.TestCase):

    # 在每个测试方法之前执行的操作
    def setUp(self):
        # 设置测试的前置条件
        self.my_data = [1, 2, 3, 4, 5]

    # 编写测试方法
    def test_sum(self):
        print("test_sum")
        # 执行被测试的代码
        result = sum(self.my_data)
        # 使用断言进行验证
        self.assertEqual(result, 15)

    def test_max(self):
        print("test_max")
        result = max(self.my_data)
        self.assertEqual(result, 5)

    # 在每个测试方法之后执行的操作
    def tearDown(self):
        # 清理测试的环境
        pass


# 运行测试
if __name__ == '__main__':
    unittest.main()
