from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas
from app.database import Base

router = APIRouter()

# Obtener todos los usuarios
@router.get("/usuarios/", response_model=list[schemas.Usuario])
def get_usuarios(db: Session = Depends(Base)):
    usuarios = db.query(models.Usuario).all()
    return usuarios

# Obtener un usuario por ID
@router.get("/usuarios/{usuario_id}", response_model=schemas.Usuario)
def get_usuario(usuario_id: int, db: Session = Depends(Base)):
    usuario = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

# Crear un nuevo usuario
@router.post("/usuarios/", response_model=schemas.Usuario)
def create_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(Base)):
    db_usuario = models.Usuario(**usuario.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

# Actualizar un usuario por ID
@router.put("/usuarios/{usuario_id}", response_model=schemas.Usuario)
def update_usuario(usuario_id: int, usuario: schemas.UsuarioUpdate, db: Session = Depends(Base)):
    db_usuario = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    for key, value in usuario.dict(exclude_unset=True).items():
        setattr(db_usuario, key, value)
    
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

# Eliminar un usuario por ID
@router.delete("/usuarios/{usuario_id}", response_model=schemas.Usuario)
def delete_usuario(usuario_id: int, db: Session = Depends(Base)):
    db_usuario = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db.delete(db_usuario)
    db.commit()
    return db_usuario
