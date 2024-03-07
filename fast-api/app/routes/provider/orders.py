from fastapi import APIRouter, Depends, Request, HTTPException
from fastapi.responses import JSONResponse
from database import SessionLocal
from models.Filters import Filters
from models.Products import Products
from models.Sales import Sales
import pandas as pd
import uuid
from sqlalchemy.orm import Session

def format(body):
    objOrder = {}
    objOrder["id"] = body["id"]
    objOrder["city"] = body["city"]
    objOrder["price_each"] = body["price_each"]
    objOrder["product"] = body["product"]
    objOrder["quantity_ordered"] = body["quantity_ordered"]
    objOrder["key"] = body["id"]
    return objOrder

def getOrdersFromProvider(request_body, db: Session = None):
    states = request_body.get("states")
    cities = request_body.get("cities")
    producttype = request_body.get("productType")
    print(producttype)
    try:
        if producttype == "orders":
            if len(states) > 0 and len(cities) > 0:
                sales_data = db.query(Sales).filter(Sales.state.in_(states), Sales.city.in_(cities)).all()
            else:
                sales_data = db.query(Sales).all()
            all_order_ids = {}
            for order in sales_data:
                tempOrder = order.__dict__
                if tempOrder["order_id"] in all_order_ids:
                    orderDetails = all_order_ids[tempOrder["order_id"]]
                    count = orderDetails["no_of_products"]
                    count = count + 1
                    orderDetails["no_of_products"] = count
                    childrenArr = orderDetails["children"]
                    childrenArr.append(format(tempOrder))
                else:
                    all_order_ids[tempOrder["order_id"]] = {
                        "order_id": tempOrder["order_id"],
                        "no_of_products": 1,
                        "key": uuid.uuid4(),
                        "order_date": tempOrder["order_date"],
                        "purchase_address": tempOrder["purchase_address"],
                        "children": [format(tempOrder)]
                    }
            #print(all_order_ids)
            response_orders = []
            for keys in all_order_ids:
                response_orders.append(all_order_ids[keys])
            # df = pd.DataFrame([sales.__dict__ for sales in sales_data])
            # allOrdersIds = df["order_id"].unique().__dict__
            # print(allOrdersIds)
            return response_orders
        else:
            sales_data = db.query(Sales).all()
            df = pd.DataFrame([sales.__dict__ for sales in sales_data])
            df["total_sales"] = df["quantity_ordered"] * df["price_each"]
            df["order_date"] = pd.to_datetime(df["order_date"], format='%d/%m/%Y')
            result = df.groupby("product").agg(
                total_orders=('order_id', 'count'),
                quantities=('quantity_ordered', 'sum'),
                total_sales=('total_sales', 'sum'),
                min_month=('order_date', 'min'),
                max_month=('order_date', 'max')
            )
            
            # result.reset_index(inplace=True)
            #print(result)
            product_details = []
            for product in result.iterrows():
                print(product[0])
                print(product[1]["total_orders"])
                print(product[1]["quantities"])
                print(product[1]["total_sales"])
                print(product[1]["min_month"])
                print(product[1]["max_month"])
                print("-----")
                obj = {"product": product[0], "total_orders": int(product[1]["total_orders"]), "quantities": int(product[1]["quantities"]), "total_sales" : float(product[1]["total_sales"])}
                product_details.append(obj)
            return product_details
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def createNewOrder(order_details, db: Session = None):
    unique_id = uuid.uuid4()
    products = order_details.get("products")
    street = order_details.get("street")
    city = order_details.get("city")
    state = order_details.get("state")
    # try:
    for product in products:
        print(unique_id)
        print(product["product"])
        print(product["quantity_ordered"])
        print(product["price"])
        print(product["order_date"])
        print(street+", "+city+", "+state)
        print(city)
        print(state)
        print("345346")
        order = Sales( 
            order_id = unique_id,
            product = product["product"],
            quantity_ordered = product["quantity_ordered"],
            price_each = product["price"],
            order_date = str(product["order_date"]),
            purchase_address = street+", "+city+", "+state,
            city = city,
            state = state,
            zip_code = "34534"
        )
        db.add(order)
    db.commit()
    return {"message": f"{len(products)} sales records created successfully"}
    # except Exception as e:
    #     db.rollback()
    #     raise HTTPException(status_code=500, detail=str(e))
    


def get_details():
    try:
        db = SessionLocal()
        states = db.query(Filters.state).distinct().all()
        streets = db.query(Filters.address).distinct().limit(100).all()
        list_states = [state[0] for state in states]
        cities = db.query(Filters.city, Filters.state).filter(Filters.state.in_(list_states)).distinct().all()
        products = db.query(Products).all()
        db.close()
        list_street = [{ "label": street[0], "value": street[0] } for street in streets]
        def format_city(city):
            return {"label": city, "value": city}
        df = pd.DataFrame(cities, columns=['City', 'State'])
        cities_by_state = df.groupby('State')['City'].apply(lambda x: x.apply(format_city).tolist()).to_dict()
        # print([state[0] for state in states])
        # distinct_states = [{"label": state[0], "value": state[0]} for state in states]
        # distinct_cities = [{"label": city[0], "value": city[0]} for city in cities]
        # all_products = [product.__dict__ for product in products]
        # print(distinct_states)
        # print(distinct_cities)
        # print(all_products)
        return {
            "products": products,
            "state": [{"label": state, "value": state} for state in list_states],
            "city": cities_by_state,
            "address": list_street
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    