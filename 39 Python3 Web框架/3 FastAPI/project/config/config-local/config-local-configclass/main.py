# main.py
from fastapi import FastAPI
from config import DevelopmentConfig

config = DevelopmentConfig()

app = FastAPI()


@app.get("/")
def read_root():
    return {"database_url": config.database_url, "api_key": config.api_key}


# 启动项目，或使用命令行方式：uvicorn main:apps --reload
# 访问项目-前端：http://127.0.0.1:8000/
# 访问项目-api：http://127.0.0.1:8000/docs
if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app='main:app', host="0.0.0.0", port=8000, reload=False, workers=1)