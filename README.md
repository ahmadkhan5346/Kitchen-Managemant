Inventory Management API
This module provides endpoints to manage the stock of items in an inventory. It includes functionality to add stock, update stock quantities, and calculate the total stock for all items. The code uses FastAPI for building the API and SQLAlchemy for database interaction.

Functions Overview
home():

A simple function that returns a welcome message ("PreciTaste").
This can be used to verify that the service is running.
addStock(stock_item: StockItem, request: Request, db: Session = Depends(get_db)):

Adds or updates the quantity of an item in the inventory.
If the item already exists in the inventory, its quantity is increased.
If the item does not exist, a new entry is created.
After the operation, the database is committed, and a success message with the updated quantity is returned.
updateStock(request: Request, db: Session = Depends(get_db)):

Decreases the quantity of an existing item in the inventory.
Accepts a JSON request with the item's ID and the quantity to deduct.
Updates the database and commits the changes.
Returns a success message with the item's name and updated quantity.
calculateItem(db: Session = Depends(get_db)):

Retrieves all items in the inventory and calculates the current stock for each item.
Returns a dictionary where the keys are item names and the values are their respective quantities.
Features
Dynamic Stock Management: Add new items or update the quantity of existing items in the inventory.
Easy Quantity Updates: Deduct quantities from items using their unique IDs.
Stock Overview: Fetch a complete list of all items with their current stock levels.
Tech Stack
FastAPI: For building the REST API.
SQLAlchemy: For ORM-based database interaction.
PostgreSQL: The database used for storing inventory data.
Pydantic: For data validation and request schema definition.
Database Models
The code assumes the following Inventory model is defined in the app.models module:

python
Copy code
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Inventory(Base):
    __tablename__ = "inventory"
    id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String, unique=True, index=True)
    quantity = Column(Integer, default=0)
Usage
Add Stock: Send a POST request to the addStock endpoint with the item name and quantity to add or update.
Update Stock: Send a POST request to the updateStock endpoint with the item's ID and quantity to deduct.
View Stock: Send a GET request to the calculateItem endpoint to retrieve the current stock for all items.

Example Endpoints
Add Stock:
POST /addStock
{
  "item_name": "Burger Bun",
  "quantity": 10
}

Response:
{
  "message": "Stock Update: Burger Bun = 10"
}

Update Stock:
POST /updateStock
{
  "id": 1,
  "quantity": 3
}

Response:
{
  "message": "Inventory updated successfully",
  "item": "Burger Bun = 7"
}

View Stock:
GET /calculateItem
Response:

{
  "Burger Bun": 7,
  "Beef Patty": 15
}