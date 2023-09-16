from sqlalchemy.orm import Session

from app import models, schemas

#USUARIOS
def create_usuario(usuario: schemas.UsuarioCreate, db: Session ):
    db_usuario = models.Usuario(**usuario.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

#TIENDAS
def create_tienda(db: Session, tienda: schemas.TiendaCreate):
    db_tienda = models.Tienda(**tienda.dict())
    db.add(db_tienda)
    db.commit()
    db.refresh(db_tienda)
    return db_tienda


