# FastAPI web框架

FastAPI 是一个现代的、快速（高性能）的Web框架，用于构建API。以下是它的优缺点：

## 优点

* 高性能：
    * FastAPI 基于 Starlette 核心和 Pydantic 模型，性能非常出色，可以与 NodeJS 和 Go 相媲美。
* 自动交互式 API 文档：
    * 内置了两个自动生成的交互式 API 文档界面：Swagger UI 和 ReDoc。这使得开发者和用户可以轻松地测试和理解 API。
* 类型提示支持：
    * 完全支持 Python 的类型提示，这不仅提高了代码的可读性和可维护性，还能够在开发阶段捕获更多错误。
* 依赖注入系统：
    * 提供了一个强大的依赖注入系统，简化了复杂应用的构建，并且易于测试。
* 异步支持：
    * 强大的异步支持，允许使用 async 和 await，从而提高 I/O 密集型应用的性能。
* 数据验证和序列化：
    * 使用 Pydantic 进行数据验证和序列化，确保输入输出数据的一致性和正确性。
* 社区活跃：
    * FastAPI 拥有一个活跃的社区，提供了丰富的插件和扩展，能够满足各种需求。

## 缺点

* 相对较新：
    * 相比 Flask 或 Django 等老牌框架，FastAPI 出现的时间较短，因此在某些方面可能还不够成熟，文档和第三方库的支持也相对较少。
* 生态系统较小：
    * 尽管 FastAPI 社区增长迅速，但其生态系统仍然不及一些更成熟的框架如 Django 或 Flask 大。
* 学习曲线：
    * 对于不熟悉 Python 类型提示或异步编程的开发者来说，可能会有一定的学习成本。

总结来说，FastAPI 是一个非常适合构建现代高效 API 的框架，尤其适合那些追求高性能和开发效率的项目。如果你的应用需要处理大量并发请求或者你希望利用最新的
Python 特性，FastAPI 是一个非常好的选择。

## 安装FastAPI模块

```shell
pip install fastapi
pip install uvicorn
```

> uvicorn用于运行 Python 的异步 Web 应用程序，与许多流行的 Python 框架（如 FastAPI、Starlette 等）兼容，可以帮助开发者构建高效的异步
> Web 服务

### FastAPI入门体验

创建一个main.py

```python
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Project  :wangting_FastAPI
# @File     :main.py.py
# @Author   :wangting_666

from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

```

async 关键字用于定义异步函数。异步函数可以在执行过程中暂停并允许其他代码执行，直到某些条件满足后再恢复执行。
在 FastAPI 中，使用 async 可以使函数能够处理异步操作，例如异步的数据库查询、IO 操作等，以提高性能和并发能力。
在这个例子中，read_root 和 read_item 函数都是异步函数，它们使用了 async 关键字来定义。
这样的函数可以通过 await 关键字调用其他异步函数，或者执行需要等待的异步操作，而不会阻塞整个应用程序的执行。

运行程序

在 PyCharm 的 Terminal 中运行 uvicorn 命令启动 FastAPI 应用程序

```shell
uvicorn main:app --reload

```

这里的 main 是你的 Python 文件名（不含扩展名main方法的意思），app 是你创建的 FastAPI 应用程序实例。

uvicorn main:app --reload 命令含义如下:

* main：main.py 文件（一个 Python “模块”）。
* app：在 main.py 文件中通过 app = FastAPI() 创建的对象。
* --reload：让服务器在更新代码后重新启动。仅在开发时使用该选项。

### 访问 API文档界面

* API文档界面： http://127.0.0.1:8000/docs

测试：

* http://localhost:8000/
* http://localhost:8000/items/1