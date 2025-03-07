from fastapi import FastAPI

from api import retrieve, setup, upload

app = FastAPI(
    title="Vector Store API",
    version="0.1.0"
)

app.include_router(retrieve.router)
app.include_router(setup.router)
app.include_router(upload.router)


@app.get("/")
async def root():
    return "Hello, World..!"
