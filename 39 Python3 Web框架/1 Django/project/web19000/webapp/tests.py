from django.test import TestCase

# Create your tests here.

from django.test import TestCase


# 一个简单的测试用例可以如下所示：
class MyTestCase(TestCase):
    def test_something(self):
        # 测试代码
        self.assertEqual(1 + 1, 2)  # 断言测试结果
        print('单元测试运行完成.')

# 运行单元测试
# python manage.py test

# 运行特定单元测试方法
# python manage.py test myapp
