import uuid
from api.models import Policy, PolicyStatus, PolicyType

# keeping a list as a mock databse
policies = [
    Policy(PolicyID="001b767e-b947-11ef-9ece-342eb7925977", PolicyName="Life Insurance", PolicyType=PolicyType.Life, PolicyStartDate="2021-01-01", PolicyEndDate="2025-01-01", PremiumAmount=10000, Status=PolicyStatus.active),
    Policy(PolicyID=uuid.uuid1(), PolicyName="Health Insurance", PolicyType=PolicyType.Health, PolicyStartDate="2021-01-01", PolicyEndDate="2025-01-01", PremiumAmount=20000, Status=PolicyStatus.active),
    Policy(PolicyID=uuid.uuid1(), PolicyName="Car Insurance", PolicyType=PolicyType.Car, PolicyStartDate="2021-01-01", PolicyEndDate="2024-03-01", PremiumAmount=30000, Status=PolicyStatus.expired),
    Policy(PolicyID=uuid.uuid1(), PolicyName="Home Insurance", PolicyType=PolicyType.Home, PolicyStartDate="2021-01-01", PolicyEndDate="2026-01-01", PremiumAmount=40000, Status=PolicyStatus.active),
]
