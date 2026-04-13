from fastapi import Depends,FastAPI 
from model import Dish
from databaseconnection import engine
from modeldatabase import Base
from sqlalchemy.orm import Session
from databaseconnection import sessionlocal,engine ,sessionmaker 
from fastapi.middleware.cors import CORSMiddleware
import modeldatabase
Base.metadata.create_all(bind=engine)

dishes=[ 
Dish(dish_id=1, price=400.0, name="Manchurian", dish_type="Appetizer", veg=True),
Dish(dish_id=2, price=450.0, name="Alfreo Pasta", dish_type="Appetizer", veg=True),
Dish(dish_id=4, price=459.0, name="Red Sauce Pasta", dish_type="Appetizer", veg=True),
Dish(dish_id=5, price=500.0, name="Veg Delight Farmhouse Pizza", dish_type="Appetizer", veg=True),
Dish(dish_id=6, price=550.0, name="Chicken Farm Pizza", dish_type="Appetizer", veg=False),
Dish(dish_id=7, price=300.0, name="Veg Spring Rolls", dish_type="Starter", veg=True),
Dish(dish_id=8, price=320.0, name="Paneer Tikka", dish_type="Starter", veg=True),
Dish(dish_id=9, price=350.0, name="Chicken Wings", dish_type="Starter", veg=False),
Dish(dish_id=10, price=280.0, name="French Fries", dish_type="Starter", veg=True),
Dish(dish_id=11, price=420.0, name="Veg Burger", dish_type="Main Course", veg=True),
Dish(dish_id=12, price=480.0, name="Chicken Burger", dish_type="Main Course", veg=False),
Dish(dish_id=13, price=600.0, name="Butter Chicken", dish_type="Main Course", veg=False),
Dish(dish_id=14, price=520.0, name="Paneer Butter Masala", dish_type="Main Course", veg=True),
Dish(dish_id=15, price=400.0, name="Chicken Biryani", dish_type="Main Course", veg=False),
Dish(dish_id=16, price=250.0, name="Gulab Jamun", dish_type="Dessert", veg=True),
Dish(dish_id=17, price=450.0, name="Tiramisu", dish_type="Dessert", veg=True),
Dish(dish_id=18, price=620.0, name="Pull Me Up Pistachio Cake", dish_type="Dessert", veg=True),
Dish(dish_id=19, price=500.0, name="Chocolate Truffle Cake", dish_type="Dessert", veg=True),
Dish(dish_id=20, price=640.0, name="Lotus Biscoff Cheesecake", dish_type="Dessert", veg=True),
]

def get_db():
 db = sessionlocal()
 try : 
   yield db 
 finally: 
   db.close() 

def init_db(): 
  db = sessionlocal()
  count =0 
  count =db.query(modeldatabase.Dish).count()
  if count==0:
   for Dish in dishes:
    db.add(modeldatabase.Dish(**Dish.model_dump())) 
    db.commit()

init_db()

app= FastAPI()

@app.get("/") 
def greet(): 
    return "Welcome to ByteBistro"

@app.get("/Menu")
def view_menu(db :Session = Depends(get_db)): 
    return db.query(modeldatabase.Dish).all()

@app.get("/bycategory/{d_type}")
def get_bycategory(d_type:str , db:Session = Depends(get_db)): 
    return db.query(modeldatabase.Dish).filter(modeldatabase.Dish.dish_type == d_type).all()

@app.get("/dishbyid/{id}")
def getbyid(id:int,db:Session = Depends(get_db)):
   return (db.query(modeldatabase.Dish).filter(modeldatabase.Dish.dish_id==id).first() )

@app.get("/veg") 
def get_veg(mode:str, db:Session = Depends(get_db)): 
    return ( db.query(modeldatabase.Dish).filter(modeldatabase.Dish.veg==True).all())
     
@app.get("/nonveg") 
def get_nonveg( db:Session = Depends(get_db)): 
    return ( db.query(modeldatabase.Dish).filter(modeldatabase.Dish.veg==False).all())   
     
@app.delete("/del_dish/{dishid}") 
def del_dish(dishid:int, db:Session = Depends(get_db)): 
 db_dish = db.query(modeldatabase.Dish).filter(modeldatabase.Dish.dish_id==dishid).first()
 if db_dish:
    db.delete(db_dish)
    db.commit()
    return "dish deleted"
 else :
    return "Dish not found"

@app.post("/post_dish")
def post_dish(d :Dish,db:Session = Depends(get_db)): 
    db.add(modeldatabase.Dish(**d.model_dump()))
    db.commit()
    return "Dish posted"

# from fastapi import FastAPI  
# from model import Student 

# Students =[ 
#     Student (prn=1234,name="karan",marks=78.9,roll=6),
#     Student (prn=2345,name="siya",marks=90,roll=4),
#     Student (prn=3456,name="Riya",marks=95,roll=6),
#     Student (prn=4567,name="diya",marks=89.3,roll=9),
# ]
# app=FastAPI() 

# @app.get("/") 
# def greet(): 
#     return "hello There , welcome !"; 
 
# @app.get("/viewdata") 
# def viewdata(): 
#      return Students
 
         

# @app.get("/byid/{prn}")
# def getstudentbyid(prn:int): 
#     for Student in Students : 
#         if Student.prn ==prn:
#           return Student  
#     return "student not found" 


# @app.put("/updatest/{prn}")
# def update_st(prn:int ,student:Student):
#     for s in Students: 
#       if s.prn==prn:   
#           s.name= student.name 
#           s.marks= student.marks
#           s.roll = student.roll
#           return "Student updated" 
#     return "not Updated" 

# @app.post("/post") 
# def post_st(student :Student): 
#    Students.append(student) 
#    return "student added" 

# @app.delete("/delete_st/{prn}") 
# def delete_st(prn:int): 
#   for s in range(len(Students)): 
#     if Students[s].prn==prn: 
#       Students.pop(s) 
#       return "student deletd" 
#   return "student not deleted" 
