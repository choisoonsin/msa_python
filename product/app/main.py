"""

    Product-server
"""
from fastapi import FastAPI, HTTPException

app = FastAPI()

fake_db = [
  {"id": 1, "name": "신발", "price": 29700, "category": "shoes"},
  {"id": 2, "name": "좋은 신발", "price": 189700, "category": "shoes"},
  {"id": 3, "name": "평범한 신발", "price": 56000, "category": "shoes"},
  {"id": 4, "name": "가디건", "price": 206000, "category": "outer"},
  {"id": 5, "name": "가죽자켓", "price": 346500, "category": "outer"},
]


@app.get("/product/category/{category_id}")
def read_items_by_category(category_id: str) -> dict:

  items = list(filter(lambda x: x["category"] == category_id, fake_db))

  return items


@app.get("/product/id/{prod_id}")
def read_item(prod_id: int) -> dict:

  item = [x for x in fake_db if x["id"] == prod_id]
  if len(item) == 0:
    raise HTTPException(status_code=404, detail="Item not found")

  return item[0]
