from datetime import date
import re
from typing import Optional
from pydantic import BaseModel, ConfigDict, EmailStr, field_validator
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
    Email: EmailStr  
    Password: str  
    UserType: UserType

    @field_validator('Password')
    def validate_password(cls, v):
        if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[\W_]).+$", v):
            raise ValueError("Password must contain at least one uppercase letter, one lowercase letter, one number, and one special character.")
        return v
class UserLoginInput(BaseModel):
    Email: EmailStr
    Password: str