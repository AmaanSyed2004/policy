from pydantic import BaseModel
from enum import Enum
import uuid
from datetime import date

class PolicyType(str, Enum):
    Life = "Life"
    Health = "Health"
    Car = "Car"
    Home = "Home"

class PolicyStatus(str, Enum):
    active = "active"
    expired = "expired"

class Policy(BaseModel):
    PolicyID: uuid.UUID
    PolicyName: str
    PolicyType: PolicyType
    PolicyStartDate: date
    PolicyEndDate: date
    PremiumAmount: int
    Status: PolicyStatus