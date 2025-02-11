from typing import Union
from fastapi import FastAPI

app = FastAPI()


# 访问API文档界面： http://127.0.0.1:8000/docs

@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
