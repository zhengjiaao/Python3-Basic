# main.py
from fastapi import FastAPI, Depends
from app.config_manager import ConfigManager

app = FastAPI(
    title="Your API Title",
    description="Your API Description",
    version="0.1.0",
)

# config_manager = ConfigManager()

async def get_config_manager() -> ConfigManager:
    return ConfigManager()

async def startup_event():
    # 在应用启动时加载配置
    config_manager = await get_config_manager()
    config = config_manager.get_config()
    print("Initial config:", config)


async def shutdown_event():
    # 在应用关闭时执行清理操作（如果有）
    print("Application is shutting down")


app.add_event_handler("startup", startup_event)
app.add_event_handler("shutdown", shutdown_event)


@app.get("/config")
async def get_config(config_manager: ConfigManager = Depends()):
    return config_manager.get_config()


# 启动项目，或使用命令行方式：uvicorn main:apps --reload
# 访问项目-前端：http://127.0.0.1:8000/config
# 访问项目-api：http://127.0.0.1:8000/docs
if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app='main:app', host="0.0.0.0", port=8000, reload=False, workers=1)
