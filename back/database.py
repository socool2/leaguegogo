import json
from urllib.parse import quote

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


path = 'config.json'

with open(path) as f:
    config = json.load(f)

SQLALCHEMY_DATABASE_URL = "postgresql://{DB_USER}:%s@{DB_HOST}:{DB_PORT}/{DB_NAME}".format(
    DB_USER=config["POSTGRES"]["USER"],
    DB_HOST=config["POSTGRES"]["HOST"],
    DB_PORT=config["POSTGRES"]["PORT"],
    DB_NAME=config["POSTGRES"]["NAME"]) % quote(config["POSTGRES"]["PWD"])

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, pool_pre_ping=True,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
