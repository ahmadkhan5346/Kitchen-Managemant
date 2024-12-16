from sqlalchemy import Column, Integer, String
from config.db.base import Base

class Inventory(Base):
    """Database model for inventory items."""
    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String, index=True, unique=True)
    quantity = Column(Integer, default=0)
