from fastapi import FastAPI, HTTPException, Depends
from app import crud
from pydantic import BaseModel

# app = FastAPI()

app = FastAPI(
    title="Your API Title",
    description="Your API Description",
    version="0.1.0",
    swagger_ui_parameters={
        "defaultModelsExpandDepth": 1,  # 默认不展开 Schemas
        "docExpansion": "none"  # 默认不展开路由
    }
)


class KeyVal(BaseModel):
    key: str
    value: str


@app.post("/redis/set_key")
def set_key(key_val: KeyVal):
    print(key_val.key, key_val.value)
    crud.set_key(key_val.key, key_val.value)
    return {"key": key_val.key, "value": key_val.value}


@app.get("/redis/get_key")
def get_key(key: str):
    print(key)
    return crud.get_key(key)


@app.put("/redis/update_key")
def update_key(key_val: KeyVal):
    print(key_val.key, key_val.value)
    crud.update_key(key_val.key, key_val.value)
    return {"key": key_val.key, "value": key_val.value}


@app.delete("/redis/delete_key")
def delete_key(key: str):
    print(key)
    crud.delete_key(key)
    # return {"key": key} # 默认返回 null


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app='main:app', host="0.0.0.0", port=8000, reload=False, workers=1)
