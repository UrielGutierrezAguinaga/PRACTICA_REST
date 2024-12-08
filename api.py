from fastapi import FastAPI, UploadFile, File, Form, Depends
from typing import Optional
from pydantic import BaseModel
import shutil
import os
import uuid
import orm.repo as repo #funciones para hacer consultas a la BD
from sqlalchemy.orm import Session
from orm.config import generador_sesion #generador de sesiones

# creación del servidor
app = FastAPI()

#definición de la base del alumno
class UsuarioBase(BaseModel):
    nombre:Optional[str]=None
    edad:int
    domicilio:str
    carrera:str   
    trimestre:str


 

  
# decorator
@app.get("/")
def hola_mundo():
    print("invocando a ruta /")
    respuesta = {
        "mensaje": "hola mundo!"
    }

    return respuesta


@app.get("/alumnos")
def obtener_todos_los_alumnos(sesion: Session = Depends(generador_sesion)):
    print("API consultando todos los alumnos")
    alumnos = repo.obtener_todos_los_alumnos(sesion)  # Aquí se pasa la sesión
    return alumnos

@app.get("/alumnos/{id}")
def obtener_alumno_por_id(id:int, sesion: Session = Depends(generador_sesion)):
    print("API consultando alumno por id", id)
    alumno = repo.obtener_alumno_por_id(sesion, id)  # Aquí se pasa la sesión
     
    return alumno


@app.get("/alumno/{id}/calificacion")
def obtener_calificacion_por_id_de_alumno(id:int, sesion: Session = Depends(generador_sesion)):
    print("API consultando foto por id de alumno", id)
    calificacion = repo.obtener_calificacion_por_id_de_alumno(sesion, id)  # Aquí se pasa la sesión
     
    return calificacion

@app.get("/alumno/{id}/fotos")
def obtener_foto_por_id_alumno(id:int, sesion: Session = Depends(generador_sesion)):
    print("API consultando foto por id de alumno", id)
    foto = repo.obtener_foto_por_id_alumno(sesion, id)  # Aquí se pasa la sesión
     
    return foto

@app.get("/fotos/{id}")
def obtener_foto_por_id_foto(id:int, sesion: Session = Depends(generador_sesion)):
    print("API consultando foto por id de foto", id)
    foto = repo.obtener_foto_por_id_foto(sesion, id)  # Aquí se pasa la sesión
    
    return foto

@app.get("/calificaciones/{id_calificacion}")
def obtener_calificacion_por_id_de_calificacion(id_calificacion:int, sesion: Session = Depends(generador_sesion)):
    print("API consultando foto por id de alumno", id_calificacion)
    calificacion = repo.obtener_calificacion_por_id_de_calificacion(sesion, id_calificacion)  # Aquí se pasa la sesión
     
    return calificacion

@app.get("/fotos")
def obtener_todos_los_alumnos(sesion: Session = Depends(generador_sesion)):
    print("API consultando todas las fotos")
    fotos = repo.obtener_todos_las_fotos(sesion)  # Aquí se pasa la sesión
     
    return fotos

@app.get("/calificaciones")
def obtener_todos_las_calificaciones(sesion: Session = Depends(generador_sesion)):
    print("API consultando todas las calificaciones")
    calificaciones = repo.obtener_todos_las_calificaciones(sesion)  # Aquí se pasa la sesión
     
    return calificaciones


#Hasta aqui terminan las peticiones del tipo Get

@app.delete("/fotos/{id}")
def borrar_fotos(id:int, sesion:Session=Depends(generador_sesion)):
    repo.borra_fotos_por_id(sesion,id)
    return {"foto_borrada", "ok"}

@app.delete("/calificaciones/{id}")
def borrar_calificaciones(id:int, sesion:Session=Depends(generador_sesion)):
    repo.borra_calificaciones_por_id(sesion,id)
    return {"calificacion_borrada", "ok"}

@app.delete("/alumnos/{id}/calificaciones/")
def borrar_calificaciones(id:int, sesion:Session=Depends(generador_sesion)):
    repo.borrar_calificaciones_por_id_alumno(sesion,id)
    return {"calificacion_borrada", "ok"}


@app.delete("/alumnos/{id}/fotos/")
def borrar_fotos(id:int, sesion:Session=Depends(generador_sesion)):
    repo.borrar_fotos_por_id_alumno(sesion,id)
    return {"foto_borrada", "ok"}

@app.delete("/alumnos/{id}")
def borrar_fotos(id:int, sesion:Session=Depends(generador_sesion)):
    repo.borra_fotos_por_id(sesion,id)
    repo.borrar_calificaciones_por_id_alumno(sesion,id)
    repo.borrar_alumno_por_id(sesion,id)
    return {"alumno_borrado", "ok"}




 


