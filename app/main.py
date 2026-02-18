from fastapi import FastAPI
from app.database import Base, engine
from app.routes import user

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Hello world route
@app.get("/")
def hello():
    return {"message": "FastAPI Hello World 🚀"}

# Include routes
app.include_router(user.router)