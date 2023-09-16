from pydantic import BaseModel
from enum import Enum

class TipoUsuarioEnum(str, Enum):
    admin = 'admin'
    jefe_tienda = 'jefe_tienda'
    jefe_caja = 'jefe_caja'
    promotor = 'promotor'

class UsuarioBase(BaseModel):
    nombre: str
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

class StockBase(BaseModel):
    nombre_producto: str
    cantidad: int
    tipo_stock: Enum('Stock1', 'Stock2')
    id_almacen: int

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