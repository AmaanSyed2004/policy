from fastapi import APIRouter, HTTPException, Depends
import uuid
from sqlalchemy.orm import Session

from api.schemas import PolicyInput, PolicyPutInput, PoliciesResponse, PolicyResponse
from api.database import get_db
from api.models import PolicyDB
router = APIRouter()



# get all policies

@router.get("/policies",  response_model= PoliciesResponse)
def get_all_policies(db:Session=Depends(get_db))->PoliciesResponse:
    policies =  db.query(PolicyDB).all()
    return {"policies":policies}

#get a policy by it's id

@router.get("/policies/{policy_id}", response_model=PolicyResponse)
def get_specific_policy(policy_id:uuid.UUID, db:Session=  Depends(get_db)):
    policy= db.query(PolicyDB).filter(PolicyDB.PolicyID == policy_id).first()
    if policy is None:
        raise HTTPException(status_code=404, detail=f"Policy with id {policy_id} not found.")
    return policy

#post a new policy

@router.post("/policies")
def add_policy(policy: PolicyInput, db:Session= Depends(get_db)):
    new_policy = PolicyDB(**policy.model_dump())
    db.add(new_policy)
    db.commit()
    db.refresh(new_policy)
    return {"message": "Policy added successfully", "policy_id": new_policy.PolicyID}

#Update an existing policy

@router.put("/policies/{policy_id}")
def change_existing_policy(policy_id: uuid.UUID, policy: PolicyPutInput, db:Session= Depends(get_db)):
    policy_to_change = db.query(PolicyDB).filter(PolicyDB.PolicyID == policy_id).first()
    if policy_to_change is None:
        raise HTTPException(status_code=404, detail=f"Policy with id {policy_id} not found.")
    for key, value in policy.model_dump(exclude_unset=True).items():
        setattr(policy_to_change, key, value)
    db.commit()
    db.refresh(policy_to_change)
    return {"message": "Policy updated successfully"}

#delete a policy by it's id
@router.delete("/policies/{policy_id}")
def delete_policy(policy_id: uuid.UUID, db:Session= Depends(get_db)):
    policy_to_delete= db.query(PolicyDB).filter(PolicyDB.PolicyID == policy_id).first()
    if policy_to_delete is None:
        raise HTTPException(status_code=404, detail=f"Policy with id {policy_id} not found.")
    db.delete(policy_to_delete)
    db.commit()
    return {"message": "Policy deleted successfully"}
