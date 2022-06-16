from sqlalchemy import Column, DateTime, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func


Base = declarative_base()

class Inventory(Base):
    __tablename__ = "Inventory"
    id = Column(Integer, primary_key=True, index=True)
    item = Column(String)
    time_purchased = Column(DateTime(timezone=True), server_default=func.now())
    price_per_unit = Column(Float, index=True)
    unit = Column(Float)
    quantity = Column(Float, index=True)
