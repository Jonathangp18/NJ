from flask import Flask, render_template, request, json, url_for, redirect
from flaskext.mysql import MySQL
app = Flask(__name__)

app.config["DEBUG"] = True
app.config['MYSQL_DATABASE_USER'] = 'sepherot_jonathan'
app.config['MYSQL_DATABASE_PASSWORD'] = 'fL9WD0vDyZ'
app.config['MYSQL_DATABASE_DB'] = 'sepherot_jonathanBD'
app.config['MYSQL_DATABASE_HOST'] = 'nemonico.com.mx'
mysql = MySQL(app)

          

def insertarpostext(_nom, _cor, _eda, _dir, _car, _esc, _pro, _idi, _exp, _cur, _cel, _apt, _vac, _cv):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sqlCreateSP1="SELECT contador FROM CREATE_EMP WHERE tittle = '"+_vac+"'"
        cursor.execute(sqlCreateSP1)
        _data2 = cursor.fetchall()
        print(_data2[0][0])
        suma = str(_data2[0][0] + 1)
        print(suma)
        sqlCreateSP2="UPDATE CREATE_EMP set contador = "+suma+" WHERE tittle = '"+_vac+"'"
        cursor.execute(sqlCreateSP2)
        sqlCreateSP3="SELECT id_cemp FROM CREATE_EMP WHERE tittle = '"+_vac+"'"
        cursor.execute(sqlCreateSP3)
        _data3 = cursor.fetchall()
        id_cemp= str(_data3[0][0])
        _TABLA="POSTULANT"
        sqlCreateSP="INSERT INTO "+_TABLA+"(name, email, age, address, career, school, average, languages, experience, courses, cellphone, aptitudes, vacancy, cv) VALUES (""'"+_nom+"'"",""'"+_cor+"'"",""'"+_eda+"'"",""'"+_dir+"'"",""'"+_car+"'"",""'"+_esc+"'"",""'"+_pro+"'"",""'"+_idi+"'"",""'"+_exp+"'"",""'"+_cur+"'"",""'"+_cel+"'"",""'"+_apt+"'"",""'"+id_cemp+"'"",""'"+_cv+"'"")"
        cursor.execute(sqlCreateSP)
        data = cursor.fetchall()
        if len(data) == 0:
            conn.commit()         
            return True

        else:
            return False

    except:
        return redirect(url_for('errorr')) 
    finally:
       cursor.close() 
       conn.close()

def validar(_correoL, _contrasenaL):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        _TABLA = "USERS"
        sqlvalidarProcedure = "SELECT * FROM USERS where email= ""'"+_correoL+"'"
        sqlvalidar2Procedure = "SELECT * FROM USERS where password= ""'"+_contrasenaL+"'"
        cursor.execute(sqlvalidarProcedure)
        data = cursor.fetchall()
        cursor.execute(sqlvalidar2Procedure)
        data2 = cursor.fetchall()

        if data and data2:
             conn.commit()          
             return True

        else:
            return False

    except:
        return False 
        
    finally:
        cursor.close()
        conn.close()



def insertaruser( _nombre, _apellido, _correo, _celular, _contraseña):
    try: 
        conn = mysql.connect()
        cursor = conn.cursor()
        _TABLA="USERS"
        sqlDropProcedure="DROP PROCEDURE IF EXISTS Insertaruser;"
        cursor.execute(sqlDropProcedure)
        sqlCreateSP="CREATE PROCEDURE Insertaruser(IN name VARCHAR(60), IN last_name VARCHAR(60), IN email VARCHAR(60), IN cellphone int(100), IN password VARCHAR(60)) INSERT INTO "+_TABLA+" (name, last_name, email, cellphone, password) VALUES( ""'"+_nombre+"'""," "'"+_apellido+"'" "," "'"+_correo+ "'""," "'"+_celular+"'"","  "'"+_contraseña+ "'"")"
        cursor.execute(sqlCreateSP)
        cursor.callproc('Insertaruser',(_nombre, _apellido, _correo, _celular, _contraseña))
        data = cursor.fetchall()

        if len(data) == 0:
            conn.commit()
            return True
        else:
            return False
      

    except:
        return redirect(url_for('errorr')) 
    finally:
       cursor.close() 
       conn.close()


