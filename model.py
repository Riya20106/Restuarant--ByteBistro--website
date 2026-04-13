from pydantic import BaseModel 

class Dish (BaseModel) :
   dish_id :int 
   price :float 
   name: str
   dish_type:str 
   veg : bool  

   