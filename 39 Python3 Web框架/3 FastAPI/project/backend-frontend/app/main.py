# example-frontend/app/main.py
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from . import models, database
from .routers import users, files

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(files.router)

# Mount the frontend static files
app.mount("/static", StaticFiles(directory="example-frontend/frontend/dist"), name="static")

# Serve the frontend index.html for all other routes
@app.get("/{full_path:path}", response_class=HTMLResponse)
async def read_index(request: Request, full_path: str):
    with open("example-frontend/frontend/dist/index.html") as f:
        return HTMLResponse(content=f.read())
