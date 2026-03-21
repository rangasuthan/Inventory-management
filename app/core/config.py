from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    app_name:str
    debug:bool
    db_host:str="localhost"
    db_port:int=3306
    db_user:str
    db_password:str
    db_name:str
    log_level:str

    @property
    def database_url(self)->str:
       return( f"mysql+pymysql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}")
    
    model_config = SettingsConfigDict(env_file="C:/inventory_management/app/.env")

settings=Settings()