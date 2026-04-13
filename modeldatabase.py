from sqlalchemy.orm import DeclarativeBase 
from sqlalchemy import Integer ,Float,Column,schema ,String, Boolean 

class Base(DeclarativeBase):
    pass 

class Dish(Base):
    __tablename__ ="Dishes" 
    dish_id = Column(Integer,primary_key =True)
    name = Column(String)
    price = Column(Float)
    dish_type=Column(String)
    veg = Column(Boolean)
   
