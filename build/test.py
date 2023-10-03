from fastapi import FastAPI
import uvicorn
import routers.blog as blog, routers.user as user, routers.authentication as login
import models
from database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(login.router)
app.include_router(blog.router)
app.include_router(user.router)

if __name__ == "__main__":
    uvicorn.run('test:app', host='127.0.0.1', port=5000, reload=True)