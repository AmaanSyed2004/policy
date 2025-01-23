from fastapi import APIRouter, HTTPException, Depends
import uuid
from sqlalchemy.orm import Session

from api.schemas import PolicyInput, PolicyPutInput, PoliciesResponse, PolicyResponse
from api.database import get_db
from api.models.policies import PolicyDB
from api.kafka.producer import produce_event
from api.middleware.authMiddleware import authenticateJWT, authenticateAdmin
router = APIRouter()



# get all policies

@router.get("/policies",  response_model= PoliciesResponse)
def get_all_policies(db:Session=Depends(get_db), current_user:dict= Depends(authenticateJWT))->PoliciesResponse:
    role = current_user.get('role')
    UserID = current_user.get('UserID')
    if not role or not UserID:
        raise HTTPException(status_code=401, detail="Invalid token") #extra check, even though it should never be reached due to the middleware
    if role == 'admin':
        print('role is admin, returning all the policies in the db')
        policies =  db.query(PolicyDB).all()
        return {"policies":policies}
    elif role == 'user':
        print('role is user, returning all the policies for the user')
        policies = db.query(PolicyDB).filter(PolicyDB.UserID ==UserID).all()
        return {"policies":policies}
    
    raise HTTPException(status_code=403, detail="You are not authorized to access this route")

#get a policy by it's id

@router.get("/policies/{policy_id}", response_model=PolicyResponse)
def get_specific_policy(policy_id:uuid.UUID, db:Session=  Depends(get_db), current_user:dict= Depends(authenticateJWT)):
    policy= db.query(PolicyDB).filter(PolicyDB.PolicyID == policy_id).first()
    #print policy in a readable format
    if policy is None:
        raise HTTPException(status_code=404, detail=f"Policy with id {policy_id} not found.")
    if current_user.get('role') == 'admin':
        return policy
    else:
        print(policy.UserID)
        print(current_user.get('UserID'))
        if str(policy.UserID) != str(current_user.get('UserID')):
            raise HTTPException(status_code=403, detail="This policy does not belong to you!")
        return policy

#post a new policy

@router.post("/policies")
def add_policy(policy: PolicyInput, db:Session= Depends(get_db), current_user:dict= Depends(authenticateJWT)):
    new_policy = PolicyDB(**policy.model_dump())
    new_policy.UserID= current_user.get('UserID')
    db.add(new_policy)
    db.commit()
    db.refresh(new_policy)

    event= new_policy.serialize()
    produce_event("policy-created", event)
    return {"message": "Policy added successfully", "policy_id": new_policy.PolicyID}

#Update an existing policy

@router.put("/policies/{policy_id}")
def change_existing_policy(policy_id: uuid.UUID, policy: PolicyPutInput, db:Session= Depends(get_db), current_user:dict= Depends(authenticateJWT)):
    policy_to_change = db.query(PolicyDB).filter(PolicyDB.PolicyID == policy_id).first()
    if policy_to_change is None:
        raise HTTPException(status_code=404, detail=f"Policy with id {policy_id} not found.")
    if current_user.get('role') == 'user' and str(policy_to_change.UserID) != str(current_user.get('UserID')):
        raise HTTPException(status_code=403, detail="This policy does not belong to you!")
    
    for key, value in policy.model_dump(exclude_unset=True).items():
        setattr(policy_to_change, key, value)
    db.commit()
    db.refresh(policy_to_change)

    event= policy_to_change.serialize()
    produce_event("policy-updated", event)
    return {"message": "Policy updated successfully"}

#delete a policy by it's id
@router.delete("/policies/{policy_id}")
def delete_policy(policy_id: uuid.UUID, admin: dict = Depends(authenticateAdmin), db: Session = Depends(get_db)):
    policy_to_delete= db.query(PolicyDB).filter(PolicyDB.PolicyID == policy_id).first()
    if policy_to_delete is None:
        raise HTTPException(status_code=404, detail=f"Policy with id {policy_id} not found.")
    db.delete(policy_to_delete)
    db.commit()
    event= policy_to_delete.serialize()
    produce_event("policy-deleted", event)
    return {"message": "Policy deleted successfully"}
