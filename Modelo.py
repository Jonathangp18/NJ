from flask import Flask, render_template, request, json, url_for, redirect
from flaskext.mysql import MySQL
import hashlib
import random
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
        sqlCreateSP2="UPDATE CREATE_EMP set contador = "+suma+", c_registrados = "+suma+" WHERE tittle = '"+_vac+"'"
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
        sqlvalidarProcedure = "SELECT email FROM USERS where email= ""'"+_correoL+"'"
        cursor.execute(sqlvalidarProcedure)
        data = cursor.fetchall()
        sqlvalidar2Procedure = "SELECT password FROM USERS where email= ""'"+_correoL+"'"
        cursor.execute(sqlvalidar2Procedure)
        data2 = cursor.fetchall()
        sqlvalidar3Procedure = "SELECT SALT FROM USERS where email=  ""'"+_correoL+"'"
        cursor.execute(sqlvalidar3Procedure)
        data3 = cursor.fetchall()
        print(data2)
        data2=str(data2)
        print(data3)
        data3=str(data3)

        data33=(data3[3][0]+data3[4][0]+data3[5][0]+data3[6][0]+data3[7][0]+data3[8][0]+data3[9][0]+data3[10][0]+data3[11][0]+data3[12][0])
        print(data33)



        print("antes del hash")
        contraseña_cifrada = hashlib.sha512(_contrasenaL.encode())
        print("despues del hash")
        salt=(data33)
        print(salt)
        contraseña=("(('"+contraseña_cifrada.hexdigest()+salt)
        print("Su contraseña cifrada1 es:")
        print(contraseña)
        print(salt)


        if data and (data2==contraseña):
             conn.commit()   
             sqlCreatedos="SELECT sessions FROM USERS WHERE email=""'"+_correoL+"'"
             cursor.execute(sqlCreatedos)
             datados = cursor.fetchall()
             suma=str(datados)
             sumaa=(suma[2][0])
             dos=int(sumaa)
             doss=str(dos + 1)
             print(doss)
             sumaqry="UPDATE USERS SET sessions ='"+doss+"'WHERE email = '"+_correoL+"'"   
             print(sumaqry)
             cursor.execute(sumaqry)
             dat = cursor.fetchall() 

             return True

        else:
            return False

    except:
        return redirect(url_for('errorr')) 
        
    finally:
        cursor.close()
        conn.close()



def insertaruser( _nombre, _apellido, _correo, _celular, _contraseña):
    try: 
        conn = mysql.connect()
        cursor = conn.cursor()
        _TABLA="USERS"

        contraseña_cifrada = hashlib.sha512(_contraseña.encode())
        print("ya hizo el hash")
        _salt=str(random.randrange(10000, 99999))
        _contraseña=(contraseña_cifrada.hexdigest()+_salt)
        
        sqlDropProcedure="DROP PROCEDURE IF EXISTS Insertaruser;"
        cursor.execute(sqlDropProcedure)
        sqlCreateSP="CREATE PROCEDURE Insertaruser(IN name VARCHAR(60), IN last_name VARCHAR(60), IN email VARCHAR(60), IN cellphone int(100), IN password VARCHAR(400),IN SALT VARCHAR(100), IN sessions int(100)) INSERT INTO "+_TABLA+" (name, last_name, email, cellphone, password, SALT, sessions) VALUES( ""'"+_nombre+"'""," "'"+_apellido+"'" "," "'"+_correo+ "'""," "'"+_celular+"'"","  "'"+_contraseña+ "'"","  "'"+_salt+ "'"", 1)"
        print(sqlCreateSP)
        cursor.execute(sqlCreateSP)
        cursor.callproc('Insertaruser',(_nombre, _apellido, _correo, _celular, _contraseña, _salt, "1"))
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
        suma2 = suma
        print(suma)
        sqlCreateSP3="SELECT id_cemp FROM CREATE_EMP WHERE tittle = '"+_vac+"'"
        cursor.execute(sqlCreateSP3)
        _data3 = cursor.fetchall()
        id_cemp= str(_data3[0][0])
        sqlCreateSP2="UPDATE CREATE_EMP set contador = "+suma+", c_registrados = "+suma2+" WHERE tittle = '"+_vac+"'"
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
        print(insertarpostulante(_registro[0].strip(), _registro[1].strip(), _registro[2].strip(), _registro[3].strip(), _registro[4].strip(), _registro[5].strip(), _registro[6].strip(), _registro[7].strip(), _registro[8].strip(), _registro[9].strip(), _registro[10].strip(), _registro[11].strip(), _vac.strip(),_archivo))
    return True


