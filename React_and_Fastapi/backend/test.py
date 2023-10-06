from fastapi import FastAPI
import uvicorn
import routers.blog as blog, routers.user as user, routers.authentication as login
import models
from database import engine
from fastapi.middleware.cors import CORSMiddleware


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:5000",
    # "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(login.router)
app.include_router(blog.router)
app.include_router(user.router)

if __name__ == "__main__":
    uvicorn.run('test:app', host='127.0.0.1', port=5000, reload=True)