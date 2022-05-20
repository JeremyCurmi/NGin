from typing import Generator
from sqlalchemy.orm import Session
from src.db.session import SessionLocal


def get_db() -> Generator:
    db: Session = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception as e:
        db.rollback()
    finally:
        db.close()