def SelectAll(_p):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        _TABLA = "POSTULANT"
        _condicion="Registrado"
        sqlSelectAllProcedure =" SELECT p.id_post, p.name, p.email, p.age, p.address, p.career, p.school, p.average, p.languages, p.experience, p.courses, p.cellphone, p.aptitudes, c.tittle, p.estatus, p.cv, p.coments, p.compatibility, p.wordskey FROM POSTULANT p INNER JOIN CREATE_EMP c ON p.vacancy=c.id_cemp WHERE p.vacancy = '"+_p+"' AND (p.estatus = 'Registrado' OR p.estatus = 'Entrevistado')"
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
def actualizarPostulante2(_postulante, _vac, _user, _just):
    try:
        if _postulante:
            conn = mysql.connect()
            cursor = conn.cursor()
            sqli="SELECT Answered, Total FROM USERS WHERE email = '"+_user+"'"
            cursor.execute(sqli)
            Answered = cursor.fetchall()
            Answ = str(Answered[0][0] + 1)
            total = str(Answered[0][1] + 1)
            sqlint="UPDATE USERS SET Answered = "+Answ+", Total = "+total+" WHERE email = '"+_user+"'"
            cursor.execute(sqlint)
            sqls="SELECT c_entrevistados, c_rechazados FROM CREATE_EMP WHERE id_cemp = '"+_vac+"'"
            cursor.execute(sqls)
            rech = cursor.fetchall()
            print(rech[0][0])
            print(rech[0][1])
            reg= str(rech[0][0]-1)
            rec= str(rech[0][1]+1)
            sqlCreateSC="UPDATE CREATE_EMP SET c_entrevistados = "+reg+", c_rechazados = "+rec+"  WHERE id_cemp = '"+_vac+"'"
            cursor.execute(sqlCreateSC)
            sqlCreateS="UPDATE CREATE_EMP SET estatus = 'Progreso', A_Circulo = 'circulo hecho', E_Barra = 'barra hecho', E_Circulo = 'circulo activo', A_Check = '&#10003;' WHERE id_cemp = "+_vac
            cursor.execute(sqlCreateS)
            _TABLA="POSTULANT"
            sqlCreateSP="UPDATE "+_TABLA+" SET estatus = 'Rechazado', justification = '"+_just+"' WHERE email = '"+_postulante+"'"
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

def actualizarPostulante4(_postulante, _vac, _user, _just):
    try:
        if _postulante:
            conn = mysql.connect()
            cursor = conn.cursor()
            sqli="SELECT Answered, Total FROM USERS WHERE email = '"+_user+"'"
            cursor.execute(sqli)
            Answered = cursor.fetchall()
            Answ = str(Answered[0][0] + 1)
            total = str(Answered[0][1] + 1)
            sqlint="UPDATE USERS SET Answered = "+Answ+", Total = "+total+" WHERE email = '"+_user+"'"
            cursor.execute(sqlint)
            sqls="SELECT c_aceptados, c_rechazados FROM CREATE_EMP WHERE id_cemp = '"+_vac+"'"
            cursor.execute(sqls)
            rech = cursor.fetchall()
            print(rech[0][0])
            print(rech[0][1])
            reg= str(rech[0][0]-1)
            rec= str(rech[0][1]+1)
            sqlCreateSC="UPDATE CREATE_EMP SET c_aceptados = "+reg+", c_rechazados = "+rec+"  WHERE id_cemp = '"+_vac+"'"
            cursor.execute(sqlCreateSC)
            sqlCreateS="UPDATE CREATE_EMP SET estatus = 'Progreso', A_Circulo = 'circulo hecho', E_Barra = 'barra hecho', E_Circulo = 'circulo activo', A_Check = '&#10003;' WHERE id_cemp = "+_vac
            cursor.execute(sqlCreateS)
            _TABLA="POSTULANT"
            sqlCreateSP="UPDATE "+_TABLA+" SET estatus = 'Rechazado', justification = '"+_just+"' WHERE email = '"+_postulante+"'"
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



