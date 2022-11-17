"""
    channel api
"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/read/item/{prod_id}")
def read_item(prod_id: int) -> dict:
  """read_item

  Args:
      prod_id (int): 상품아이디

  Returns:
      json: 상품정보
  """

  return {"id": prod_id, "name": f"stock_{prod_id}"}
