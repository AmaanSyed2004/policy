from fastapi import FastAPI
from api.routes.policy_routes import router as policy_router
from api.database import Base, engine
from api.models import PolicyDB
from api.kafka.events import create_topics

Base.metadata.create_all(bind=engine)
app = FastAPI()
create_topics()
app.include_router(policy_router)