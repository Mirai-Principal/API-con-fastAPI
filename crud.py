
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

import database

import models
import esquemas

def registrar_ibo(datos: esquemas.IBOCreate, db: Session):
    query = models.IBO(
        nombre = datos.nombre,
        telefono = datos.telefono,
        email = datos.email,
        direccion = datos.direccion,
        volumen = datos.volumen,
    )
    db.add(query)
    db.commit()
    db.refresh(query)
    return query

def registrar_pedido(datos: esquemas.PedidoCreate, db: Session ):
    query = models.Pedido(
        fecha= datos.registrar_pedido,
        ibo_id= datos.registrar_pedido,
        cliente_id= datos.registrar_pedido,
        subtotal= datos.registrar_pedido,
        impuesto= datos.registrar_pedido,
        total= datos.registrar_pedido,
        metodo_pago= datos.registrar_pedido,
        numero_tarjeta= datos.registrar_pedido,
        firma= datos.registrar_pedido
    )
    db.add(query)
    db.commit()
    db.refresh(query)
    return query

def registrar_detalle_pedido(datos: esquemas.DetallePedidoCreate, db: Session ):
    query = models.DetallePedido(
        articulo = datos.articulo,
        cantidad = datos.cantidad,
        color = datos.color,
        talla = datos.talla,
        precio_unitario = datos.precio_unitario,
        precio_total = datos.precio_total
    )
    db.add(query)
    db.commit()
    db.refresh(query)
    return query

def registrar_garantia(datos: esquemas.GarantiaCreate, db: Session ):
    query = models.Garantia(
        motivo = datos.motivo,
        estatus = datos.estatus,
        fecha_proceso = datos.fecha_proceso
    )
    db.add(query)
    db.commit()
    db.refresh(query)
    return query

def registrar_cancelacion(datos: esquemas.CancelacionCreate, db: Session ):
    query = models.Cancelacion(
        fecha_cancelacion = datos.fecha_cancelacion,
        razon = datos.razon
    )
    db.add(query)
    db.commit()
    db.refresh(query)
    return query