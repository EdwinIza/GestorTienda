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


# Crear un nuevo usuario
@app.post("/usuarios/", response_model=schemas.Usuario)
def create_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db) ):
    return crud.create_usuario(db=db, usuario=usuario)

# Crear una nueva tienda
@app.post("/tiendas/", response_model=schemas.Tienda)
def create_tienda(tienda: schemas.TiendaCreate, db: Session = Depends(get_db)):
    return crud.create_tienda(db=db, tienda=tienda )

# Otras configuraciones y rutas de la aplicación FastAPI
