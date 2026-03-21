from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

engine=create_engine(settings.database_url,pool_pre_ping=True)

sessionlocal=sessionmaker(bind=engine,autoflush=False,autocommit=False)

Base=declarative_base()

def get_db():
    db=sessionlocal()
    try:
        yield db
    finally:
        db.close()