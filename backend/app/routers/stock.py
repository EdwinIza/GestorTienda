from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import Base
from typing import List

router = APIRouter()

# Obtener todo el stock
@router.get("/stock/", response_model=List[schemas.Stock])
def get_stock(db: Session = Depends(Base)):
    stock = db.query(models.Stock).all()
    return stock

# Obtener un elemento de stock por ID
@router.get("/stock/{stock_id}", response_model=schemas.Stock)
def get_stock_item(stock_id: int, db: Session = Depends(Base)):
    stock_item = db.query(models.Stock).filter(models.Stock.id == stock_id).first()
    if stock_item is None:
        raise HTTPException(status_code=404, detail="Elemento de stock no encontrado")
    return stock_item

# Crear un nuevo elemento de stock
@router.post("/stock/", response_model=schemas.Stock)
def create_stock_item(stock_item: schemas.StockCreate, db: Session = Depends(Base)):
    db_stock_item = models.Stock(**stock_item.dict())
    db.add(db_stock_item)
    db.commit()
    db.refresh(db_stock_item)
    return db_stock_item

# Actualizar un elemento de stock por ID
@router.put("/stock/{stock_id}", response_model=schemas.Stock)
def update_stock_item(stock_id: int, stock_item: schemas.StockUpdate, db: Session = Depends(Base)):
    db_stock_item = db.query(models.Stock).filter(models.Stock.id == stock_id).first()
    if db_stock_item is None:
        raise HTTPException(status_code=404, detail="Elemento de stock no encontrado")
    
    for key, value in stock_item.dict(exclude_unset=True).items():
        setattr(db_stock_item, key, value)
    
    db.commit()
    db.refresh(db_stock_item)
    return db_stock_item

# Eliminar un elemento de stock por ID
@router.delete("/stock/{stock_id}", response_model=schemas.Stock)
def delete_stock_item(stock_id: int, db: Session = Depends(Base)):
    db_stock_item = db.query(models.Stock).filter(models.Stock.id == stock_id).first()
    if db_stock_item is None:
        raise HTTPException(status_code=404, detail="Elemento de stock no encontrado")
    db.delete(db_stock_item)
    db.commit()
    return db_stock_item

#CLIENTES

