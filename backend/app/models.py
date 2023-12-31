from sqlalchemy import Column, Integer, String, ForeignKey, Date, Enum
from sqlalchemy.orm import relationship
from app.database import Base,engine

Base.metadata.create_all(bind=engine)

from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    cedula = Column(String, nullable=False, index=True)
    nombres = Column(String, index=True)
    apellidos = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    contrasena = Column(String)
    tipo_usuario = Column(Enum('admin', 'bodeguero', 'promotor'), nullable=False)


class Tienda(Base):
    __tablename__ = "tiendas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    direccion = Column(String)

class Almacen(Base):
    __tablename__ = "almacenes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    ubicacion = Column(String)

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    direccion = Column(String)

class Stock(Base):
    __tablename__ = "stock"

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String, unique=True, index=True)  # Agregar el campo "codigo"
    nombre_producto = Column(String, index=True)
    cantidad = Column(Integer)
    tipo_stock = Column(Enum('Stock1', 'Stock2'), nullable=False)
    fecha_recepcion = Column(Date)  # Agregar el campo "fecha_recepcion"
    id_almacen = Column(Integer, ForeignKey("almacenes.id"))

    # almacen = relationship("Almacen", back_populates="stock")

class Asignacion(Base):
    __tablename__ = "asignaciones"

    id = Column(Integer, primary_key=True, index=True)
    id_promotor = Column(Integer, ForeignKey("usuarios.id"))
    id_cliente = Column(Integer, ForeignKey("clientes.id"))
    id_stock = Column(Integer, ForeignKey("stock.id"))
    fecha_asignacion = Column(Date)

    # promotor = relationship("Usuario", back_populates="asignaciones_promotor")
    # cliente = relationship("Cliente", back_populates="asignaciones_cliente")
    # stock = relationship("Stock", back_populates="asignaciones")

# Usuario.asignaciones_promotor = relationship("Asignacion", back_populates="promotor")
# Cliente.asignaciones_cliente = relationship("Asignacion", back_populates="cliente")
# Stock.asignaciones = relationship("Asignacion", back_populates="stock")
