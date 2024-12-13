from fastapi import FastAPI
from .routes.policy_routes import router as policy_router

app = FastAPI()

app.include_router(policy_router)