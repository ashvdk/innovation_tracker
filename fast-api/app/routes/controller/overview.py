from fastapi import APIRouter, Request, Depends
from database import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from routes.provider.overview import get_products_overview, companyOverviewFilters
route = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@route.post('/overview/company')
def get_product_overview(req: Request, db: Annotated[Session, Depends(get_db)]):
    return get_products_overview(db=db)


@route.post('/overview/company/filters')
async def getCompanyOverviewFilters(req: Request, db: Annotated[Session, Depends(get_db)]):
    try:
        request_body = await req.json()
        print("reached 1")
        return companyOverviewFilters(db=db, body=request_body)
    except:
        print("error")
