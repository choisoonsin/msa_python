import requests


class Product:
    _target_server = "http://msa-product:8000/product"
    _default_timeout = 3

    @staticmethod
    def read_item(item_id: str) -> dict:
        res = requests.get(
            Product._target_server + f"/id/{item_id}",
            timeout=Product._default_timeout)
        return res

    @staticmethod
    def read_items_by_category(self, category_id: str) -> dict:
        res = requests.get(
            Product._target_server + f"/category/{category_id}",
            timeout=Product._default_timeout)
        return res


class Stock:
    _target_server = "http://msa-stock:8000/stock"
    _default_timeout = 3

    @staticmethod
    def read_stock(item_id: int):
        res = requests.get(
            Stock._target_server + f"/id/{item_id}",
            timeout=Stock._default_timeout
        )
        return res
