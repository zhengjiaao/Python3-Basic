# config.py
class Config:
    database_url = "sqlite:///./test.db"
    api_key = "your_api_key_here"


class DevelopmentConfig(Config):
    debug = True


class ProductionConfig(Config):
    debug = False