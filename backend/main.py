from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api import retrieve, setup, upload

app = FastAPI(
    title="Vector Store API",
    version="0.1.0"
)

origins = [
    "https://localhost",
    "https://localhost:3000",
    "https://preview-dv.devant.dev"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

app.include_router(retrieve.router)
app.include_router(setup.router)
app.include_router(upload.router)


@app.get("/")
async def root():
    return "Hello, World..!"
