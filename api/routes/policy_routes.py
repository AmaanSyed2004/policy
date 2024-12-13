from fastapi import APIRouter, HTTPException
import uuid
from api.models import Policy
from api.schemas import PolicyInput, PolicyPutInput, PoliciesResponse
from api.database import policies
router = APIRouter()



# get all policies

@router.get("/policies", response_model= PoliciesResponse)
def get_all_policies()->PoliciesResponse:
    return {"policies": policies}

#get a policy by it's id

@router.get("/policies/{policy_id}", response_model=Policy)
def get_specific_policy(policy_id:uuid.UUID):
    for policy in policies:
        if policy.PolicyID == policy_id:
            return policy
    raise HTTPException(status_code=404, detail=f"Policy with id {policy_id} not found")

#post a new policy

@router.post("/policies")
def add_policy(policy: PolicyInput):
    new_policy= Policy(
        PolicyID= uuid.uuid1(),
        **policy.model_dump()
    )
    policies.append(new_policy)
    return {"message": "Policy added successfully"}

#Update an existing policy

@router.put("/policies/{policy_id}")
def change_existing_policy(policy_id: uuid.UUID, policy: PolicyPutInput):
    for idx, existing_policy in enumerate(policies):
        if existing_policy.PolicyID == policy_id:
            updated_data = policy.dict(exclude_unset=True)
            
            updated_policy = existing_policy.copy(update=updated_data)
            
            policies[idx] = updated_policy
            return {"message": "Policy updated successfully"}
    
    raise HTTPException(status_code=404, detail=f"Policy with id {policy_id} not found.")


#delete a policy by it's id
@router.delete("/policies/{policy_id}")
def delete_policy(policy_id: uuid.UUID):
    for policy in policies:
        if policy.PolicyID == policy_id:
            policies.remove(policy)
            return {"message": "Item successfully deleted"}
    raise HTTPException(status_code=404, detail=f"Policy with id {policy_id} not found.")
