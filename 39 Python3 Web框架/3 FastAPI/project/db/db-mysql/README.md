# FastAPI db-mysql

## 安装FastAPI模块

```shell
pip install -r requirements.txt
# or
pip install fastapi uvicorn pydantic pydantic[email] sqlalchemy databases python-multipart pymysql
```

MySQL 的依赖库 pymysql。

## 运行程序

在 PyCharm 的 Terminal 中运行 uvicorn 命令启动 FastAPI 应用程序

```shell
uvicorn main:app --reload
```

这里的 main 是你的 Python 文件名（不含扩展名main方法的意思），app 是你创建的 FastAPI 应用程序实例。

uvicorn main:app --reload 命令含义如下:

* main：main.py 文件（一个 Python “模块”）。
* app：在 main.py 文件中通过 app = FastAPI() 创建的对象。
* --reload：让服务器在更新代码后重新启动。仅在开发时使用该选项。

## 访问 API文档界面

* API文档界面： http://127.0.0.1:8000/docs

测试：

* http://localhost:8000/
* http://localhost:8000/items/1

## 停止运行

一般：

```shell
Ctrl + C
```

### Windows 命令行结束进程

有时候停止不了，采用以下命令：

列出所有与 Uvicorn 相关的进程：

```shell
  # PowerShell
  # 列出所有与 Uvicorn 相关的进程：
  Get-Process | Where-Object { $_.ProcessName -eq "python" } | Select-Object Id, ProcessName
  # 如果你看到多个 Python 进程，可以逐个终止它们：
  Stop-Process -Id <PID>
```

查看端口占用情况：

```shell
  # PowerShell
  netstat -ano | findstr :8000
  # 结束进程占用的端口：
  taskkill /F /PID <PID>
```