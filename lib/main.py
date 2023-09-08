from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Vendor, Product, Farmer, Consumer

engine = create_engine('sqlite:///market.db')

Vendor.metadata.create_all(engine)
Product.metadata.create_all(engine)
Farmer.metadata.create_all(engine)
Consumer.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

print("List of Vendors:")
vendors = session.query(Vendor).all()
for vendor in vendors:
    print(f"Vendor ID: {vendor.id}, Vendor Name: {vendor.name}")

print("\nList of Products:")
products = session.query(Product).all()
for product in products:
    print(f"Product ID: {product.id}, Product Name: {product.name}, Vendor: {product.vendor.name}")

print("\nList of Farmers:")
farmers = session.query(Farmer).all()
for farmer in farmers:
    print(f"Farmer ID: {farmer.id}, Farmer Name: {farmer.name}")

print("\nList of Consumers:")
consumers = session.query(Consumer).all()
for consumer in consumers:
    print(f"Consumer ID: {consumer.id}, Consumer Name: {consumer.name}")

target_product_name = "Product 1"
target_product = session.query(Product).filter_by(name=target_product_name).first()
if target_product:
    print(f"\nProduct found: {target_product.name}, Vendor: {target_product.vendor.name}")
else:
    print(f"\nProduct '{target_product_name}' not found.")

session.close()
