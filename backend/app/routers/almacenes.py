from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import Base
from typing import List

router = APIRouter()

# Obtener todos los almacenes
@router.get("/almacenes/", response_model=List[schemas.Almacen])
def get_almacenes(db: Session = Depends(Base)):
    almacenes = db.query(models.Almacen).all()
    return almacenes

# Obtener un almacén por ID
@router.get("/almacenes/{almacen_id}", response_model=schemas.Almacen)
def get_almacen(almacen_id: int, db: Session = Depends(Base)):
    almacen = db.query(models.Almacen).filter(models.Almacen.id == almacen_id).first()
    if almacen is None:
        raise HTTPException(status_code=404, detail="Almacén no encontrado")
    return almacen

# Crear un nuevo almacén
@router.post("/almacenes/", response_model=schemas.Almacen)
def create_almacen(almacen: schemas.AlmacenCreate, db: Session = Depends(Base)):
    db_almacen = models.Almacen(**almacen.dict())
    db.add(db_almacen)
    db.commit()
    db.refresh(db_almacen)
    return db_almacen

# Actualizar un almacén por ID
@router.put("/almacenes/{almacen_id}", response_model=schemas.Almacen)
def update_almacen(almacen_id: int, almacen: schemas.AlmacenUpdate, db: Session = Depends(Base)):
    db_almacen = db.query(models.Almacen).filter(models.Almacen.id == almacen_id).first()
    if db_almacen is None:
        raise HTTPException(status_code=404, detail="Almacén no encontrado")
    
    for key, value in almacen.dict(exclude_unset=True).items():
        setattr(db_almacen, key, value)
    
    db.commit()
    db.refresh(db_almacen)
    return db_almacen

# Eliminar un almacén por ID
@router.delete("/almacenes/{almacen_id}", response_model=schemas.Almacen)
def delete_almacen(almacen_id: int, db: Session = Depends(Base)):
    db_almacen = db.query(models.Almacen).filter(models.Almacen.id == almacen_id).first()
    if db_almacen is None:
        raise HTTPException(status_code=404, detail="Almacén no encontrado")
    db.delete(db_almacen)
    db.commit()
    return db_almacen
