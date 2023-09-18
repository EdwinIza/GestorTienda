from sqlalchemy.orm import Session

from app import models, schemas

#USUARIOS
#Obtiene todos los usuarios
def get_usuarios(db: Session):
    usuarios = db.query(models.Usuario).all()
    return usuarios

#Obtiene usuario por ID
def get_usuario(usuario_id: int, db: Session):
    usuario = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    return usuario

#Crea Usuarios
def create_usuario(usuario: schemas.UsuarioCreate, db: Session ):
    db_usuario = models.Usuario(**usuario.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

#Actualizar Usuario
def update_usuario(usuario_id: int, usuario: schemas.UsuarioUpdate, db: Session):
    db_usuario = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    for key, value in usuario.dict(exclude_unset=True).items():
        setattr(db_usuario, key, value)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

#Eliminar Usuario
def delete_usuario(usuario_id: int, db: Session):
    db_usuario = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    db.delete(db_usuario)
    db.commit()
    return db_usuario

#TIENDAS
#Obtiene todas las tiendas
def get_tiendas(db: Session):
    tiendas = db.query(models.Tienda).all()
    return tiendas

#Obtener tienda por ID
def get_tienda(tienda_id: int, db: Session):
    tienda = db.query(models.Tienda).filter(models.Tienda.id == tienda_id).first()
    return tienda

#Crear tiendas
def create_tienda(db: Session, tienda: schemas.TiendaCreate):
    db_tienda = models.Tienda(**tienda.dict())
    db.add(db_tienda)
    db.commit()
    db.refresh(db_tienda)
    return db_tienda

#Actualizar una tienda por ID
def update_tienda(tienda_id: int, tienda: schemas.TiendaUpdate, db: Session):
    db_tienda = db.query(models.Tienda).filter(models.Tienda.id == tienda_id).first()

    for key, value in tienda.dict(exclude_unset=True).items():
        setattr(db_tienda, key, value)
    
    db.commit()
    db.refresh(db_tienda)
    return db_tienda

#Eliminar una Tienda
def delete_tienda(tienda_id: int, db: Session ):
    db_tienda = db.query(models.Tienda).filter(models.Tienda.id == tienda_id).first()
    db.delete(db_tienda)
    db.commit()
    return db_tienda

#ALMACENES
#Obtener todos los almacenes
def get_almacenes(db: Session):
    almacenes = db.query(models.Almacen).all()
    return almacenes

# Obtener un almacén por ID
def get_almacen(almacen_id: int, db: Session ):
    almacen = db.query(models.Almacen).filter(models.Almacen.id == almacen_id).first()
    return almacen

#Crear Almacen
def create_almacen(almacen: schemas.AlmacenCreate, db: Session ):
    db_almacen = models.Almacen(**almacen.dict())
    db.add(db_almacen)
    db.commit()
    db.refresh(db_almacen)
    return db_almacen

#Actualizar Almacen
def update_almacen(almacen_id: int, almacen: schemas.AlmacenUpdate, db: Session):
    db_almacen = db.query(models.Almacen).filter(models.Almacen.id == almacen_id).first()

    for key, value in almacen.dict(exclude_unset=True).items():
        setattr(db_almacen, key, value)
    
    db.commit()
    db.refresh(db_almacen)
    return db_almacen

# Eliminar un almacén por ID
def delete_almacen(almacen_id: int, db: Session):
    db_almacen = db.query(models.Almacen).filter(models.Almacen.id == almacen_id).first()
    db.delete(db_almacen)
    db.commit()
    return db_almacen

#STOCK
#Obtener todo stock
def get_stock(db: Session):
    stock = db.query(models.Stock).all()
    return stock

# Obtener un elemento de stock por ID
def get_stock_item(stock_id: int, db: Session):
    stock_item = db.query(models.Stock).filter(models.Stock.id == stock_id).first()
    return stock_item

# Crear un nuevo elemento de stock
def create_stock_item(stock_item: schemas.StockCreate, db: Session):
    db_stock_item = models.Stock(**stock_item.dict())
    db.add(db_stock_item)
    db.commit()
    db.refresh(db_stock_item)
    return db_stock_item

# Actualizar un elemento de stock por ID
def update_stock_item(stock_id: int, stock_item: schemas.StockUpdate, db: Session):
    db_stock_item = db.query(models.Stock).filter(models.Stock.id == stock_id).first()

    for key, value in stock_item.dict(exclude_unset=True).items():
        setattr(db_stock_item, key, value)
    
    db.commit()
    db.refresh(db_stock_item)
    return db_stock_item

# Eliminar un elemento de stock por ID
def delete_stock_item(stock_id: int, db: Session ):
    db_stock_item = db.query(models.Stock).filter(models.Stock.id == stock_id).first()
    db.delete(db_stock_item)
    db.commit()
    return db_stock_item

#Clientes
# Obtener todos los clientes
def get_clientes(db: Session):
    clientes = db.query(models.Cliente).all()
    return clientes

# Obtener un cliente por ID
def get_cliente(cliente_id: int, db: Session):
    cliente = db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()
    return cliente

# Crear un nuevo cliente
def create_cliente(cliente: schemas.ClienteCreate, db: Session):
    db_cliente = models.Cliente(**cliente.dict())
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

# Actualizar un cliente por ID
def update_cliente(cliente_id: int, cliente: schemas.ClienteUpdate, db: Session):
    db_cliente = db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()
    
    for key, value in cliente.dict(exclude_unset=True).items():
        setattr(db_cliente, key, value)
    
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

# Eliminar un cliente por ID
def delete_cliente(cliente_id: int, db: Session ):
    db_cliente = db.query(models.Cliente).filter(models.Cliente.id == cliente_id).first()
    db.delete(db_cliente)
    db.commit()
    return db_cliente
