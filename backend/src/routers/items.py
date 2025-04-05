from fastapi import APIRouter, Path, Query
from src.schemas.items import Item

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{item_id}")
async def read_item(
    item_id: int = Path(..., title="アイテムのID"),
    q: str = Query(None, min_length=3, max_length=50),
):
    return {"item_id": item_id, "q": q}


@router.post("/create")
async def create_item(item: Item):
    return item
