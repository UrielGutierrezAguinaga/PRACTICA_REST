from orm import esquemas
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

#POST '/usuarios' PRACTICA 2

def guardar_alumno(sesion:Session, almn_nuevo:esquemas.AlumnoBase):
    #1.- Crear un nuevo objeto de la clase modelo Usuario
    almn_bd = modelos.Alumnos()
    #2.- Llenamos el nuevo objeto con los parámetros que nos paso el usuario
    almn_bd.nombre = almn_nuevo.nombre
    almn_bd.edad = almn_nuevo.edad
    almn_bd.domicilio = almn_nuevo.domicilio
    almn_bd.email = almn_nuevo.email
    almn_bd.carrera = almn_nuevo.carrera
    almn_bd.trimestre = almn_nuevo.trimestre
    almn_bd.password = almn_nuevo.password
    #3.- Insertar el nuevo objeto a la BD
    sesion.add(almn_bd)
    #4.- Confirmamos el cambio
    sesion.commit()
    #5.- Hacemos un refresh e imprimimos
    print(almn_bd)
    sesion.refresh(almn_bd)
    return almn_bd


#PUT '/alumnos/{id}'
# UPDATE app.alumnos
# SET alumno=almn_esquema.nombre, edad=almn_esquema.edad, 
# domicilio=almn_esquema.domicilio, email=almn_esquema.email,
# password=almn_esquema.password
# WHERE id = id_
def actualiza_alumno(sesion:Session,id_alumno:int,almn_esquema:esquemas.AlumnoBase):
    #1.-Verificar que el usuario existe
    almn_bd = obtener_alumno_por_id(sesion,id_alumno)
    if almn_bd is not None:
        #2.- Actualizamos los datos del usuaurio en la BD
        almn_bd.nombre = almn_esquema.nombre
        almn_bd.edad = almn_esquema.edad
        almn_bd.domicilio = almn_esquema.domicilio
        almn_bd.email = almn_esquema.email
        almn_bd.password = almn_esquema.password
        almn_bd.carrera = almn_esquema.carrera
        almn_bd.trimestre = almn_esquema.trimestre
        
        #3.-Confirmamos los cambios
        sesion.commit()
        #4.-Refrescar la BD
        sesion.refresh(almn_bd)
        #5.-Imprimir los datos nuevos
        print(almn_esquema)
        return almn_esquema
    else:
        respuesta = {"mensaje":"No existe registro en BD"}
        return respuesta
    

def guardar_calificacion_id_alumno(sesion:Session, id_almn:int, almn_nuevo:esquemas.CalificacionesBase):
    #1.-Verificar que el usuario existe
    calif_bd = obtener_calificacion_por_id_de_alumno(sesion,id_almn)
    if calif_bd is not None:
        #2.- Creamos un nuevo objeto en compra
        calif_bd = modelos.Calificaciones()
        #3.-actualizamos el objeto
        calif_bd.id_alumno = id_almn
        calif_bd.uea = almn_nuevo.uea
        calif_bd.calificacion= almn_nuevo.calificacion
        #4.-agregamos a bd
        sesion.refresh(calif_bd)
        #5.-hacemos la actualización
        sesion.commit()
        #6.-Refrescar la BD
        sesion.refresh(calif_bd)
        #6.-Imprimir los datos nuevos
        print(calif_bd)
        return calif_bd
    else:
        respuesta = {"mensaje":"No existe registro en BD"}
        return respuesta
    


# put("/calificaciones/{id}")
def   actualizar_calificacion_calificacion_id(sesion:Session,id_calif:int,almn_esquema:esquemas.CalificacionesBase):
    #1.-Verificar que el usuario existe
    almn_bd = obtener_calificacion_por_id_de_calificacion(sesion,id_calif)
    if almn_bd is not None:
        #2.- Actualizamos los datos del usuaurio en la BD
        almn_bd.uea = almn_esquema.uea
        almn_bd.calificacion = almn_esquema.calificacion
        #3.-Confirmamos los cambios
        sesion.commit()
        #4.-Refrescar la BD
        sesion.refresh(almn_bd)
        #5.-Imprimir los datos nuevos
        print(almn_esquema)
        return almn_esquema
    else:
        respuesta = {"mensaje":"No existe registro en BD"}
        return respuesta


# post("/alumnos/{id}/fotos")
def guardar_foto_alumno_id(sesion:Session, id_alumno:int, almn_nuevo:esquemas.FotosBase):
    almn_bd = obtener_alumno_por_id(sesion,id_alumno)
    if almn_bd is not None:
        #1.- Crear un nuevo objeto de la clase modelo Compra
        almn_bd = modelos.Fotos()
        #2.- Llenamos el nuevo objeto con los parámetros que nos paso el usuario
        almn_bd.titulo = almn_nuevo.titulo
        almn_bd.descripcion = almn_nuevo.descripcion
        almn_bd.id_alumno = id_alumno
        #3.- Insertar el nuevo objeto a la BD
        sesion.add(almn_bd)
        #4.- Confirmamos el cambio
        sesion.commit()
        #5.- Hacemos un refresh e imprimimos
        print(almn_bd)
        sesion.refresh(almn_bd)
        return almn_bd
    else:
        respuesta = {"mensaje":"No existe registro en BD"}
        return respuesta
    
    
    # put("/fotos/{id}")
def actualizar_foto_por_id(sesion:Session,id_foto:int,almn_esquema:esquemas.FotosBase):
    #1.-Verificar que el usuario existe
    almn_bd = obtener_foto_por_id_foto(sesion,id_foto)
    if almn_bd is not None:
        #2.- Actualizamos los datos del usuaurio en la BD
        almn_bd.titulo = almn_esquema.titulo
        almn_bd.descripcion = almn_esquema.descripcion
        #3.-Confirmamos los cambios
        sesion.commit()
        #4.-Refrescar la BD
        sesion.refresh(almn_bd)
        #5.-Imprimir los datos nuevos
        print(almn_esquema)
        return almn_esquema
    else:
        respuesta = {"mensaje":"No existe registro en BD"}
        return respuesta