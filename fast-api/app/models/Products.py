from sqlalchemy import VARCHAR, Column, Integer, Numeric, String
from database import Base

class Products(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    product = Column(VARCHAR(100)) 
    price = Column(Numeric(precision=10, scale=2))