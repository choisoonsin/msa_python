from fastapi import FastAPI

app = FastAPI()

@app.get("/stock/{id}")
def read_stock(id: int):
    return {"id": id, "name": f"stock_{id}"}