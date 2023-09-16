from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import Base

router = APIRouter()

# Obtener todas las tiendas
@router.get("/tiendas/", response_model=list[schemas.Tienda])
def get_tiendas(db: Session = Depends(Base)):
    tiendas = db.query(models.Tienda).all()
    return tiendas

# Obtener una tienda por ID
@router.get("/tiendas/{tienda_id}", response_model=schemas.Tienda)
def get_tienda(tienda_id: int, db: Session = Depends(Base)):
    tienda = db.query(models.Tienda).filter(models.Tienda.id == tienda_id).first()
    if tienda is None:
        raise HTTPException(status_code=404, detail="Tienda no encontrada")
    return tienda

# Crear una nueva tienda
@router.post("/tiendas/", response_model=schemas.Tienda)
def create_tienda(tienda: schemas.TiendaCreate, db: Session = Depends(Base)):
    db_tienda = models.Tienda(**tienda.dict())
    db.add(db_tienda)
    db.commit()
    db.refresh(db_tienda)
    return db_tienda

# Actualizar una tienda por ID
@router.put("/tiendas/{tienda_id}", response_model=schemas.Tienda)
def update_tienda(tienda_id: int, tienda: schemas.TiendaUpdate, db: Session = Depends(Base)):
    db_tienda = db.query(models.Tienda).filter(models.Tienda.id == tienda_id).first()
    if db_tienda is None:
        raise HTTPException(status_code=404, detail="Tienda no encontrada")
    
    for key, value in tienda.dict(exclude_unset=True).items():
        setattr(db_tienda, key, value)
    
    db.commit()
    db.refresh(db_tienda)
    return db_tienda

# Eliminar una tienda por ID
@router.delete("/tiendas/{tienda_id}", response_model=schemas.Tienda)
def delete_tienda(tienda_id: int, db: Session = Depends(Base)):
    db_tienda = db.query(models.Tienda).filter(models.Tienda.id == tienda_id).first()
    if db_tienda is None:
        raise HTTPException(status_code=404, detail="Tienda no encontrada")
    db.delete(db_tienda)
    db.commit()
    return db_tienda
