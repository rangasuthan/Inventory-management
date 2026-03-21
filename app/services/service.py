from sqlalchemy.orm import Session
from app.repo.repository import InventoryRepository
from app.schema.schema import Inventory
from app.core.logger import logger
class InventoryService:

    @staticmethod
    def create_items(db:Session,items:Inventory):
        logger.info("creating item: "+items.name)
        return InventoryRepository.create(db,items)
    
    @staticmethod
    def get_items_all(db:Session):
        return InventoryRepository.get_all(db)
    
    @staticmethod
    def get_items_name(db:Session,name:str):
        return InventoryRepository.get_by_name(db,name)
    
    @staticmethod
    def get_items_totalvalue(db:Session):
        return InventoryRepository.get_total_stockvalue(db)
    
    @staticmethod
    def get_items_lowstock(db:Session,threshold:int):
        return InventoryRepository.get_low_stockitem(db,threshold)
    
    @staticmethod
    def delete_items(db:Session,item_id:int):
        result=InventoryRepository.delete(db,item_id)
        if result:
            logger.info("Item deleted successfully")
        else:
            logger.warning("Item id not exsist")
        return result
    