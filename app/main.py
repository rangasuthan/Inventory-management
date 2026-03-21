from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
from app.core.config import settings
from app.utils.exceptions import InvalidStockException,ItemNotFoundException
from fastapi.exceptions import RequestValidationError
from app.database.database import Base, engine
from app.api.routes.route import router as item_route
from app.core.logger import logger

app=FastAPI(title=settings.app_name)

Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(item_route)


@app.exception_handler(ItemNotFoundException)
async def item_not_found_exception_handler(request: Request, exc: ItemNotFoundException):
    logger.error(f"ItemNotFoundException on {request.url.path}: {exc.message}")
    return JSONResponse(
        status_code=404,
        content={"success": False, "error": exc.message},
    )

@app.exception_handler(InvalidStockException)
async def invalid_stock_exception_handler(request: Request, exc: InvalidStockException):
    logger.error(f"InvalidStockException on {request.url.path}: {exc.message}")
    return JSONResponse(
        status_code=400,
        content={"success": False, "error": exc.message},
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.error(f"Validation error on {request.url.path}: {exc.errors()}")
    return JSONResponse(
        status_code=422,
        content={"success": False, "error": exc.errors()},
    )

@app.get("/")
def root():
    return {"message": "FastAPI CRUD App Running"}