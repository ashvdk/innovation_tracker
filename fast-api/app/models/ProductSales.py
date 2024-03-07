from sqlalchemy import VARCHAR, Column, Integer, Numeric, String, BIGINT
from database import Base


class ProductSales(Base):
    __tablename__ = "product_sales"

    id = Column(Integer, primary_key=True, index=True)
    country = Column(VARCHAR(255))
    company = Column(VARCHAR(255))
    segment = Column(VARCHAR(255))
    color = Column(VARCHAR(255))
    variant = Column(VARCHAR(255))
    extraoption = Column(VARCHAR(255))
    product_name = Column(VARCHAR(255))
    valusd = Column(BIGINT)
    units = Column(Integer)
    price_per_unit = Column(Integer)
    sales_year = Column(Integer)
    quater = Column(VARCHAR(100))
