from datetime import date
from typing import Optional
from pydantic import BaseModel
from uuid import UUID

from api.enums import PolicyStatus
from api.enums import PolicyType

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

    class Config:
        orm_mode= True
class PoliciesResponse(BaseModel):
    policies: list[PolicyResponse]