def actualizarPostulante(_postulante, _vac, _user, _salary, _date):
    try:
        if _postulante:
            conn = mysql.connect()
            cursor = conn.cursor()
            sqli="SELECT Answered, Total FROM USERS WHERE email = '"+_user+"'"
            cursor.execute(sqli)
            Answered = cursor.fetchall()
            print(Answered[0][0])
            print(Answered[0][1])
            Answ = str(Answered[0][0] + 1)
            print(Answ)
            total = str(Answered[0][1] + 1)
            sqlint="UPDATE USERS SET Answered = "+Answ+", Total = "+total+" WHERE email = '"+_user+"'"
            cursor.execute(sqlint)

            sqls="SELECT c_entrevistados, c_aceptados FROM CREATE_EMP WHERE id_cemp = '"+_vac+"'"
            cursor.execute(sqls)
            acep = cursor.fetchall()
            print(acep[0][0])
            print(acep[0][1])
            reg= str(acep[0][0]-1)
            ace= str(acep[0][1]+1)
            sqlCreateSC="UPDATE CREATE_EMP SET c_entrevistados = "+reg+", c_aceptados = "+ace+"  WHERE id_cemp = '"+_vac+"'"
            cursor.execute(sqlCreateSC)

            sqlCreateS="UPDATE CREATE_EMP SET estatus = 'Progreso', A_Circulo = 'circulo hecho', E_Barra = 'barra hecho', E_Circulo = 'circulo activo', A_Check = '&#10003;' WHERE id_cemp = "+_vac
            cursor.execute(sqlCreateS)
            _TABLA="POSTULANT"
            sqlCreateSP="UPDATE "+_TABLA+" SET estatus = 'Aceptado', salary ="+_salary+", signature_date= '"+_date+"' WHERE email = '"+_postulante+"'"
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

def actualizarPostulante1(_postulante, _vac, _user, _salary, _date):
    try:
        if _postulante:
            conn = mysql.connect()
            cursor = conn.cursor()
            sqli="SELECT Answered, Total FROM USERS WHERE email = '"+_user+"'"
            cursor.execute(sqli)
            Answered = cursor.fetchall()
            print(Answered[0][0])
            print(Answered[0][1])
            Answ = str(Answered[0][0] + 1)
            print(Answ)
            total = str(Answered[0][1] + 1)
            sqlint="UPDATE USERS SET Answered = "+Answ+", Total = "+total+" WHERE email = '"+_user+"'"
            cursor.execute(sqlint)

            sqls="SELECT c_rechazados, c_aceptados FROM CREATE_EMP WHERE id_cemp = '"+_vac+"'"
            cursor.execute(sqls)
            acep = cursor.fetchall()
            print(acep[0][0])
            print(acep[0][1])
            reg= str(acep[0][0]-1)
            ace= str(acep[0][1]+1)
            sqlCreateSC="UPDATE CREATE_EMP SET c_rechazados = "+reg+", c_aceptados = "+ace+"  WHERE id_cemp = '"+_vac+"'"
            cursor.execute(sqlCreateSC)

            sqlCreateS="UPDATE CREATE_EMP SET estatus = 'Progreso', A_Circulo = 'circulo hecho', E_Barra = 'barra hecho', E_Circulo = 'circulo activo', A_Check = '&#10003;' WHERE id_cemp = "+_vac
            cursor.execute(sqlCreateS)
            _TABLA="POSTULANT"
            sqlCreateSP="UPDATE "+_TABLA+" SET estatus = 'Aceptado', salary ="+_salary+", signature_date= '"+_date+"' WHERE email = '"+_postulante+"'"
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
        sqlSelectAllProcedure = "SELECT c.tittle, c.contador, c.estatus, c.A_Circulo, c.E_Barra, c.E_Circulo, c.S_Barra, c.S_Circulo, c.C_Barra, c.C_Circulo, c.A_Check, c.E_Check, c.S_Check, c.C_Check, c.id_cemp, c.c_registrados, c.c_entrevistados, c.c_aceptados, c.c_rechazados from CREATE_EMP c"
        cursor.execute(sqlSelectAllProcedure)
        data = cursor.fetchall()
        return data
    except:
        return redirect(url_for('errorr')) 
    finally:
        cursor.close()
        conn.close()

