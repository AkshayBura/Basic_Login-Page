from typing import List
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
import schemas, database, crud
from sqlalchemy.orm import Session


router = APIRouter(
    prefix='/user',
    tags=['User']
)

@router.post('/display')
def display(user: schemas.Login):
    return f"I am {user.username} "

@router.get('/',response_model=List[schemas.User])
def all_users(db: Session = Depends(database.get_db)):
    return crud.get_users(db=db)


@router.post("/add", response_model=schemas.UserCreate)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@router.get("/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(database.get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post('/uploadfile')
def upload_file(user : schemas.UserCreate = Depends(), db : Session = Depends(database.get_db), file: UploadFile = File(...)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    crud.create_user(db=db, user=user)
    file_path = f'D:/FastAPI_CRUD/testing/{file.filename}'
    with open(file_path,'wb') as obj:
        obj.write(file.file.read())
    return {"Info": f"File '{file.filename}' saved at '{file_path}'", "info2": f'{user} created'}

