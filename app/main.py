from fastapi import FastAPI
from app.core.config import settings

from app.database.database import Base, engine
from app.api.routes.route import router as item_route

app=FastAPI(title=settings.app_name)

Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(item_route)

@app.get("/")
def root():
    return {"message": "FastAPI CRUD App Running"}