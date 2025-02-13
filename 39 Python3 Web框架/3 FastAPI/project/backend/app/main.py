# example-vue-frontend/apps/main.py
from fastapi import FastAPI
from . import models, database
from .routers import users, files

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(
    title="Your API Title",
    description="Your API Description",
    version="0.1.0",
    swagger_ui_parameters={
        "defaultModelsExpandDepth": 1,  # 默认不展开 Schemas
        "docExpansion": "none"  # 默认不展开路由
    }
)

# 包含 users.py 中的路由
app.include_router(users.router, prefix="/api", tags=["users"])
app.include_router(files.router, prefix="/api", tags=["files"])
# apps.include_router(users.router)
# apps.include_router(files.router)


# Mount the vue-frontend static files
# apps.mount("/static", StaticFiles(directory="example-vue-frontend/vue-frontend/dist"), name="static")


# Serve the vue-frontend index.html for all other routes
# @apps.get("/{full_path:path}", response_class=HTMLResponse)
# async def read_index(request: Request, full_path: str):
#     with open("example-vue-frontend/vue-frontend/dist/index.html") as f:
#         return HTMLResponse(content=f.read())


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app='main:app', host="0.0.0.0", port=8000, reload=False, workers=1)
