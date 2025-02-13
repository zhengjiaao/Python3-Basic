# main.py
from fastapi import FastAPI
import argparse

app = FastAPI()


def parse_arguments():
    parser = argparse.ArgumentParser(description="FastAPI Application")
    parser.add_argument("--database-url", type=str, required=True)
    parser.add_argument("--api-key", type=str, required=True)
    return parser.parse_args()


args = parse_arguments()


@app.get("/")
def read_root():
    return {"database_url": args.database_url, "api_key": args.api_key}

# 运行时传递参数：python main.py --database-url sqlite:///./test.db --api-key your_api_key_here
# 访问项目-前端：http://127.0.0.1:8000/
# 访问项目-api：http://127.0.0.1:8000/docs
if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app='main:app', host="0.0.0.0", port=8000, reload=False, workers=1)