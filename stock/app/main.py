"""
    Stock-server
"""
from fastapi import FastAPI, HTTPException

app = FastAPI()

fake_db = [
    {"id": 1, "quantity": 100},
    {"id": 2, "quantity": 200},
    {"id": 3, "quantity": 300},
    {"id": 4, "quantity": 400},
    {"id": 5, "quantity": 500},
]

@app.get("/stock/id/{id}")
def read_stock(id: int):
    item = [x for x in fake_db if x["id"] == id]
    if len(item) == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return item[0]