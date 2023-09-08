from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///market.db')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Consumer(Base):
    __tablename__ = 'consumers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    phone_number = Column(String)

    def __init__(self,name,email,phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number


class Vendor(Base):
    __tablename__ = 'vendors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    

    products = relationship('Product', back_populates='vendor')


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
  
    vendor_id = Column(Integer, ForeignKey('vendors.id'))
    vendor = relationship('Vendor', back_populates='products')
    

    farmer_id = Column(Integer, ForeignKey('farmers.id'))
    farmer = relationship('Farmer', back_populates='products')

class Farmer(Base):
    __tablename__ = 'farmers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    

    products = relationship('Product', back_populates='farmer')


Base.metadata.create_all(engine)


vendors = session.query(Vendor).all()
