# 异常捕捉可以使用 try/except 语句

# 1.让用户输入一个合法的整数，但是允许用户中断这个程序.
# 用户中断的信息会引发一个 KeyboardInterrupt 异常.
while True:
    try:
        x = int(input("请输入一个数字: "))
        break
    except ValueError:
        print("您输入的不是数字，请再次尝试输入！")