#PARA LA FOMRA DEL POSTULANTE
def insertarpostulante(_name, _email, _age, _address, _career, _school, _average, _languages, _experience, _courses, _cellphone, _aptitudes, _vac, _archivo):
    try:
        
        conn = mysql.connect()
        cursor = conn.cursor()
        _TABLA="POSTULANT"
        sqlCreateSP1="SELECT contador FROM CREATE_EMP WHERE tittle = '"+_vac+"'"
        cursor.execute(sqlCreateSP1)
        _data2 = cursor.fetchall()
        print(_data2[0][0])
        suma = str(_data2[0][0] + 1)
        print(suma)
        sqlCreateSP3="SELECT id_cemp FROM CREATE_EMP WHERE tittle = '"+_vac+"'"
        cursor.execute(sqlCreateSP3)
        _data3 = cursor.fetchall()
        id_cemp= str(_data3[0][0])
        sqlCreateSP2="UPDATE CREATE_EMP set contador = "+suma+" WHERE tittle = '"+_vac+"'"
        cursor.execute(sqlCreateSP2)
        sqlCreateSP="INSERT INTO "+_TABLA+"(name, email, age, address, career, school, average, languages, experience, courses, cellphone, aptitudes, vacancy, cv) VALUES (""'"+_name+"'""," "'"+_email+"'"",""'"+_age+"'"",""'"+_address+"'"",""'"+_career+"'"",""'"+_school+"'"",""'"+_average+"'"",""'"+_languages+"'"",""'"+_experience+"'"",""'"+_courses+"'"",""'"+_cellphone+"'"",""'"+_aptitudes+"'"",""'"+id_cemp+"'"",""'"+_archivo+"'"" )"
        cursor.execute(sqlCreateSP)
        data = cursor.fetchall()
        if len(data) == 0:
            conn.commit()
            return redirect(url_for('Gracias')) 
        else:
            return redirect(url_for('errorr')) 
    
    except:
        return redirect(url_for('errorr')) 
    finally:
       cursor.close() 
       conn.close()


def Insertarpostulante(_arreglo, _vac, _archivo):
    for _registro in _arreglo:
        print(insertarpostulante(_registro[0],_registro[1],_registro[2],_registro[3],_registro[4],_registro[5],_registro[6],_registro[7],_registro[8],_registro[9],_registro[10],_registro[11], _vac,_archivo))
    return True


def SelectAll(_p):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        _TABLA = "POSTULANT"
        _condicion="Registrado"
        sqlSelectAllProcedure =" SELECT p.id_post, p.name, p.email, p.age, p.address, p.career, p.school, p.average, p.languages, p.experience, p.courses, p.cellphone, p.aptitudes, c.tittle, p.estatus, p.cv, p.coments, p.compatibility FROM POSTULANT p INNER JOIN CREATE_EMP c ON p.vacancy=c.id_cemp WHERE p.vacancy = '"+_p+"' AND (p.estatus = 'Registrado' OR p.estatus = 'Entrevistado')"
        cursor.execute(sqlSelectAllProcedure)
        data = cursor.fetchall()
        return data
    except:
        return redirect(url_for('errorr')) 
    finally:
        cursor.close()
        conn.close()

def Eventocv(_archivo):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        data = _archivo
        return data 
    except:
        return redirect(url_for('errorr')) 
    finally:
        cursor.close()
        conn.close()

