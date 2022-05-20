from src.core import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine_args = {"url": settings.DATABASE_URL}

if "sqlite" in engine_args["url"]:
    engine_args["connect_args"] = {"check_same_thread": False}
elif "postgres" in engine_args["url"]:
    engine_args["url"] = engine_args["url"].replace("postgres://", "postgresql://")


engine = create_engine(**engine_args)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
