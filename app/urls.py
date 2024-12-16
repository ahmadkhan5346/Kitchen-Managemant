from fastapi import APIRouter
from app.views import home, addStock, calculateItem, updateStock


router = APIRouter()

router.get("/")(home)
router.post("/api/insert-item")(addStock)
router.put("/api/update-item")(updateStock)
router.get("/api/calculate-item")(calculateItem)