def Editpost(_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sqlCreateS="SELECT * FROM POSTULANT WHERE id_post = "+_id
        cursor.execute(sqlCreateS)
        data = cursor.fetchall()
        return data 
    except:
        return redirect(url_for('errorr')) 
    finally:
        cursor.close()
        conn.close()

def Recupere(_correo):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        _TABLA = "USERS"
        _condicion="Registrado"
        sqlSelectAllProcedure = "SELECT * FROM USERS WHERE email = '"+ _correo +"' "
        cursor.execute(sqlSelectAllProcedure)
        data = cursor.fetchall()
        conn.commit()
        return data
    except:
        return redirect(url_for('errorr')) 
    finally:
        cursor.close()
        conn.close()

def SelectB(_p):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        _TABLA = "POSTULANT"
        _condicion="Registrado"
        sqlSelectAllProcedure =" SELECT p.id_post, p.name, p.email, p.age, p.address, p.career, p.school, p.average, p.languages, p.experience, p.courses, p.cellphone, p.aptitudes, c.tittle, p.estatus, p.cv, p.coments, p.compatibility FROM POSTULANT p INNER JOIN CREATE_EMP c ON p.vacancy=c.id_cemp WHERE p.vacancy = '"+_p+"' AND p.estatus = 'Aceptado'"
        cursor.execute(sqlSelectAllProcedure)
        data = cursor.fetchall()     
        return data  

    except:
        return redirect(url_for('errorr')) 

    finally:
        cursor.close()
        conn.close()


def SelectC(_p):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        _TABLA = "POSTULANT"
        _condicion="Registrado"
        sqlSelectAllProcedure =" SELECT p.id_post, p.name, p.email, p.age, p.address, p.career, p.school, p.average, p.languages, p.experience, p.courses, p.cellphone, p.aptitudes, c.tittle, p.estatus, p.cv, p.coments, p.compatibility FROM POSTULANT p INNER JOIN CREATE_EMP c ON p.vacancy=c.id_cemp WHERE p.vacancy = '"+_p+"' AND p.estatus = 'Rechazado'"
        cursor.execute(sqlSelectAllProcedure)
        data = cursor.fetchall()
        return data
    except:
        return redirect(url_for('errorr')) 
    finally:
        cursor.close()
        conn.close()

def Olvidar(_correo):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        _TABLA = "POSTULANT"
        _condicion="Registrado"
        sqlSelectAllProcedure = "SELECT * FROM POSTULANT WHERE email = '"+ _correo +"' "
        cursor.execute(sqlSelectAllProcedure)
        data = cursor.fetchall()
        if len(data)==1:
            conn.commit()
            return redirect(url_for('Olvide', o=_correo))
        else:
            return redirect(url_for('errorr')) 
    except:
        return redirect(url_for('errorr')) 
    finally:
        cursor.close()
        conn.close()

def Recuperada(_correo, _contraseña):
    try:
        if _correo and _contraseña:
            conn = mysql.connect()
            cursor = conn.cursor()
            _TABLA="USERS"
            sqlCreateSP="UPDATE "+_TABLA+" SET password = '"+ _contraseña +"' WHERE email = '"+ _correo +"'"
            cursor.execute(sqlCreateSP)
            data = cursor.fetchall()

            if len(data)==0:
                return True
            else:
                return False
        else:
            return redirect(url_for('errorr')) 
    except:
        return redirect(url_for('errorr')) 
    finally:
       cursor.close() 
       conn.close()


#################################################################################################################PARA ACTUALIZAR POSTULANTE
def actualizarPostulante2(_postulante, _vac):
    try:
        if _postulante:
            conn = mysql.connect()
            cursor = conn.cursor()
            sqlCreateS="UPDATE CREATE_EMP SET estatus = 'Progreso', A_Circulo = 'circulo hecho', E_Barra = 'barra hecho', E_Circulo = 'circulo activo', A_Check = '&#10003;' WHERE id_cemp = "+_vac
            cursor.execute(sqlCreateS)
            _TABLA="POSTULANT"
            sqlCreateSP="UPDATE "+_TABLA+" SET estatus = 'Rechazado' WHERE email = '"+_postulante+"'"
            cursor.execute(sqlCreateSP)
            data = cursor.fetchall()

            if len(data)==0:
                conn.commit()
                return True
            else:
                return False
        else:
            return redirect(url_for('errorr')) 
    except:
        return redirect(url_for('errorr')) 
    finally:
       cursor.close() 
       conn.close()


def actualizarPostulante3(_id, _name, _email, _age, _address, _career, _school, _average, _languages, _experience, _courses, _cellphone, _aptitudes, _vac):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        _TABLA="POSTULANT"
        sqlCreateSP="UPDATE "+_TABLA+" Set name = '"+_name+"', email = '"+_email+"', age = "+_age+", address = '"+_address+"', career = '"+_career+"', school = '"+_school+"', average = '"+_average+"', languages = '"+_languages+"', experience = '"+_experience+"', courses = '"+_courses+"', cellphone = "+_cellphone+", aptitudes = '"+_aptitudes+"', vacancy = '"+_vac+"' WHERE id_post = "+_id
        cursor.execute(sqlCreateSP)
        data = cursor.fetchall()
        if len(data) == 0:
            conn.commit()
            return True
        else:
            return True

    except:
        return redirect(url_for('errorr')) 
    finally:
       cursor.close() 
       conn.close()



def actualizarPostulante(_postulante, _vac):
    try:
        if _postulante:
            conn = mysql.connect()
            cursor = conn.cursor()
            sqlCreateS="UPDATE CREATE_EMP SET estatus = 'Progreso', A_Circulo = 'circulo hecho', E_Barra = 'barra hecho', E_Circulo = 'circulo activo', A_Check = '&#10003;' WHERE id_cemp = "+_vac
            cursor.execute(sqlCreateS)
            _TABLA="POSTULANT"
            sqlCreateSP="UPDATE "+_TABLA+" SET estatus = 'Aceptado' WHERE email = '"+_postulante+"'"
            cursor.execute(sqlCreateSP)
            data = cursor.fetchall()

            if len(data)==0:
                conn.commit()
                return True
            else:
                return False
        else:
            return redirect(url_for('errorr')) 

    except:
        return redirect(url_for('errorr')) 
    finally:
       cursor.close() 
       conn.close()


################################################################################vacantes
def Dash():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        _TABLA = "POSTULANT"
        _condicion="Registrado"
        sqlSelectAllProcedure = "SELECT c.tittle, c.contador, c.estatus, c.A_Circulo, c.E_Barra, c.E_Circulo, c.S_Barra, c.S_Circulo, c.C_Barra, c.C_Circulo, c.A_Check, c.E_Check, c.S_Check, c.C_Check, c.id_cemp from CREATE_EMP c"
        cursor.execute(sqlSelectAllProcedure)
        data = cursor.fetchall()
        return data
    except:
        return redirect(url_for('errorr')) 
    finally:
        cursor.close()
        conn.close()

def Vacerrada(_vacante):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sqlCreateS="UPDATE CREATE_EMP SET estatus = 'cerrada', A_Circulo = 'circulo hecho', E_Barra = 'barra hecho', E_Circulo = 'circulo hecho', S_Barra = 'barra hecho', S_Circulo = 'circulo hecho', C_Barra = 'barra hecho', C_Circulo = 'circulo hecho', A_Check = '&#10003;', E_Check = '&#10003;', S_Check = '&#10003;', C_Check = '&#10003;' WHERE tittle = '"+_vacante+"'"
        cursor.execute(sqlCreateS)
        data = cursor.fetchall()
        if len(data)==0:
            return True
        else:
            return False
    except:
        return redirect(url_for('errorr')) 
    finally:
        cursor.close()
        conn.close()

def Vabierta(_vacante):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sqlCreateS="UPDATE CREATE_EMP SET estatus = 'abierta', A_Circulo = 'circulo activo', E_Barra = 'barra', E_Circulo = 'circulo', S_Barra = 'barra', S_Circulo = 'circulo', C_Barra = 'barra', C_Circulo = 'circulo', A_Check = '1', E_Check = '2', S_Check = '3', C_Check = '4' WHERE tittle = '"+_vacante+"'"
        cursor.execute(sqlCreateS)
        data = cursor.fetchall()
        if len(data)==0:
            return True
        else:
            return False
    except:
        return redirect(url_for('errorr')) 
    finally:
        cursor.close()
        conn.close()
def Editvac(_vacante, _id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sqlCreateS="UPDATE CREATE_EMP SET tittle = '"+_vacante+"' WHERE id_cemp = "+_id
        cursor.execute(sqlCreateS)
        data = cursor.fetchall()
        if len(data)==0:
            return True
        else:
            return False
    except:
        return redirect(url_for('errorr')) 
    finally:
        cursor.close()
        conn.close()

def insvacante(_emp):
    try:
        if _emp:
            conn = mysql.connect()
            cursor = conn.cursor()
            _TABLA="POSTULANT"
            sqlCreateSP="INSERT INTO CREATE_EMP (tittle, estatus) VALUES ('"+_emp+"', 'abierta')"
            cursor.execute(sqlCreateSP)
            data = cursor.fetchall()

            if len(data)==0:
                conn.commit()
                return True
            else:
                return False
        else:
            return redirect(url_for('errorr')) 

    except:
        return redirect(url_for('errorr')) 
    finally:
       cursor.close() 
       conn.close()

def openvacante():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        _TABLA = "POSTULANT"
        _condicion="Registrado"
        sqlSelectAllProcedure = "SELECT * FROM CREATE_EMP WHERE estatus = 'abierta' "
        cursor.execute(sqlSelectAllProcedure)
        data = cursor.fetchall()     
        return data  

    except:
        return redirect(url_for('errorr')) 

    finally:
        cursor.close()
        conn.close()

#################################################################################### PARA EVENTOS
def eventos(_A, _B, _C):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        _TABLA="EVENTS"
        sqlCreateS="INSERT INTO EVENTS (id_user, stage, stageinfo) VALUES (""'"+_A+"'""," "'"+_B+"'"",""'"+_C+"'"")"
        cursor.execute(sqlCreateS)
        data = cursor.fetchall()
        if len(data) == 0:
            conn.commit()    
        else:
            return redirect(url_for('errorr')) 

    except:
        return redirect(url_for('errorr')) 
    finally:
       cursor.close() 
       conn.close()

def eventos1():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sqlCreateS="INSERT INTO EVENTS (id_user, stage, stageinfo) VALUES ('1@gmail.com', 'Tabla de postulantes', 'Ver postulantes sin tratar')"
        cursor.execute(sqlCreateS)
        data = cursor.fetchall()
        if len(data) == 0:
            conn.commit()    
        else:
            return redirect(url_for('errorr')) 

    except:
        return redirect(url_for('errorr')) 
    finally:
       cursor.close() 
       conn.close()
def eventos2():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sqlCreateS="INSERT INTO EVENTS (id_user, stage, stageinfo) VALUES ('1@gmail.com', 'Tabla de postulantes1', 'Ver postulantes aceptados')"
        cursor.execute(sqlCreateS)
        data = cursor.fetchall()
        if len(data) == 0:
            conn.commit()    
        else:
            return redirect(url_for('errorr')) 

    except:
        return redirect(url_for('errorr')) 
    finally:
       cursor.close() 
       conn.close()
def eventos3():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sqlCreateS="INSERT INTO EVENTS (id_user, stage, stageinfo) VALUES ('1@gmail.com', 'Tabla de postulantes2', 'Ver postulantes rechazados')"
        cursor.execute(sqlCreateS)
        data = cursor.fetchall()
        if len(data) == 0:
            conn.commit()    
        else:
            return redirect(url_for('errorr')) 

    except:
        return redirect(url_for('errorr')) 
    finally:
       cursor.close() 
       conn.close()

def eventosR():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sqlCreateS="INSERT INTO EVENTS (id_user, stage, stageinfo) VALUES ('1@gmail.com', 'Recuperar contraseña', 'Se recuperó contraseña del usuario')"
        cursor.execute(sqlCreateS)
        data = cursor.fetchall()
        if len(data) == 0:
            conn.commit()    
        else:
            return redirect(url_for('errorr')) 

    except:
        return redirect(url_for('errorr')) 
    finally:
       cursor.close() 
       conn.close()

def eventosAC():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sqlCreateS="INSERT INTO EVENTS (id_user, stage, stageinfo) VALUES ('1@gmail.com', 'enviar correo aceptar', 'Aceptar postulante con enviar correo')"
        cursor.execute(sqlCreateS)
        data = cursor.fetchall()
        if len(data) == 0:
            conn.commit()    
        else:
            return redirect(url_for('errorr')) 

    except:
        return redirect(url_for('errorr')) 
    finally:
       cursor.close() 
       conn.close()

def eventosRE():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sqlCreateS="INSERT INTO EVENTS (id_user, stage, stageinfo) VALUES ('1@gmail.com', 'Enviar correo rechazar', 'rechazar postulante con enviar correo')"
        cursor.execute(sqlCreateS)
        data = cursor.fetchall()
        if len(data) == 0:
            conn.commit()    
        else:
            return redirect(url_for('errorr')) 

    except:
        return redirect(url_for('errorr')) 
    finally:
       cursor.close() 
       conn.close()

def eventosv():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sqlCreateS="INSERT INTO EVENTS (id_user, stage, stageinfo) VALUES ('1@gmail.com', 'Editar', 'Se editó un postulante')"
        cursor.execute(sqlCreateS)
        data = cursor.fetchall()
        if len(data) == 0:
            conn.commit()    
        else:
            return redirect(url_for('errorr')) 

    except:
        return redirect(url_for('errorr')) 
    finally:
       cursor.close() 
       conn.close()

def buscarU(_user):
    if _user:
        conn = mysql.connect()
        cursor = conn.cursor()
        query = "SELECT * FROM USERS WHERE email = '"+_user+"'"
        try: 
            cursor.execute(query,(_user))
            data = cursor.fetchall()
            if data:
                return data[0][2]
            else:
                return False
        except:
            cursor.close()
            conn.close()
            return redirect(url_for('errorr')) 
            
    else: 
            return redirect(url_for('errorr'))    

#########################################################################COMENTARIOS UPDATE
def com(_com, _comn):
    try:
        if _com and _comn:
            conn = mysql.connect()
            cursor = conn.cursor()
            _TABLA="POSTULANT"
            sqlCreateSP="UPDATE "+_TABLA+" SET coments = '"+_com+"' WHERE id_post = '"+_comn+"'"
            cursor.execute(sqlCreateSP)
            data = cursor.fetchall()
            sqla="UPDATE "+_TABLA+" SET estatus = 'Entrevistado' WHERE id_post = '"+_comn+"'"
            cursor.execute(sqla)
            dataa = cursor.fetchall()

            if len(data)==0 and len(dataa)==0 :
                conn.commit()
                return True
            else:
                return False
        else:
            return redirect(url_for('errorr')) 
    except:
        return False
    finally:
       cursor.close() 
       conn.close()

########################################################################################COGNITIVE
def cog(consultaa, _comn):
    try:
        if _comn:
            conn = mysql.connect()
            cursor = conn.cursor()
            _axx= int(consultaa * 100)
            _a=str(_axx)
            print(_axx)
            s="UPDATE POSTULANT SET compatibility = '"+_a+"'" " WHERE id_post = '"+_comn+"'"
            print(s)
            cursor.execute(s)
            data = cursor.fetchall()
            if len(data)==0:
                conn.commit()
                print("regresar un true")
                return True
            else:
                return False
        else:
            return redirect(url_for('errorr')) 
    except:
        return False
    finally:
       cursor.close() 
       conn.close()