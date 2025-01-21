from datetime import date
from typing import Optional
from pydantic import BaseModel, ConfigDict
from uuid import UUID

from api.models.enums import PolicyStatus, PolicyType, UserType

class PolicyInput(BaseModel):
    PolicyHolderName: str
    PolicyType: PolicyType
    PolicyStartDate: date
    PolicyEndDate: date
    PremiumAmount: int
    Status: PolicyStatus

class PolicyPutInput(BaseModel):
    PolicyHolderName: Optional[str] = None
    PolicyType: Optional[PolicyType] = None #type: ignore
    PolicyStartDate: Optional[date] = None
    PolicyEndDate: Optional[date] = None
    PremiumAmount: Optional[int] = None
    Status: Optional[PolicyStatus] = None

class PolicyResponse(BaseModel):
    PolicyID: UUID
    PolicyHolderName: str
    PolicyType: PolicyType
    PolicyStartDate: date
    PolicyEndDate: date
    PremiumAmount: int
    Status: PolicyStatus
    
    model_config= ConfigDict(from_attributes=True)

    
class PoliciesResponse(BaseModel):
    policies: list[PolicyResponse]


class UserRegisterInput(BaseModel):
    Name: str
    Email: str
    Password: str
    UserType: UserType

class UserLoginInput(BaseModel):
    Email: str
    Password: str