def SumaTotal():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        _TABLA = "POSTULANT"
        _condicion="Registrado"
        sqlSelectAllProcedure = "SELECT sum(contador), sum(c_registrados), sum(c_entrevistados), sum(c_aceptados), sum(c_rechazados) from CREATE_EMP"
        cursor.execute(sqlSelectAllProcedure)
        data = cursor.fetchall()
        return data
    except:
        return redirect(url_for('errorr')) 
    finally:
        cursor.close()
        conn.close()

def VacTotal(_vac):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        _TABLA = "POSTULANT"
        _condicion="Registrado"
        sqlSelectAllProcedure = "SELECT sum(contador), sum(c_registrados), sum(c_entrevistados), sum(c_aceptados), sum(c_rechazados) from CREATE_EMP WHERE id_cemp = "+_vac
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
        sqlCreateS="UPDATE CREATE_EMP SET estatus = 'abierta', A_Circulo = 'circulo activo', E_Barra = 'barra', E_Circulo = 'circulo', S_Barra = 'barra', S_Circulo = 'circulo', C_Barra = 'barra', C_Circulo = 'circulo', A_Check = '1', E_Check = '2', S_Check = '3', C_Check = '3' WHERE tittle = '"+_vacante+"'"
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
        _A=_A
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

def eventos1(nombre1):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sqlCreateS="INSERT INTO EVENTS (id_user, stage, stageinfo) VALUES ('"+nombre1+"', 'Tabla de postulantes', 'Ver postulantes sin tratar')"
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
def eventos2(nombre1):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sqlCreateS="INSERT INTO EVENTS (id_user, stage, stageinfo) VALUES ('"+nombre1+"', 'Tabla de postulantes1', 'Ver postulantes aceptados')"
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
def eventos3(nombre1):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sqlCreateS="INSERT INTO EVENTS (id_user, stage, stageinfo) VALUES ('"+nombre1+"', 'Tabla de postulantes2', 'Ver postulantes rechazados')"
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

def eventosR(nombre1):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sqlCreateS="INSERT INTO EVENTS (id_user, stage, stageinfo) VALUES ('"+nombre1+"', 'Recuperar contraseña', 'Se recuperó contraseña del usuario')"
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

def eventosAC(nombre1):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sqlCreateS="INSERT INTO EVENTS (id_user, stage, stageinfo) VALUES ('"+nombre1+"', 'enviar correo aceptar', 'Aceptar postulante con enviar correo')"
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

def eventosRE(nombre1):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sqlCreateS="INSERT INTO EVENTS (id_user, stage, stageinfo) VALUES ('"+nombre1+"', 'Enviar correo rechazar', 'rechazar postulante con enviar correo')"
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

def eventosv(nombre1):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sqlCreateS="INSERT INTO EVENTS (id_user, stage, stageinfo) VALUES ('"+nombre1+"', 'Editar', 'Se editó un postulante')"
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

def eventoserror(nombre1):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sqlCreateS="INSERT INTO EVENTS (id_user, stage, stageinfo) VALUES ('"+nombre1+"', 'Error 404', 'La página falló')"
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

def eventosinsertvac(nombre1):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sqlCreateS="INSERT INTO EVENTS (id_user, stage, stageinfo) VALUES ('"+nombre1+"', 'Se insertó una vacante ', 'se creó una nueva vacante')"
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

