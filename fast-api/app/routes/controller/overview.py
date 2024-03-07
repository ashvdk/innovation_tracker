from fastapi import APIRouter, Request, Depends
from database import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from routes.provider.overview import get_products_overview
route = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@route.post('/overview/products')
def get_product_overview(req: Request, db: Annotated[Session, Depends(get_db)]):
    return get_products_overview(db=db)
