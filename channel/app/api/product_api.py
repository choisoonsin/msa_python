import requests

class CommonApi:

  def __init__(self):
    self.stock_server = "stock:8000/stock"
    self.product_server = "product:8000/product"

class ProductApi(CommonApi):

  def __init__(self):
    pass
    
  def read_items_by_category(self, category_id: str) -> dict:
    result = requests.get(self.product_server + f"/category/{category_id}", timeout=3)
    return result