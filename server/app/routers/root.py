from fastapi import APIRouter

# define router
router = APIRouter(
    tags=["root"]
)


@router.get("/")
def read_root():
    return {"Hello": "World"}


@router.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
