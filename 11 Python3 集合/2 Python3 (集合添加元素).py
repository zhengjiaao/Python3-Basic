thisset = set(("Google", "Runoob", "Taobao"))

# 添加一个元素
thisset.add("Facebook")
print(thisset)  # {'Facebook', 'Google', 'Runoob', 'Taobao'}

# 添加多个元素
thisset.update({1, 3})
print(thisset)  # {'Taobao', 1, 3, 'Facebook', 'Runoob', 'Google'}

