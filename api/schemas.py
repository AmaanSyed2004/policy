from datetime import date
from typing import Optional
from pydantic import BaseModel

from api.models import PolicyStatus
from api.models import PolicyType
from api.models import Policy

class PolicyInput(BaseModel):
    PolicyName: str
    PolicyType: PolicyType
    PolicyStartDate: date
    PolicyEndDate: date
    PremiumAmount: int
    Status: PolicyStatus

class PolicyPutInput(BaseModel):
    PolicyName: Optional[str] = None
    PolicyType: Optional[PolicyType] = None
    PolicyStartDate: Optional[date] = None
    PolicyEndDate: Optional[date] = None
    PremiumAmount: Optional[int] = None
    Status: Optional[PolicyStatus] = None

class PoliciesResponse(BaseModel):
    policies: list[Policy]