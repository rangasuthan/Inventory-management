from sqlalchemy import Column,Integer,Float,String
from app.database.database import Base

class Inventory(Base):
    __tablename__="items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)

    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False, default=0)