from fastapi import APIRouter, Request, HTTPException
from database import SessionLocal
from models.Filters import Filters

def get_filters(reqBody):
    
    try:
        db = SessionLocal()
        bodyState = reqBody.get("state")
        states = db.query(Filters.state).distinct().all()
        if len(bodyState) > 0:
            cities = db.query(Filters.city).distinct().filter(Filters.state.in_(bodyState)).all()
        else:
            cities = db.query(Filters.city).distinct().all()
        db.close()
        distinct_states = [{"label": state[0], "value": state[0]} for state in states]
        distinct_cities = [{"label": city[0], "value": city[0]} for city in cities]
        print(distinct_states)
        print(distinct_cities)
        return {
            "state": distinct_states,
            "city": distinct_cities,
            "dateRange": "dfd"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    