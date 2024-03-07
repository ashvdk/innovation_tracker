from sqlalchemy import VARCHAR, Column, Integer, Numeric, String
from database import Base

class Sales(Base):
    __tablename__ = 'sales'

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(VARCHAR(100)) 
    product = Column(VARCHAR(100))
    quantity_ordered = Column(Integer) 
    price_each = Column(Numeric(precision=10, scale=2)) 
    order_date = Column(VARCHAR(100)) 
    purchase_address = Column(VARCHAR(100)) 
    city = Column(VARCHAR(100)) 
    state = Column(VARCHAR(100)) 
    zip_code = Column(VARCHAR(100)) 