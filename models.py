
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
from database import engine

# Modelo para IBO
class IBO(Base):
    __tablename__ = "ibo"

    ibo_id = Column(Integer, primary_key=True, index=True, autoincrement="auto")
    nombre = Column(String, nullable=False)
    telefono = Column(String, nullable=False)
    email = Column(String, nullable=False)
    direccion = Column(String, nullable=False)
    volumen = Column(Float, nullable=False)

    pedidos = relationship("Pedido", back_populates="ibo")

# Modelo para Cliente
class Cliente(Base):
    __tablename__ = "cliente"

    cliente_id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    direccion = Column(String, nullable=False)
    ciudad = Column(String, nullable=False)
    estado = Column(String, nullable=False)
    codigo_postal = Column(String, nullable=False)
    telefono = Column(String, nullable=False)
    email = Column(String, nullable=False)

    pedidos = relationship("Pedido", back_populates="cliente")

# Modelo para Pedido
class Pedido(Base):
    __tablename__ = "pedido"

    pedido_id = Column(Integer, primary_key=True, index=True)
    fecha = Column(DateTime, nullable=False)
    ibo_id = Column(Integer, ForeignKey("ibo.ibo_id"), nullable=False)
    cliente_id = Column(Integer, ForeignKey("cliente.cliente_id"), nullable=False)
    subtotal = Column(Float, nullable=False)
    impuesto = Column(Float, nullable=False)
    total = Column(Float, nullable=False)
    metodo_pago = Column(String, nullable=False)
    numero_tarjeta = Column(String, nullable=True)
    firma = Column(String, nullable=False)

    ibo = relationship("IBO", back_populates="pedidos")
    cliente = relationship("Cliente", back_populates="pedidos")
    detalles = relationship("DetallePedido", back_populates="pedido")
    garantias = relationship("Garantia", back_populates="pedido")
    cancelaciones = relationship("Cancelacion", back_populates="pedido")

# Modelo para DetallePedido
class DetallePedido(Base):
    __tablename__ = "detalle_pedido"

    detalle_id = Column(Integer, primary_key=True, index=True)
    pedido_id = Column(Integer, ForeignKey("pedido.pedido_id"), nullable=False)
    articulo = Column(String, nullable=False)
    cantidad = Column(Integer, nullable=False)
    color = Column(String, nullable=True)
    talla = Column(String, nullable=True)
    precio_unitario = Column(Float, nullable=False)
    precio_total = Column(Float, nullable=False)

    pedido = relationship("Pedido", back_populates="detalles")

# Modelo para Garantia
class Garantia(Base):
    __tablename__ = "garantia"

    garantia_id = Column(Integer, primary_key=True, index=True)
    pedido_id = Column(Integer, ForeignKey("pedido.pedido_id"), nullable=False)
    motivo = Column(String, nullable=False)
    estatus = Column(String, nullable=False)
    fecha_proceso = Column(DateTime, nullable=False)

    pedido = relationship("Pedido", back_populates="garantias")

# Modelo para Cancelacion
class Cancelacion(Base):
    __tablename__ = "cancelacion"

    cancelacion_id = Column(Integer, primary_key=True, index=True)
    pedido_id = Column(Integer, ForeignKey("pedido.pedido_id"), nullable=False)
    fecha_cancelacion = Column(DateTime, nullable=False)
    razon = Column(String, nullable=False)

    pedido = relationship("Pedido", back_populates="cancelaciones")


# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)