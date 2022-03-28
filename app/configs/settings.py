
  
from pydantic import BaseSettings


class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str = '!@#!@$#!@$!#%#$%^ERGET$%^&%$&%^GRFYH%^&^%@#$@#RDFGETDFHDFGASRF'
    algorithm: str = 'SHA256'
    access_token_expire_minutes: int = 12

    class Config:
        env_file = ".env"


settings = Settings()