def eventoscervac(nombre1):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sqlCreateS="INSERT INTO EVENTS (id_user, stage, stageinfo) VALUES ('"+nombre1+"', 'Se cerró una vacante ', 'se cerró una vacante')"
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

def eventosabrvac(nombre1):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sqlCreateS="INSERT INTO EVENTS (id_user, stage, stageinfo) VALUES ('"+nombre1+"', 'Se abrió una vacante ', 'se abrió una vacante')"
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

def eventosedivac(nombre1):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        print("entro al sql")
        print(nombre1)
        sqlCreateS="INSERT INTO EVENTS (id_user, stage, stageinfo) VALUES ('"+nombre1+"', 'Se editó una vacante ', 'se editó una nueva vacante')"
        cursor.execute(sqlCreateS)
        print(sqlCreateS)
        data = cursor.fetchall()
        if len(data) == 0:
            conn.commit()  
            return True  
        else:
            return redirect(url_for('errorr')) 

    except:
        return redirect(url_for('errorr')) 
    finally:
       cursor.close() 
       conn.close()

def eventoscom(nombre1):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sqlCreateS="INSERT INTO EVENTS (id_user, stage, stageinfo) VALUES ('"+nombre1+"', 'Se insertó un comentario ', 'se insertó un comentario')"
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
def com(_com, _comn, _user, _vac):
    try:
        if _com and _comn:
            conn = mysql.connect()
            cursor = conn.cursor()
            _TABLA="POSTULANT"
            sqli="SELECT Interviewed, Total FROM USERS WHERE email = '"+_user+"'"
            cursor.execute(sqli)
            interviewed = cursor.fetchall()
            print(interviewed[0][0])
            print(interviewed[0][1])
            inter = str(interviewed[0][0] + 1)
            total = str(interviewed[0][1] + 1)
            sqlint="UPDATE USERS SET Interviewed = "+inter+", Total = "+total+" WHERE email = '"+_user+"'"
            cursor.execute(sqlint)

            sqls="SELECT c_registrados, c_entrevistados FROM CREATE_EMP WHERE id_cemp = '"+_vac+"'"
            cursor.execute(sqls)
            entre = cursor.fetchall()
            print(entre[0][0])
            print(entre[0][1])
            reg= str(entre[0][0]-1)
            entr= str(entre[0][1]+1)
            sqlCreateSC="UPDATE CREATE_EMP SET c_registrados = "+reg+", c_entrevistados = "+entr+"  WHERE id_cemp = '"+_vac+"'"
            cursor.execute(sqlCreateSC)

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

def comn(_com, _comn, _user, _vac):
    try:
        if _com and _comn:
            conn = mysql.connect()
            cursor = conn.cursor()
            _TABLA="POSTULANT"
            sqli="SELECT Interviewed, Total FROM USERS WHERE email = '"+_user+"'"
            cursor.execute(sqli)
            interviewed = cursor.fetchall()
            print(interviewed[0][0])
            print(interviewed[0][1])
            inter = str(interviewed[0][0] + 1)
            total = str(interviewed[0][1] + 1)
            sqlint="UPDATE USERS SET Interviewed = "+inter+", Total = "+total+" WHERE email = '"+_user+"'"
            cursor.execute(sqlint)

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
def cog(axx, w, _comn):
    try:
        if _comn:
            conn = mysql.connect()
            cursor = conn.cursor()
            print("entro al sql")

            _axx= int(axx * 100)

            _a=str(_axx)
            _w=str(w)

            print(_a)
            print(_w)


            s="UPDATE POSTULANT SET compatibility = '"+_a+"' WHERE id_post = '"+_comn+"'"
            print(s)
            cursor.execute(s)
            data1 = cursor.fetchall()
            conn.commit()

            print("debe hacer el sql de busqueda")
            s1="UPDATE POSTULANT SET wordskey ='"+_w+"' WHERE id_post = '"+_comn+"'"
            print(s1)
            cursor.execute(s1)
            data = cursor.fetchall()
            conn.commit()

            #s1="UPDATE POSTULANT SET negative = '"+_a1+"' WHERE id_post = '"+_comn+"'"
           # print(s1)
          #  cursor.execute(s1)
          #  data = cursor.fetchall()

           # s2="UPDATE POSTULANT SET neutro = '"+_a2+"' WHERE id_post = '"+_comn+"'"
           # print(s2)
           # cursor.execute(s2)
           # data = cursor.fetchall()


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

