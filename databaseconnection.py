from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker 
  
dburl ="postgresql://postgres:Riya2006!@localhost:5432/Restaurant_BB" 
# dburl = "postgresql://postgres:Riya2006%21@localhost:5432/Restaurant_BB"

engine = create_engine(dburl) 
sessionlocal = sessionmaker(autocommit=False,autoflush=False,bind=engine) 
