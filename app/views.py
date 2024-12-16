from sqlalchemy.orm import Session
from fastapi import Depends, Request
from app.models import Inventory
from app.schemas import StockItem
from config.db.base import get_db

def home():
    return "PreciTaste"

async def addStock(stock_item: StockItem, request: Request, db: Session = Depends(get_db)):

    inventory_item = db.query(Inventory).filter(Inventory.item_name == stock_item.item_name).first()
    if inventory_item:
        # Update Quantity
        inventory_item.quantity += stock_item.quantity
    else:
        # Add a new item
        inventory_item = Inventory(item_name=stock_item.item_name, quantity=stock_item.quantity)
        db.add(inventory_item)
    db.commit()
    
    return {"message" :f"Stock Update: {stock_item.item_name} = {inventory_item.quantity}"}

async def updateStock(request: Request, db: Session = Depends(get_db)):
    data = await request.json()
    inventory_item = db.query(Inventory).filter(Inventory.id==data['id']).first()
    inventory_item.quantity -= data['quantity']
    db.commit()
    return {"message": "Inventory updated successfully", "item": f"{inventory_item.item_name} = {inventory_item.quantity}"}

async def calculateItem(db: Session = Depends(get_db)):
    inventory_item = db.query(Inventory).all()
    stock = {item.item_name: item.quantity for item in inventory_item}
    return stock