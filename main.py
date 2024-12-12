from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import models 
import database
import esquemas
import crud


app = FastAPI()

@app.post("/registrar_ibo")
def registrar_ibo(datos: esquemas.IBO, db: Session = Depends(database.get_db)):
    return crud.registrar_ibo(datos, db)


@app.post("/registrar_pedido")
def registrar_pedido(datos: esquemas.Pedido, db: Session = Depends(database.get_db)):
    return crud.registrar_pedido(datos, db)

@app.post("/registrar_detalle_pedido")
def registrar_detalle_pedido(datos: esquemas.DetallePedido, db: Session = Depends(database.get_db)):
    return crud.registrar_detalle_pedido(datos, db)

@app.post("/registrar_garantia")
def registrar_garantia(datos: esquemas.Garantia, db: Session = Depends(database.get_db)):
    return crud.registrar_garantia(datos, db)

@app.post("/registrar_cancelacion")
def registrar_cancelacion(datos: esquemas.Cancelacion, db: Session = Depends(database.get_db)):
    return crud.registrar_cancelacion(datos, db)