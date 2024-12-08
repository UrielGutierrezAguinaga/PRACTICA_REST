import orm.modelos as modelos
from sqlalchemy.orm import Session
from sqlalchemy import and_

# ------------ Peticiones a usuarios ---------------------
 
 #Obtener todos los alumnos  #SELECT * FROM app.alumnos
def obtener_todos_los_alumnos(sesion: Session):
    print("select * from app.alumnos")
    return sesion.query(modelos.Alumnos).all()

#SELECT * FROM app.alumnos WHERE id={id_al} Obtener alumno por id

def obtener_alumno_por_id(sesion:Session,id_alumno:int):
    print("select * from app.alumnos where id = ", id_alumno)
    return sesion.query(modelos.Alumnos).filter(modelos.Alumnos.id==id_alumno).first()



#Obtener la calificacion por id de calificacion #SELECT * FROM app.calificacioens WHERE id={id_alumno} 
def obtener_calificacion_por_id_de_alumno(sesion: Session,id_alumno):
    print("select * from app.calificaciones where id_alumno= ",id_alumno)
    return sesion.query(modelos.Calificaciones).filter(modelos.Calificaciones.id_alumno==id_alumno).first()


#SELECT * FROM app.fotos WHERE id={id_alumno} Obtener foto por id de alumno

def obtener_foto_por_id_alumno(sesion:Session,id_alumno:int):
    print("select * from app.fotos where id_alumno = ", id_alumno)
    return sesion.query(modelos.Fotos).filter(modelos.Fotos.id_alumno==id_alumno).first()


#Obtener la calificacion por id de foto SELECT *FROM app.fotos where id={id_foto}
def obtener_foto_por_id_foto(sesion: Session,id_foto):
    print("select * from app.foto where id_foto= ",id_foto)
    return sesion.query(modelos.Fotos).filter(modelos.Fotos.id==id_foto).first()


#SELECT * FROM app.fotos WHERE id={id_al} Obtener foto por id de alumno

def obtener_calificacion_por_id_de_calificacion(sesion:Session,id_calificacion:int):
    print("select * from app.calificacion where id:calificacion = ", id_calificacion)
    return sesion.query(modelos.Calificaciones).filter(modelos.Calificaciones.id==id_calificacion).first()



 #Obtener todas los fotos SELECT * FROM app.fotos 
def obtener_todos_las_fotos(sesion: Session):
    print("select * from app.fotos")
    return sesion.query(modelos.Fotos).all()

#Obtener todas las calificaciones SELECT * FROM app.calificaciones
def obtener_todos_las_calificaciones(sesion: Session):
    print("select * from app.calificaciones")
    return sesion.query(modelos.Calificaciones).all()




# Borra fotos por id de usuario
# DELETE '/usuarios/{id}/fotos'
# delete from app.fotos where id_usuario=id
def borra_fotos_por_id(sesion:Session,id_foto:int):
    print("delete from app.fotos where id=", id_foto)
    #1.- select para ver si existe el usuario a borrar
    foto_usr = obtener_foto_por_id_alumno(sesion, id_foto)
    print(foto_usr)
    #2.- Borramos
    if foto_usr is not None:
        #Borramos usuario
        sesion.delete(foto_usr)
        #Confirmar los cambios
        sesion.commit()
    respuesta = {
        "mensaje": "foto eliminada"
    }
    return respuesta



def borra_calificaciones_por_id(sesion:Session,id_foto:int):
    print("delete from app.calificacion where id=", id_foto)
    #1.- select para ver si existe el usuario a borrar
    calif_usr = obtener_calificacion_por_id_de_calificacion(sesion, id_foto)
    print(calif_usr)
    #2.- Borramos
    if calif_usr is not None:
        #Borramos usuario
        sesion.delete(calif_usr)
        #Confirmar los cambios
        sesion.commit()
    respuesta = {
        "mensaje": "calificacion eliminada"
    }
    return respuesta


def borrar_calificaciones_por_id_alumno(sesion:Session,id_alumno:int):
    print("delete from app.calificacion where id_alumno=", id_alumno)
    #1.- select para ver si existe el usuario a borrar
    calif_usr = obtener_calificacion_por_id_de_alumno(sesion, id_alumno)
    print(calif_usr)
    #2.- Borramos
    if calif_usr is not None:
        #Borramos usuario
       sesion.delete(calif_usr)
        #Confirmar los cambios
       sesion.commit()
    respuesta = {
        "mensaje": "calificacion eliminada"
    }
    return respuesta

def borrar_fotos_por_id_alumno(sesion:Session,id_alumno:int):
    print("delete from app.foto where id_alumno=", id_alumno)
    #1.- select para ver si existe el usuario a borrar
    calif_usr = obtener_foto_por_id_alumno(sesion, id_alumno)
    print(calif_usr)
    #2.- Borramos
    if calif_usr is not None:
        #Borramos usuario
       sesion.delete(calif_usr)
        #Confirmar los cambios
       sesion.commit()
    respuesta = {
        "mensaje": "foto eliminada"
    }
    return respuesta


def borrar_alumno_por_id(sesion:Session,id_alumno:int):
    print("delete from app.alumno where id_alumno=", id_alumno)
    #1.- select para ver si existe el usuario a borrar
    _usr = obtener_alumno_por_id(sesion, id_alumno)
    
    #2.- Borramos
    if _usr is not None:
        #Borramos usuario
       sesion.delete(_usr)
        #Confirmar los cambios
       sesion.commit()
    respuesta = {
        "mensaje": "usuario eliminado"
    }
    return respuesta
