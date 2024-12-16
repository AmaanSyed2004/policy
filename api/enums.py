from enum import Enum

class PolicyType(str, Enum):
    Life = "Life"
    Health = "Health"
    Car = "Car"
    Home = "Home"

class PolicyStatus(str, Enum):
    active = "active"
    expired = "expired"
