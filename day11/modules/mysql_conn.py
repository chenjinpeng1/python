import pymysql
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from  sqlalchemy.orm import sessionmaker


engine = create_engine("mysql+pymysql://root:chen27@localhost:3306/chen",echo=False)
sess = sessionmaker(bind=engine)
session = sess()