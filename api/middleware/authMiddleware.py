import jwt
from fastapi import HTTPException, Depends, Request
import os
def authenticateJWT(req: Request):
    token= req.cookies.get("access_token")

    if not token:
        raise HTTPException(status_code=400, detail="Token missing!")
    
    try:
        payload= jwt.decode(token,os.getenv("JWT_SECRET"), algorithms=['HS256'])
        UserID= payload.get('UserID')
        if UserID is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return {"UserID":UserID, "role":payload.get('role')}
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    

def authenticateAdmin(req: Request):
    token= req.cookies.get('access-token')

    if not token:
        raise HTTPException(status_code=400, detail="Token Missing!")
    try:
        payload= jwt.decode(token, os.getenv("JWT_SECRET"), algorithms=['HS256'])
        UserID= payload.get('UserID')
        if UserID is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        role= payload.get('role')
        if role is None:
            raise HTTPException(status_code=401, detail="Invalid token!")
        if role != 'admin':
            raise HTTPException(status_code=403, detail="Only admins are allowed to access this route")
        return UserID
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail= 'Invalid token!')