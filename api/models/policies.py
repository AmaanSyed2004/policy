from sqlalchemy import Column, String, Enum, Date, Integer, UUID, ForeignKey
from sqlalchemy.orm import relationship
from api.database import Base
import uuid

from api.models.enums import PolicyType, PolicyStatus

class PolicyDB(Base):
    __tablename__= 'policies'

    UserID= Column(UUID(as_uuid=True), ForeignKey('users.UserID'), primary_key=True)
    PolicyID= Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4) 
    PolicyHolderName= Column(String, nullable=False)
    PolicyType= Column(Enum(PolicyType), nullable=False)
    PolicyStartDate= Column(Date, nullable=False)
    PolicyEndDate= Column(Date, nullable=False)
    PremiumAmount= Column(Integer, nullable=False)
    Status= Column(Enum(PolicyStatus), nullable=False)
    
    user = relationship("User", back_populates="policies")
    def serialize(self):
        return {
            "PolicyID": str(self.PolicyID),
            "PolicyHolderName": self.PolicyHolderName,
            "PolicyType": self.PolicyType.value,
            "PolicyStartDate": self.PolicyStartDate.isoformat(),
            "PolicyEndDate": self.PolicyEndDate.isoformat(),
            "PremiumAmount": self.PremiumAmount,
            "Status": self.Status.value,
            "UserID": str(self.UserID)
        }
