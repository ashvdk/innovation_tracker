from sqlalchemy.orm import Session
from models.Sales import Sales
import pandas as pd 
def getDashboardDetails(requestBody, db: Session = None):
    states = requestBody.get("states")
    cities = requestBody.get("cities")
    # print(requestBody.get("cities"))
    if len(states) == 0 and len(cities) == 0:
        tempOrderIds = db.query(Sales.order_id).distinct().all()
        all_records = db.query(Sales).all()
    else:
        tempOrderIds = db.query(Sales.order_id).filter(Sales.state.in_(states), Sales.city.in_(cities)).distinct().all()
        all_records = db.query(Sales).filter(Sales.state.in_(states), Sales.city.in_(cities)).all()
    df = pd.DataFrame([record.__dict__ for record in all_records])
    result = (df["quantity_ordered"] * df["price_each"]).sum()
    print(result)
    order_ids = [order_id[0] for order_id in tempOrderIds]
    print(len(order_ids))
    return {
        "data": {
            "no_of_orders": len(order_ids),
            "total_sales": result
        }
    }