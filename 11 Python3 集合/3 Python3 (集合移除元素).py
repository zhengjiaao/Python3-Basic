thisset = set(("Google", "Runoob", "Taobao"))
thisset.remove("Taobao")
print(thisset)

# 随机删除元素
x = thisset.pop()
print(x)

# 移除元素
thisset.discard("Facebook")  # 不存在，不会发生错误
thisset.remove("Facebook")  # 不存在，会发生异常 KeyError: 'Facebook'
