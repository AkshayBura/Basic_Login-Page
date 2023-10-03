from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
import schemas, database, crud
from sqlalchemy.orm import Session
from routers.hashing import Hash
from JWTtoken import create_access_token

router = APIRouter(
    tags=['Authentication']
)

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = crud.auth(db, request)
    if not user:
        raise HTTPException(status_code=404, detail='Invalid Credentials or User not found')
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=404, detail='Incorrect Password')
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}