from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Products API")


# Product Model
class Product(BaseModel):
    id: int
    name: str
    price: float


# In-memory database
products: List[Product] = [
    Product(id=1, name="Laptop", price=1200),
    Product(id=2, name="Mouse", price=25),
    Product(id=3, name="Keyboard", price=80),
]


# GET /products
@app.get("/products", response_model=List[Product])
def get_products(max_price: Optional[float] = None):
    if max_price is not None:
        return [product for product in products if product.price < max_price]
    return products


# GET /products/{id}
@app.get("/products/{id}", response_model=Product)
def get_product(id: int):
    for product in products:
        if product.id == id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")


# POST /products
@app.post("/products", response_model=Product)
def create_product(product: Product):
    for p in products:
        if p.id == product.id:
            raise HTTPException(status_code=400, detail="Product ID already exists")

    products.append(product)
    return product


# PUT /products/{id}
@app.put("/products/{id}", response_model=Product)
def update_product(id: int, updated_product: Product):
    for index, product in enumerate(products):
        if product.id == id:
            products[index] = updated_product
            return updated_product

    raise HTTPException(status_code=404, detail="Product not found")


# DELETE /products/{id}
@app.delete("/products/{id}")
def delete_product(id: int):
    for index, product in enumerate(products):
        if product.id == id:
            deleted = products.pop(index)
            return {
                "message": "Product deleted successfully",
                "product": deleted
            }

    raise HTTPException(status_code=404, detail="Product not found")