from sqlalchemy.orm import Session
from app.schema.schema import Inventory

class InventoryRepository:


    @staticmethod
    def create(db:Session,items:Inventory):
        db_item = Inventory(name=items.name, price=items.price,quantity=items.quantity)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    
    @staticmethod
    def get_all(db:Session):
        return db.query(Inventory).all()
    
    @staticmethod
    def get_by_name(db:Session,name:str):
        return db.query(Inventory).filter(Inventory.name==name).first()
    
    @staticmethod
    def get_total_stockvalue(db:Session):
        items=db.query(Inventory).all()
        total=0
        for i in items:
            total+=(i.price*i.quantity)
        return total
    
    @staticmethod
    def get_low_stockitem(db:Session,threshold:int):
        return db.query(Inventory).filter(Inventory.quantity<threshold).all()
    
    @staticmethod
    def update(db:Session,item_id:int,items:Inventory):
        update_item=db.query(Inventory).filter(Inventory.id==item_id).first()
        update_item.name=items.name
        update_item.price=items.price
        update_item.quantity=items.quantity
        db.commit()
        db.refresh(update_item)
        return update_item
        

    
    @staticmethod
    def delete(db:Session,item_id:int):
        item=db.query(Inventory).filter(Inventory.id==item_id).first()
        if item:
            db.delete(item)
            db.commit()
        return item
