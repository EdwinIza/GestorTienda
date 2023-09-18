from pydantic import BaseModel
from enum import Enum
from datetime import date

class TipoUsuarioEnum(str, Enum):
    admin = 'admin'
    bodeguero = 'bodeguero'
    promotor = 'promotor'

class UsuarioBase(BaseModel):
    cedula: str
    nombres: str
    apellidos: str
    email: str
    contrasena: str
    tipo_usuario: TipoUsuarioEnum

class UsuarioCreate(UsuarioBase):
    pass

class Usuario(UsuarioBase):
    id: int

    class Config:
        orm_mode = True

class UsuarioUpdate(BaseModel):
    nombre: str
    email: str
    contrasena: str
    tipo_usuario: TipoUsuarioEnum
    
class TiendaBase(BaseModel):
    nombre: str
    direccion: str

class TiendaCreate(TiendaBase):
    pass

class Tienda(TiendaBase):
    id: int

    class Config:
        orm_mode = True

class TiendaUpdate(BaseModel):
    nombre: str
    direccion: str

class AlmacenBase(BaseModel):
    nombre: str
    ubicacion: str

class AlmacenCreate(AlmacenBase):
    pass

class Almacen(AlmacenBase):
    id: int

    class Config:
        orm_mode = True

class AlmacenUpdate(BaseModel):
    nombre: str
    ubicacion: str

class ClienteBase(BaseModel):
    nombre: str
    direccion: str

class ClienteCreate(ClienteBase):
    pass

class Cliente(ClienteBase):
    id: int

    class Config:
        orm_mode = True

class ClienteUpdate(BaseModel):
    nombre: str
    direccion: str

class TipoStockEnum(str, Enum):
    Stock1 = 'Stock1'
    Stock2 = 'Stock2'

class StockBase(BaseModel):
    codigo: str  # Agregar el campo "codigo"
    nombre_producto: str
    cantidad: int
    tipo_stock: TipoStockEnum
    id_almacen: int
    fecha_recepcion: date  # Agregar el campo "fecha_recepcion"


class StockBase(BaseModel):
    codigo: str  # Agregar el campo "codigo"
    nombre_producto: str
    cantidad: int
    tipo_stock: TipoStockEnum
    id_almacen: int
    fecha_recepcion: date  # Agregar el campo "fecha_recepcion"


class StockCreate(StockBase):
    pass

class Stock(StockBase):
    id: int

    class Config:
        orm_mode = True


class StockUpdate(BaseModel):
    nombre_producto: str
    cantidad: int
    tipo_stock: str  # Debes definir un tipo válido, por ejemplo, 'Stock1' o 'Stock2'
    id_almacen: int