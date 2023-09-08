from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# Create a SQLAlchemy engine and session
engine = create_engine('sqlite:///your_database.db')
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

# Define the Vendor model
class Vendor(Base):
    __tablename__ = 'vendors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    # Define the one-to-many relationship with products
    products = relationship('Product', back_populates='vendor')

# Define the Product model
class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    # Define the foreign key relationship to the vendor
    vendor_id = Column(Integer, ForeignKey('vendors.id'))
    vendor = relationship('Vendor', back_populates='products')
    
    # Define the many-to-one relationship with farmers
    farmer_id = Column(Integer, ForeignKey('farmers.id'))
    farmer = relationship('Farmer', back_populates='products')

# Define the Farmer model
class Farmer(Base):
    __tablename__ = 'farmers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    # Define the one-to-many relationship with products
    products = relationship('Product', back_populates='farmer')

# Create the database tables
Base.metadata.create_all(engine)

# Now you can use the session to interact with the database
# For example, to query all vendors:
vendors = session.query(Vendor).all()
