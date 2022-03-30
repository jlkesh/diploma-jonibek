from pydantic import BaseSettings


class Settings(BaseSettings):
    database_hostname: str = "localhost"
    database_port: str = '5432'
    database_password: str = '2001'
    database_name: str = 'diploma'
    database_username: str = 'postgres'
    secret_key: str = '!@#!@$#!@$!#%#$%^ERGET$%^&%$&%^GRFYH%^&^%@#$@#RDFGETDFHDFGASRF'
    algorithm: str = 'SHA256'
    access_token_expire_minutes: int = 12

    class Config:
        env_file = ".env"


settings = Settings()
