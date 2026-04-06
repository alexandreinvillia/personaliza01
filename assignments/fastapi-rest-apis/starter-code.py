# pyright: reportMissingImports=false

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Products API")


class ProductIn(BaseModel):
    name: str = Field(min_length=1)
    price: float = Field(gt=0)
    in_stock: bool


class Product(ProductIn):
    id: int


products: list[Product] = []
next_id = 1


@app.get("/products", response_model=list[Product])
def list_products() -> list[Product]:
    return products


@app.post("/products", response_model=Product, status_code=201)
def create_product(payload: ProductIn) -> Product:
    global next_id
    product = Product(id=next_id, **payload.model_dump())
    products.append(product)
    next_id += 1
    return product


@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int) -> Product:
    for product in products:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")


@app.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, payload: ProductIn) -> Product:
    for index, product in enumerate(products):
        if product.id == product_id:
            updated = Product(id=product_id, **payload.model_dump())
            products[index] = updated
            return updated
    raise HTTPException(status_code=404, detail="Product not found")


@app.delete("/products/{product_id}", status_code=204)
def delete_product(product_id: int) -> None:
    for index, product in enumerate(products):
        if product.id == product_id:
            products.pop(index)
            return None
    raise HTTPException(status_code=404, detail="Product not found")
