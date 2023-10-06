from typing import List
from fastapi import APIRouter, Depends, HTTPException
import schemas, database, crud, oauth2
from sqlalchemy.orm import Session


router = APIRouter(
    prefix='/blog',
    tags=['Blog']
)


@router.get("/", response_model=List[schemas.Blog])
def all_blogs(db: Session = Depends(database.get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    return crud.get_blogs(db=db)


@router.get("/{blog_id}", response_model=schemas.Blog)
def read_blog(blog_id: int, db: Session = Depends(database.get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    db_blog = crud.get_blog(db, blog_id=blog_id)
    if db_blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    return db_blog


@router.post("/add", response_model=schemas.BlogBase)
def create_blog(blog: schemas.BlogBase, db: Session = Depends(database.get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    db_blog = crud.get_blog_by_title(db, title=blog.title)
    if db_blog:
        raise HTTPException(status_code=400, detail=f"Blog with title {blog.title} already existed")
    return crud.create_blog(db=db, blog=blog)
