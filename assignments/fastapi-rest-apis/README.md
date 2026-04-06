# 📘 Assignment: REST APIs with FastAPI

## 🎯 Objective

Build a REST API with FastAPI to practice route creation, request validation, status codes, and basic in-memory data management.

## 📝 Tasks

### 🛠️ Create Product Endpoints

#### Description
Implement an API for product management using FastAPI. Start with an in-memory list (no database) and create endpoints for listing and creating products.

#### Requirements
Completed program should:

- Create a FastAPI app in `starter-code.py`.
- Implement `GET /products` to return all products.
- Implement `POST /products` to create a new product with fields: `name` (string), `price` (float > 0), and `in_stock` (boolean).
- Return status code `201` when a product is created.
- Validate invalid inputs and return proper FastAPI validation responses.


### 🛠️ Add Detail, Update, and Delete

#### Description
Expand the API with full CRUD behavior for a single product resource, identified by `product_id`.

#### Requirements
Completed program should:

- Implement `GET /products/{product_id}` to return one product or `404` if not found.
- Implement `PUT /products/{product_id}` to update all product fields.
- Implement `DELETE /products/{product_id}` to remove a product and return `204` with empty body.
- Ensure IDs are unique and auto-incremented.
- Keep behavior consistent and test manually with `/docs`.
