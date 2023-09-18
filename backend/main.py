from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.database import SessionLocal, engine

#from app.routers import tiendas, almacenes, stock, usuarios, clientes  # Importa los enrutadores


models.Base.metadata.create_all(bind=engine)


app = FastAPI()

# Configurar la dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Configurar CORS para permitir solicitudes desde todos los dominios (cambia esto según tus necesidades)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes especificar aquí los dominios permitidos
    allow_credentials=True,
    allow_methods=["*"],  # Puedes especificar aquí los métodos HTTP permitidos
    allow_headers=["*"],  # Puedes especificar aquí los encabezados permitidos
)

# Monta los enrutadores

#USUARIOS
#Obtiene todos los usuarios
@app.get("/usuarios/", response_model=list[schemas.Usuario])
def get_usuarios(db: Session = Depends(get_db)):
    return crud.get_usuarios(db=db)

#Obtiene usuarios por ID
@app.get("/usuarios/{usuario_id}", response_model=schemas.Usuario)
def get_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario_db = crud.get_usuario(usuario_id=usuario_id, db=db)
    if usuario_db is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario_db

#Crear un nuevo usuario
@app.post("/usuarios/", response_model=schemas.Usuario)
def create_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db) ):
    return crud.create_usuario(db=db, usuario=usuario)

#Actualizar usuario
@app.put("/usuarios/{usuario_id}", response_model=schemas.Usuario)
def update_usuario(usuario_id: int, usuario: schemas.UsuarioUpdate, db: Session = Depends(get_db)):
    usuario_db = crud.update_usuario(usuario_id=usuario_id,usuario=usuario , db=db)
    if usuario_db is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario_db

#Eliminar usuario
@app.delete("/usuarios/{usuario_id}", response_model=schemas.Usuario)
def delete_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario_db = crud.delete_usuario(usuario_id=usuario_id, db=db )
    if usuario_db is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario_db

#TIENDAS
#Obtener todas las tiendas
@app.get("/tiendas/", response_model=list[schemas.Tienda])
def get_tiendas(db: Session = Depends(get_db)):
    return crud.get_tiendas(db=db)

#Obtener tienda por ID
@app.get("/tiendas/{tienda_id}", response_model=schemas.Tienda)
def get_tienda(tienda_id: int, db: Session = Depends(get_db)):
    tienda = crud.get_tienda(tienda_id=tienda_id, db=db)
    if tienda is None:
        raise HTTPException(status_code=404, detail="Tienda no encontrada")
    return tienda

# Crear una nueva tienda
@app.post("/tiendas/", response_model=schemas.Tienda)
def create_tienda(tienda: schemas.TiendaCreate, db: Session = Depends(get_db)):
    return crud.create_tienda(db=db, tienda=tienda )

#Actualizar una tienda
@app.put("/tiendas/{tienda_id}", response_model=schemas.Tienda)
def update_tienda(tienda_id: int, tienda: schemas.TiendaUpdate, db: Session = Depends(get_db)):
    db_tienda = crud.update_tienda(tienda_id=tienda_id, tienda=tienda, db=db)
    if db_tienda is None:
        raise HTTPException(status_code=404, detail="Tienda no encontrada")
    return db_tienda

#Eliminar una Tienda
@app.delete("/tiendas/{tienda_id}", response_model=schemas.Tienda)
def delete_tienda(tienda_id: int, db: Session = Depends(get_db) ):
    db_tienda = crud.delete_tienda(tienda_id=tienda_id, db=db)
    if db_tienda is None:
        raise HTTPException(status_code=404, detail="Tienda no encontrada")
    return db_tienda

#ALMACENES
#Obtener todos los almacenes
@app.get("/almacenes/", response_model=list[schemas.Almacen])
def get_almacenes(db: Session = Depends(get_db)):
    return crud.get_almacenes(db=db)

#Obtener almacen por Id
@app.get("/almacenes/{almacen_id}", response_model=schemas.Almacen)
def get_almacen(almacen_id: int, db: Session = Depends(get_db) ):
    almacen = crud.get_almacen(almacen_id=almacen_id, db=db)
    if almacen is None:
        raise HTTPException(status_code=404, detail="Almacen no encontrado")    
    return almacen

