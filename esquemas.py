from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# Esquema para IBO
class IBOBase(BaseModel):
    nombre: str
    telefono: str
    email: str
    direccion: str
    volumen: float

class IBOCreate(IBOBase):
    pass

class IBO(IBOBase):
    ibo_id: int

    class Config:
        from_attributes = True
# Esquema para Cliente
class ClienteBase(BaseModel):
    nombre: str
    direccion: str
    ciudad: str
    estado: str
    codigo_postal: str
    telefono: str
    email: str

class ClienteCreate(ClienteBase):
    pass

class Cliente(ClienteBase):
    cliente_id: int

    class Config:
        orm_mode = True

# Esquema para Pedido
class PedidoBase(BaseModel):
    fecha: datetime
    ibo_id: int
    cliente_id: int
    subtotal: float
    impuesto: float
    total: float
    metodo_pago: str
    numero_tarjeta: Optional[str]
    firma: str

class PedidoCreate(PedidoBase):
    pass

class Pedido(PedidoBase):
    pedido_id: int

    class Config:
        from_attributes = True

# Esquema para DetallePedido
class DetallePedidoBase(BaseModel):
    articulo: str
    cantidad: int
    color: Optional[str]
    talla: Optional[str]
    precio_unitario: float
    precio_total: float

class DetallePedidoCreate(DetallePedidoBase):
    pedido_id: int

class DetallePedido(DetallePedidoBase):
    detalle_id: int
    pedido_id: int

    class Config:
        from_attributes = True

# Esquema para Garantia
class GarantiaBase(BaseModel):
    motivo: str
    estatus: str
    fecha_proceso: datetime

class GarantiaCreate(GarantiaBase):
    pedido_id: int

class Garantia(GarantiaBase):
    garantia_id: int
    pedido_id: int

    class Config:
        from_attributes = True

# Esquema para Cancelacion
class CancelacionBase(BaseModel):
    fecha_cancelacion: datetime
    razon: str

class CancelacionCreate(CancelacionBase):
    pedido_id: int

class Cancelacion(CancelacionBase):
    cancelacion_id: int
    pedido_id: int

    class Config:
        from_attributes = True
