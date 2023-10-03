from sqlalchemy.orm import Session
from routers.hashing import Hash
import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    hashedpass = Hash.bcrpt(password = user.password)
    db_user = models.User(name = user.name, email = user.email, password = hashedpass)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_blog(db: Session, blog: schemas.BlogBase):
    db_blog = models.Blog(title = blog.title, description = blog.description, user_id = blog.user_id)
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog


def get_blogs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Blog).offset(skip).limit(limit).all()


def get_blog(db: Session, blog_id: int):
    return db.query(models.Blog).filter(models.Blog.id == blog_id).first()


def get_blog_by_title(db: Session, title: str):
    return db.query(models.Blog).filter(models.Blog.title == title).first()


def auth(db: Session, request: schemas.Login):
    return db.query(models.User).filter(models.User.email == request.username).first()