from sqlalchemy import Column, String, Enum, UUID
from sqlalchemy.orm import relationship
from api.database import Base
import uuid

from api.models.enums import UserType
class User(Base):
    __tablename__="users"
    
    UserID = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    Name = Column(String, nullable=False)
    Email = Column(String, nullable=False, unique=True)
    Password = Column(String, nullable=False)
    UserType = Column(Enum(UserType), nullable=False)

    policies= relationship("PolicyDB", back_populates="user", cascade="all, delete-orphan")
