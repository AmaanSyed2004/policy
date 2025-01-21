from fastapi import APIRouter, Depends, HTTPException, Response
import bcrypt
import jwt
import os
from api.database import get_db
from api.models.users import User
from api.schemas import UserRegisterInput, UserLoginInput
router = APIRouter()

@router.post("/register")
def register(user: UserRegisterInput,  db=Depends(get_db)):
    # to do: user registration: check if email exists, hash the pw, save to db
    existingEmail= db.query(User).filter(User.Email==user.Email).first()
    if existingEmail:
        raise HTTPException(status_code=400, detail="Email already in use!")
    
    salt= bcrypt.gensalt()
    hashed_pw= bcrypt.hashpw(user.Password.encode('utf-8'), salt).decode('utf-8')
    new_user= User(Name=user.Name, Email=user.Email, Password=hashed_pw, UserType=user.UserType)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User registered successfully", "UserID": str(new_user.UserID)}

@router.post("/login")
def login(user:UserLoginInput, response: Response, db= Depends(get_db)):
    existingUser= db.query(User).filter(User.Email==user.Email).first()
    if not existingUser:
        raise HTTPException(status_code=400, detail="Email does not exist, please register!")
    print(f"Stored password hash: {existingUser.Password} (Type: {type(existingUser.Password)})")

    if not bcrypt.checkpw(user.Password.encode('utf-8'), existingUser.Password.encode('utf-8')):
        raise HTTPException(status_code=403, detail="Invalid password! Please try again!")
    #user is now verified, send an http only cookie to the client with the jwt
    token = jwt.encode({"UserID": str(existingUser.UserID)}, os.getenv("JWT_SECRET"), algorithm="HS256")
    response.set_cookie(key="access_token", value=token, httponly=True, samesite='strict', secure=True, max_age=3600) 
    return {"message": "User logged in successfully!"}