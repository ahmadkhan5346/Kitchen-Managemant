from pydantic import BaseModel

class StockItem(BaseModel):
    """Pydantic model for stock items."""
    item_name: str
    quantity: int
