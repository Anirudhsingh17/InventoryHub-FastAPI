from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from database import engine, SessionLocal
import database_models
from models import Product

app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# # Create tables
# database_models.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Sample initial data
products_data = [
    Product(id=1, name="Phone", description="A smartphone", price=699.99, quantity=50),
    Product(id=2, name="Laptop", description="A powerful laptop", price=999.99, quantity=30),
    Product(id=3, name="Pen", description="A blue ink pen", price=1.99, quantity=100),
    Product(id=4, name="Table", description="A wooden table", price=199.99, quantity=20),
]


# Initialize DB
def init_db():
    db = SessionLocal()
    try:
        for product in products_data:
            existing = db.query(database_models.Product).filter_by(id=product.id).first()

            if not existing:
                db.add(database_models.Product(**product.model_dump()))

        db.commit()

    except Exception as e:
        db.rollback()
        print("Error:", e)

    finally:
        db.close()


@app.on_event("startup")
def startup():
    database_models.Base.metadata.create_all(bind=engine)
    init_db()


# Routes
@app.get("/")
def greet():
    return {"message": "Welcome to Our Server"}


@app.get("/products/")
def get_all_products(db: Session = Depends(get_db)):
    return db.query(database_models.Product).all()


@app.get("/products/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    product = db.query(database_models.Product).filter_by(id=id).first()
    if product:
        return product
    return {"message": "Not Found"}


@app.post("/products/")
def add_product(product: Product, db: Session = Depends(get_db)):
    db_product = database_models.Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


@app.put("/products/{id}")
def update_product(id: int, product: Product, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter_by(id=id).first()

    if not db_product:
        return {"message": "Product not found"}

    for key, value in product.model_dump().items():
        setattr(db_product, key, value)

    db.commit()
    db.refresh(db_product)
    return db_product


@app.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter_by(id=id).first()

    if not db_product:
        return {"message": "Product not found"}

    db.delete(db_product)
    db.commit()
    return {"message": "Deleted successfully"}