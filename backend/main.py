from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api import retrieve, setup, upload

app = FastAPI(
    title="Vector Store API",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"]
)

app.include_router(retrieve.router)
app.include_router(setup.router)
app.include_router(upload.router)


@app.get("/")
async def root():
    return "Hello, World..!"