#Crear Almacenes
@app.post("/almacenes/", response_model=schemas.Almacen)
def create_almacen(almacen: schemas.AlmacenCreate, db: Session = Depends(get_db) ):
    db_almacen = crud.create_almacen(almacen=almacen, db=db)
    return db_almacen

#Actualizar Almacenes
@app.put("/almacenes/{almacen_id}", response_model=schemas.Almacen)
def update_almacen(almacen_id: int, almacen: schemas.AlmacenUpdate, db: Session = Depends(get_db)):
    db_almacen = crud.update_almacen(almacen_id=almacen_id, almacen=almacen, db=db)
    if db_almacen is None:
        raise HTTPException(status_code=404, detail="Almacen no encontrado") 
    return db_almacen

#Eliminar Almacen
@app.delete("/almacenes/{almacen_id}", response_model=schemas.Almacen)
def delete_almacen(almacen_id: int, db: Session = Depends(get_db)):
    db_almacen = crud.delete_almacen
    if db_almacen is None:
        raise HTTPException(status_code=404, detail="Almacen no encontrado")     
    return db_almacen

#STOCK
#Obtener Stock
@app.get("/stock/", response_model=list[schemas.Stock])
def get_stock(db: Session = Depends(get_db)):
    return crud.get_stock(db=db)

# Obtener un elemento de stock por ID
@app.get("/stock/{stock_id}", response_model=schemas.Stock)
def get_stock_item(stock_id: int, db: Session = Depends(get_db)):
    stock_item = crud.get_stock_item(stock_id=stock_id, db=db)
    if stock_item is None:
        raise HTTPException(status_code=404, detail="Elemento de stock no encontrado")    
    return stock_item

# Crear un nuevo elemento de stock
@app.post("/stock/", response_model=schemas.Stock)
def create_stock_item(stock_item: schemas.StockCreate, db: Session = Depends(get_db)):
    db_stock_item = crud.create_stock_item(stock_item=stock_item, db=db)
    return db_stock_item

# Actualizar un elemento de stock por ID
@app.put("/stock/{stock_id}", response_model=schemas.Stock)
def update_stock_item(stock_id: int, stock_item: schemas.StockUpdate, db: Session = Depends(get_db)):
    db_stock_item = crud.update_stock_item(stock_id=stock_id, stock_item=stock_item, db=db)
    if db_stock_item is None:
        raise HTTPException(status_code=404, detail="Elemento de stock no encontrado")    
    return db_stock_item

# Eliminar un elemento de stock por ID
@app.delete("/stock/{stock_id}", response_model=schemas.Stock)
def delete_stock_item(stock_id: int, db: Session = Depends(get_db) ):
    db_stock_item = crud.delete_stock_item(stock_id=stock_id, db=db)
    return db_stock_item

#CLIENTES
# Obtener todos los clientes
@app.get("/clientes/", response_model=list[schemas.Cliente])
def get_clientes(db: Session = Depends(get_db)):
    return crud.get_clientes(db=db)

# Obtener un cliente por ID
@app.get("/clientes/{cliente_id}", response_model=schemas.Cliente)
def get_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cliente = crud.get_cliente(cliente_id=cliente_id, db=db)
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente

# Crear un nuevo cliente
@app.post("/clientes/", response_model=schemas.Cliente)
def create_cliente(cliente: schemas.ClienteCreate, db: Session = Depends(get_db)):
    db_cliente = crud.create_cliente(cliente=cliente, db=db)
    return db_cliente

# Actualizar un cliente por ID
@app.put("/clientes/{cliente_id}", response_model=schemas.Cliente)
def update_cliente(cliente_id: int, cliente: schemas.ClienteUpdate, db: Session = Depends(get_db)):
    db_cliente = crud.update_cliente(cliente_id=cliente_id, cliente=cliente, db=db)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return db_cliente

# Eliminar un cliente por ID
def delete_cliente(cliente_id: int, db: Session = Depends(get_db) ):
    db_cliente = crud.delete_cliente(cliente_id=cliente_id, db=db)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return db_cliente

# Otras configuraciones y rutas de la aplicación FastAPI
