from sqlalchemy import Column, String, Enum, Date, Integer, UUID
from sqlalchemy.ext.declarative import declarative_base
import uuid

from api.enums import PolicyType, PolicyStatus
Base= declarative_base()

class PolicyDB(Base):
    __tablename__= 'policies'

    PolicyID= Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4) 
    PolicyHolderName= Column(String, nullable=False)
    PolicyType= Column(Enum(PolicyType), nullable=False)
    PolicyStartDate= Column(Date, nullable=False)
    PolicyEndDate= Column(Date, nullable=False)
    PremiumAmount= Column(Integer, nullable=False)
    Status= Column(Enum(PolicyStatus), nullable=False)
    
