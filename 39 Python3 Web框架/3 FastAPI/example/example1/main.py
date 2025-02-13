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

# 或执行命令启动：uvicorn main:apps --reload
if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app='main:app', host="0.0.0.0", port=8000, reload=False, workers=1)