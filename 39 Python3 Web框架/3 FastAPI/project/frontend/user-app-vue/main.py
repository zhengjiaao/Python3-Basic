# example-vue-frontend/apps/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from apps.core import models, database
from apps.routers import users, files
from pathlib import Path

# 创建数据库表
models.Base.metadata.create_all(bind=database.engine)

BASE_DIR = Path(__file__).resolve().parent.parent
# data_root = BASE_DIR / 'data'

# if not data_root.exists():
#     data_root.mkdir(parents=True, exist_ok=True)

app = FastAPI(
    title="Your API Title",
    description="Your API Description",
    version="0.1.0",
    swagger_ui_parameters={
        "defaultModelsExpandDepth": 1,  # 默认不展开 Schemas
        "docExpansion": "none"  # 默认不展开路由
    }
)

# 添加 CORS 中间件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源，生产环境中建议指定具体的来源
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有 HTTP 方法
    allow_headers=["*"],  # 允许所有头部信息
)

# 包含 users.py 中的路由
app.include_router(users.users_api, prefix="/api", tags=["users"])
app.include_router(files.files_api, prefix="/api", tags=["files"])
# apps.include_router(users.router)
# apps.include_router(files.router)


# Mount the vue-frontend static files
# apps.mount("/static", StaticFiles(directory="example-vue-frontend/vue-frontend/dist"), name="static")

# Serve the vue-frontend index.html for all other routes
# @apps.get("/{full_path:path}", response_class=HTMLResponse)
# async def read_index(request: Request, full_path: str):
#     with open("example-vue-frontend/vue-frontend/dist/index.html") as f:
#         return HTMLResponse(content=f.read())

# 添加静态资源地址
app.mount('/assets', StaticFiles(directory=f'./themes/dist/assets'), name="assets")


# 添加首页页面
@app.get('/')
async def index():
    return HTMLResponse(
        content=open(BASE_DIR / f'./user-app-vue/themes/dist/index.html', 'r', encoding='utf-8').read()
        , media_type='text/html', headers={'Cache-Control': 'no-cache'})


# 启动项目，或使用命令行方式：uvicorn main:apps --reload
# 访问项目-前端：http://127.0.0.1:8000/
# 访问项目-api：http://127.0.0.1:8000/docs
if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app='main:app', host="0.0.0.0", port=8000, reload=False, workers=1)
