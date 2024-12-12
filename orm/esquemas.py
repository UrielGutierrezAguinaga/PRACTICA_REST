from pydantic import BaseModel
from typing import Optional
#Definir el esquema alumno
class AlumnoBase(BaseModel):
    nombre:str
    edad:int
    domicilio:str
    email:str
    carrera:str
    trimestre:str
    password:str

#Definir el esquema Fotos
class FotosBase(BaseModel):
    titulo:str
    descripcion:str
#Definir el esquema Calificaciones
class CalificacionesBase(BaseModel):
    uea:str
    calificacion:str
