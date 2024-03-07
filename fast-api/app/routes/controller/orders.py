from fastapi import APIRouter, FastAPI, HTTPException, Request, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models.Sales import Sales
from routes.provider.orders import get_details, createNewOrder, getOrdersFromProvider
from typing import Annotated

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/orders")
async def orders(request: Request, db: Annotated[Session, Depends(get_db)]):
    request_body = await request.json()
    get_orders = getOrdersFromProvider(request_body, db=db)
    return {
        "data": get_orders
    }
    # try:
    #     db = SessionLocal()
    #     sales_data = db.query(Sales).limit(100).all()
    #     db.close()
    #     sales_json = [{"product": sale.product, "quantity_ordered": sale.quantity_ordered} for sale in sales_data]
    #     return {
    #         "data": sales_data
    #     }
    # except Exception as e:
    #     raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/orders/create")
async def createOrder(request: Request, db: Annotated[Session, Depends(get_db)]):
    try:
        db = SessionLocal()
        request_body = await request.json()
        create_order = createNewOrder(request_body, db = db)
        return create_order
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@router.get("/orders/create/details")
async def createOrderDetails():
    details = get_details()
    return {
        "data": details
    }
# from fastapi import APIRouter, FastAPI, HTTPException
# from database import SessionLocal
# from models.Sales import Sales
# router = APIRouter()

# @router.post("/orders")
# async def orders():
#     try:
#         db = SessionLocal()
#         sales_data = db.query(Sales).limit(10).all()
#         db.close()
#         sales_json = [{"product": sale.product, "quantity_ordered": sale.quantity_ordered} for sale in sales_data]
#         return {
#             "data": sales_json
#         }
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
    