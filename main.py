from fastapi import FastAPI
from api.routes.policy_routes import router as policy_router
from api.routes.user_routes import router as user_router
from api.database import Base, engine
from api.models.users import User
from api.models.policies import PolicyDB
from api.kafka.events import create_topics

Base.metadata.create_all(bind=engine)
app = FastAPI()
create_topics()
app.include_router(policy_router, tags=['policies'])
app.include_router(user_router, prefix='/auth', tags=['auth'])