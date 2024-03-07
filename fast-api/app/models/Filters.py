from sqlalchemy import VARCHAR, Column, Integer, Numeric, String
from database import Base

class Filters(Base):
    __tablename__ = 'filters'

    id = Column(Integer, primary_key=True, index=True)
    address = Column(VARCHAR(100)) 
    city = Column(VARCHAR(100)) 
    state = Column(VARCHAR(100)) 
    zip_code = Column(VARCHAR(100)) 