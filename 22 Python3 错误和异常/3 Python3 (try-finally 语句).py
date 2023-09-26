# finally 语句无论异常是否发生都会执行

def hello():
    print("Hello World!")
    # x = 1 / 0 # 抛异常测试


try:
    hello()
except AssertionError as error:
    print(error)  # 发生异常时执行
else:  # 没有异常时执行的代码
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:  # 无论是否存在异常都会执行
    print('这句话，无论异常是否发生都会执行。')