################################################################# Ranking

def Ranking():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        _TABLA = "POSTULANT"
        _condicion="Registrado"
        sqlSelect = "Select name, last_name, Interviewed, Answered, Total, email from USERS order by Total DESC"
        cursor.execute(sqlSelect)
        data = cursor.fetchall()     
        return data  

    except:
        return redirect(url_for('errorr')) 

    finally:
        cursor.close()
        conn.close()

def UserSession(_user):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        _TABLA = "POSTULANT"
        _condicion="Registrado"
        sqlSelect = "Select name, last_name, Interviewed, Answered, Total, email, SEED from USERS WHERE email = '"+_user+"'"
        cursor.execute(sqlSelect)
        data = cursor.fetchall()     
        return data  

    except:
        print("hola")
        return redirect(url_for('errorr')) 

    finally:
        cursor.close()
        conn.close()

def UserSkip(_user):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        _TABLA = "POSTULANT"
        _condicion="Registrado"
        sqlSelect = "UPDATE USERS SET SEED = 'Skip' WHERE email = '"+_user+"'"
        cursor.execute(sqlSelect)
        data = cursor.fetchall()     
        if len(data)==0:
            return True
        else:
            return False  

    except:
        print("hola")
        return redirect(url_for('errorr')) 

    finally:
        cursor.close()
        conn.close()

def Sumsession(_user):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        _TABLA = "POSTULANT"
        _condicion="Registrado"
        sqlSelect = "UPDATE USERS SET sessions = 3 WHERE email = '"+_user+"'"
        cursor.execute(sqlSelect)
        data = cursor.fetchall()     
        if len(data)==0:
            return True
        else:
            return False  

    except:
        print("hola")
        return redirect(url_for('errorr')) 

    finally:
        cursor.close()
        conn.close()

def Ranking2():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        _TABLA = "POSTULANT"
        _condicion="Registrado"
        sqlSelect = "Select name, last_name, Interviewed, Answered, Total from USERS order by Total DESC LIMIT 3,40"
        cursor.execute(sqlSelect)
        data = cursor.fetchall()     
        return data  

    except:
        return redirect(url_for('errorr')) 

    finally:
        cursor.close()
        conn.close()

def Goal():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        _TABLA = "POSTULANT"
        _condicion="Registrado"
        sqlSelect = "Select * from GOAL"
        cursor.execute(sqlSelect)
        data = cursor.fetchall()     
        return data  

    except:
        return redirect(url_for('errorr')) 

    finally:
        cursor.close()
        conn.close()

def Editmeta(_meta, _fecha):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sqlSelect = "UPDATE USERS SET SEED = ''"
        cursor.execute(sqlSelect)
        sqlCreateS="UPDATE GOAL SET goal = '"+ _meta +"', end_date = '"+ _fecha +"'  WHERE ID_Goal = 1"
        cursor.execute(sqlCreateS)
        data = cursor.fetchall()
        if len(data)==0:
            return True
        else:
            return False
    except:
        print("help")
        return redirect(url_for('errorr')) 
    finally:
        cursor.close()
        conn.close()


def sesiones(_user):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()

        sqlCreateS="SELECT sessions FROM USERS WHERE email=""'" +_user+ "'"
        print(sqlCreateS)
        cursor.execute(sqlCreateS)
        data = cursor.fetchall()
        print(data)
        aa=str(data)
        aaa=(aa[2][0])
        return aaa

    except:
        return redirect(url_for('errorr')) 
    finally:
        cursor.close()
        conn.close()
