"""
    channel api
"""

from fastapi import FastAPI

import app.api.api_service as api

app = FastAPI()


@app.get("/read/item/{item_id}")
def read_item(item_id: int) -> dict:
    """read_item

      Args:
          item_id (int): 상품아이디

      Returns:
          json: 상품정보
    """

    prod = api.Product.read_item(item_id=item_id).json()
    stock = api.Stock.read_stock(item_id=item_id).json()

    return {
        "id": item_id,
        "name": prod['name'],
        "price": prod['price'],
        "category": prod['category'],
        "quantity": stock['quantity']}
