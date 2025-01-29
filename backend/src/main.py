from fastapi import FastAPI
from CMC_router import router as router_crypto
from login_router import router as login_crypto
from fastapi.middleware.cors import CORSMiddleware
from logger import logger

app = FastAPI()
logger.info("Starting server")

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:5174",
    "http://127.0.0.1:5174",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router_crypto)
app.include_router(login_crypto)