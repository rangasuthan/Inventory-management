from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.services.service import InventoryService
from app.models.model import ItemCreate,ItemResponse

router = APIRouter(prefix="/items", tags=["Items"])

@router.post("/",response_model=ItemResponse)
def add_item(item:ItemCreate,db:Session=Depends(get_db)):
    return InventoryService.create_items(db,item)

@router.get("/",response_model=list[ItemResponse])
def get_itemall(db:Session=Depends(get_db)):
    return InventoryService.get_items_all(db)

@router.get("/name",response_model=ItemResponse)
def get_itemall(name:str,db:Session=Depends(get_db)):
    return InventoryService.get_items_name(db,name)

@router.get("/total")
def get_total(db:Session=Depends(get_db)):
    return {"total_stock_value": InventoryService.get_items_totalvalue(db)}

@router.get("/low",response_model=list[ItemResponse])
def get_low(threshold:int=3,db:Session=Depends(get_db)):
    return InventoryService.get_items_lowstock(db,threshold)

@router.delete("/")
def remove_item(item_id:int,db:Session=Depends(get_db)):
    return InventoryService.delete_items(db,item_id)