from flask import Flask, render_template, request, json, url_for, redirect,send_from_directory,  g, session
from flaskext.mysql import MySQL
import Modelo as Modelo
import os
from PyPDF2 import PdfFileReader
from pathlib import Path
from flask_mail import Mail, Message
import smtplib
import time
import re
import PyPDF2
import sentimientos as sentimientos

mail = Mail()

app = Flask(__name__)

app.config['UPLOAD_PATH'] = './static/uploads'
app.config['UPLOAD_EXTENSIONS'] = ['.pdf']
app.config['MAIL_SERVER'] = 'SMTP.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'njrecruite902@gmail.com'
app.config['MAIL_PASSWORD'] = 'njrecruite_2020*'
app.config['MAIL_USE_SSL']= False
app.config['MAIL_USE_TLS']= True
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

mail.init_app(app)

@app.before_request
def before_request():
   g.user = None
   if 'user' in session:
      g.user = Modelo.buscarU(session['user'])

@app.route("/edit",methods=['POST','GET'])
def vacante():
    try:
        _id = request.args.get('id')
        consulta = Modelo.Editpost(_id)
        return render_template("Vacante.html", postulantes=consulta)
    except:
        return redirect(url_for('errorr')) 

@app.route("/re",methods=['POST','GET'])
def vac():
    try:
        _vacante = request.form.get('Empleo')
        consulta = Modelo.insvacante(_vacante)
        if consulta == True:
            return redirect(url_for('dassh'))
    except:
        print("error")

@app.route("/vacante")
def insvac():
    try:
            return render_template('F_Vacante.html')
    except:
        return redirect(url_for('errorr')) 

@app.route("/editar",methods=['POST','GET'])
def postedit():
    try:
        
        _nm = request.form.get('nm')
        _id = request.form.get('iddd')
        _vac = request.form.get('vacante')
        _edad = request.form.get('edad')
        _dir = request.form.get('dir')
        _lic = request.form.get('lic')
        _uni = request.form.get('uni')
        _prom = request.form.get('prom')
        _idio = request.form.get('idio')
        _email = request.form.get('email')
        _tele = request.form.get('tele')
        _cur = request.form.get('cur')
        _exp = request.form.get('exp')
        _apt = request.form.get('apt')
        _bool = Modelo.actualizarPostulante3(_id,_nm, _email, _edad, _dir, _lic, _uni, _prom, _idio, _exp, _cur, _tele, _apt, session['vacante'])
        if _bool == True:
            Modelo.eventosv()
            return redirect(url_for('selectA'))           

        if _bool == False:
           return redirect(url_for('errorr')) 
    except:
       return redirect(url_for('errorr'))

@app.route("/editar2",methods=['POST','GET'])
def postedit2():
    try:
        
        _nm = request.form.get('nm')
        _id = request.form.get('iddd')
        _vac = request.form.get('vacante')
        _edad = request.form.get('edad')
        _dir = request.form.get('dir')
        _lic = request.form.get('lic')
        _uni = request.form.get('uni')
        _prom = request.form.get('prom')
        _idio = request.form.get('idio')
        _email = request.form.get('email')
        _tele = request.form.get('tele')
        _cur = request.form.get('cur')
        _exp = request.form.get('exp')
        _apt = request.form.get('apt')
        _bool = Modelo.actualizarPostulante3(_id,_nm, _email, _edad, _dir, _lic, _uni, _prom, _idio, _exp, _cur, _tele, _apt, session['vacante'])
        if _bool == True:
            Modelo.eventosv()
            return redirect(url_for('selectB'))           

        if _bool == False:
           return redirect(url_for('errorr')) 
    except:
       return redirect(url_for('errorr'))

@app.route("/editar3",methods=['POST','GET'])
def postedit3():
    try:
        
        _nm = request.form.get('nm')
        _id = request.form.get('iddd')
        _vac = request.form.get('vacante')
        _edad = request.form.get('edad')
        _dir = request.form.get('dir')
        _lic = request.form.get('lic')
        _uni = request.form.get('uni')
        _prom = request.form.get('prom')
        _idio = request.form.get('idio')
        _email = request.form.get('email')
        _tele = request.form.get('tele')
        _cur = request.form.get('cur')
        _exp = request.form.get('exp')
        _apt = request.form.get('apt')
        _bool = Modelo.actualizarPostulante3(_id,_nm, _email, _edad, _dir, _lic, _uni, _prom, _idio, _exp, _cur, _tele, _apt, session['vacante'])
        if _bool == True:
            Modelo.eventosv()
            return redirect(url_for('selectC'))           

        if _bool == False:
           return redirect(url_for('errorr')) 
    except:
       return redirect(url_for('errorr'))

@app.route("/a", methods=['POST'])
def indexx():
    try:
        _p = request.form.get('correo1')
        if g.user:
            session.pop('vacante', None)
            session['vacante'] = _p
            consulta = Modelo.SelectAll(_p)
            return render_template("Postulantes.html", postulantes=consulta)
        else:
            session.pop('vacante', None)
            session['vacante'] = _p
            consulta = Modelo.SelectAll(_p)
            return render_template("Postulantes.html", postulantes=consulta)

    except:
        return redirect(url_for('errorr')) 

@app.route("/dash")
def dassh():
    try:
        consulta = Modelo.Dash()
        return render_template("DashVacantes.html", Dassh=consulta)
    except:
        return redirect(url_for('errorr')) 

@app.route("/closevac", methods=['POST'])
def closevac():
    try:
        print('Hi!')
        datos = request.get_json()
        print(datos)
        consulta = Modelo.Vacerrada(datos['vacante']) 
        if consulta == True: 
            res="La vacante "+datos['vacante']+" fue cerrada."
            return res
        else:
            return redirect(url_for('errorr')) 

        return res
    except:
        return redirect(url_for('errorr')) 

@app.route("/openvac", methods=['POST'])
def openvac():
    try:
        print('Hi!')
        datos = request.get_json()
        print(datos)
        consulta = Modelo.Vabierta(datos['vacante']) 
        if consulta == True: 
            res="La vacante "+datos['vacante']+" fue abierta."
            return res
        else:
            return redirect(url_for('errorr')) 

        return res
    except:
        return redirect(url_for('errorr')) 


@app.route("/editvac", methods=['POST'])
def editvac():
    try:
        print('Hi!')
        datos = request.get_json()
        print(datos)
        consulta = Modelo.Editvac(datos['vacante'], datos['Id']) 
        if consulta == True: 
            res="La vacante "+datos['vacante']+" fue abierta."
            return res
        else:
            return redirect(url_for('errorr')) 

        return res
    except:
        return redirect(url_for('errorr')) 

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/form')
def form():
    return render_template("form.html")


@app.route('/log')
def Login():
    return render_template("login.html")
    
@app.route('/login',methods=['GET','POST'])
def lo():
    try:
        if g.user:
            session.pop('user', None)

        if request.method=='POST':
            session.pop('user', None)
            user = request.form['correoL']
            _contrasenaL = request.form['contrasenaL']
            _bool=Modelo.validar(user, _contrasenaL)
        if _bool == True:
            session['user'] = user
            Modelo.eventos(user, 'login', 'se logeo el usuario')
            return redirect(url_for('dassh'))
            

        if _bool == False:
            session['user'] = user
            Modelo.eventos(user, 'Error al logear', 'error al intentar logearse')
            return render_template('Login.html', alert='Tu contraseña o usuario es incorrecto') 
    except:
        return redirect(url_for('errorr')) 
            
    finally:
            print("Lets go!")

@app.route('/s')
def s():
    return render_template("signup.html")

@app.route('/signup',methods=['GET','POST'])
def sig():
    
    try:
        
        x=0
        for key, value in request.form.items():
            print("key: {0}, value: {1}".format(key, value))
            if x==0:
                 _nombre = "{0}".format(value)
                 
            elif x==1:
                 _apellido = "{0}".format(value)

            elif x==2:
                 _correo = "{0}".format(value)

            elif x==3:
                 _celular = "{0}".format(value)

            elif x==4:
                 _contraseña = "{0}".format(value)
            print ("ciclo"+ str(x))
            x=x+1
          
   
           
        if _nombre and _apellido and _correo and _celular and _contraseña:
            _bool = Modelo.insertaruser(_nombre, _apellido, _correo, _celular, _contraseña)

        if _bool == True:
            return redirect(url_for('indexx'))          
        if _bool == False:
            return redirect(url_for('errorr')) 
            
        else:
            return redirect(url_for('errorr')) 

    except:
            return redirect(url_for('errorr')) 
    finally:
            print("Lets go!")


@app.route("/g",methods=['POST','GET'])
def correo():
     _p = request.args.get('correo')
     if _p:
         msg = Message('Reclutamiento', sender= app.config['MAIL_USERNAME'], recipients = [_p])
         msg.body = "Estimado candidato, agradecemos su interes, usted podra continuar con el proceso de selección."
         mail.send(msg)
         _bool = Modelo.actualizarPostulante(_p, session['vacante'])

         if _bool == True:
             Modelo.eventosAC()
             return redirect(url_for('selectB'))
         if _bool == False:
             return redirect(url_for('errorr')) 
            
      
@app.route("/d",methods=['POST','GET'])
def detalles():
     _p = request.args.get('correo')
     if _p:
         msg = Message('Reclutamiento', sender= app.config['MAIL_USERNAME'], recipients = [_p])
         msg.body = "Estimado candidato, agredecemos su interes pero no fue seleccionado para seguir con el proceso."
         mail.send(msg)
         
         _bool = Modelo.actualizarPostulante2(_p, session['vacante'])
         if _bool == True:
             Modelo.eventosRE()
             return redirect(url_for('selectC'))
             
         if _bool == False:
             return redirect(url_for('errorr')) 
            

    

@app.route("/selectA")
def selectA():
    try:
        consulta = Modelo.SelectAll(session['vacante'])
        Modelo.eventos1()
        return render_template("Postulantes.html", postulantes=consulta)
    except:
        return redirect(url_for('errorr')) 

@app.route("/selectB")
def selectB():
    try:
        consulta = Modelo.SelectB(session['vacante'])
        Modelo.eventos2()
        return render_template("Postulantes2.html", postulantes=consulta)
    except:
        return redirect(url_for('errorr')) 

@app.route("/selectC")
def selectC():
    try:
        consulta = Modelo.SelectC(session['vacante'])
        Modelo.eventos3()
        return render_template("Postulantes3.html", postulantes=consulta)
    except:
        return redirect(url_for('errorr')) 

@app.route("/Recuperacion")
def recuperacion():
    try:
        return render_template("olvide.html")
    except:
        return redirect(url_for('errorr')) 

@app.route("/Recuperar",methods=['POST','GET'])
def Recuperar():
    try:
        _c = request.args.get('Correo')
        if _c:
            return Modelo.Olvidar(_c)
    except:
        return redirect(url_for('errorr')) 

@app.route("/olvide",methods=['POST','GET'])
def Olvide():
    try: 
        _o = request.args.get('o')
        if _o:
            msg = Message('Reclutamiento', sender= app.config['MAIL_USERNAME'], recipients = [_o])
            msg.body = "Por favor ingrese al siguiente link para recuperar su contraseña: http://127.0.0.1:5000/Recupere?correo="+_o
            mail.send(msg)
            return render_template("Revisar.html")
    except:
        return redirect(url_for('errorr')) 

@app.route("/Recupere",methods=['POST','GET'])
def Recupere():
    try:
        _c = request.args.get('correo')
        if _c:
            consulta = Modelo.Recupere(_c)
            return render_template("Recuperar.html", users=consulta)
    except:
        return redirect(url_for('errorr')) 

@app.route("/Recuperada",methods=['POST','GET'])
def Recuperada():
    try:
        _c = request.args.get('correo')
        _contra = request.args.get('contra')
        if _c and _contra:
            return Modelo.Recuperada(_c, _contra)
    except:
        return redirect(url_for('errorr')) 

###PARA LOS COMENTARIOS DE LOS RECLUTADORES SOBRE LOS POSTULANTES
@app.route('/coments',methods=['GET','POST'])
def comentaa():
    
    try:
         _com = request.form.get('com')
         _comn = request.form.get('comn')

         if _com and _comn:
             _bool = Modelo.com(_com, _comn)
             consultaa = sentimientos.cogn(_com)

            # datos=request.get_json()
            # consulta=sentimientos.cogn(datos['_com'])
             #print(datos)
             print(consultaa)
             #axx = { "alerta": resultado, "origen" : "Servidor", "idioma": consulta['documents'][0]['confidenceScores']['positive']}
             _bool2 = Modelo.cog(consultaa, _comn)
         if _bool == True:
            return redirect(url_for('selectA')) 

         if _bool == False:
            return redirect(url_for('errorr')) 
            

    except:
            return redirect(url_for('errorr')) 
    finally:
            print("Lets go!")


#PARA HACER LA FORMA DEL POSTULANTE

@app.route("/formtexto")
def formadetexto():
    try:
        return render_template("FormaTexto.html")
    except:
        return redirect(url_for('errorr')) 


@app.route('/formatexto',methods=['GET','POST'])
def formatexto():
    try:
        x=0
        for key, value in request.form.items():
            print("key: {0}, value: {1}".format(key, value))
            if x==0:
                 _nom = "{0}".format(value)
                 
            elif x==1:
                 _cor = "{0}".format(value)

            elif x==2:
                 _eda = "{0}".format(value)

            elif x==3:
                 _dir = "{0}".format(value)

            elif x==4:
                 _car = "{0}".format(value)

            elif x==5:
                 _esc = "{0}".format(value)

            elif x==6:
                 _pro = "{0}".format(value)

            elif x==7:
                 _idi = "{0}".format(value)

            elif x==8:
                 _exp = "{0}".format(value)

            elif x==9:
                 _cur = "{0}".format(value)

            elif x==10:
                 _cel = "{0}".format(value)
                 
            elif x==11:
                 _apt = "{0}".format(value)
           
            elif x==12:
                 _vac = "{0}".format(value)
            elif x==13:
                 _cv = "{0}".format(value)

            print ("ciclo"+ str(x))
            x=x+1
          
   
          
        if _nom and _cor and _eda and _dir and _car and _esc and _pro and _idi and _exp and _cur and _cel and _apt:
            _bool=Modelo.insertarpostext(_nom, _cor, _eda, _dir, _car, _esc, _pro, _idi, _exp, _cur, _cel, _apt, _vac, _cv)
            if _bool == True:
                return redirect(url_for('Gracias'))
            if _bool == False:
                return redirect(url_for('errorr')) 
        else:
            return redirect(url_for('errorr')) 

    except:
            return redirect(url_for('errorr')) 
    finally:
            print("Lets go!")

@app.route("/formulario")
def formulario():
    try:
        return render_template("FormaTexto.html")
    except:
        return redirect(url_for('errorr')) 

@app.route("/download", methods=['GET','POST'])
def download():
    try:
        _a = request.args.get('archivo')
        return _a.open(os.path.join(app.config['UPLOAD_PATH/'+_a]))
    except:
        return redirect(url_for('errorr')) 

@app.route("/Gracias")
def Gracias():
    try:
        return render_template("Gracias.html")
    except:
        return redirect(url_for('errorr')) 

@app.route("/errorr")
def errorr():
    try:
        return render_template("Error.html")
    except:
        return redirect(url_for('errorr')) 

@app.route("/f",methods=['GET', 'POST'])
def archivo():
    try:
        if request.method == 'POST':
            _a=request.files['Archivo']
            _nomarchivo=_a.filename
            if guardarArchivo(_a):
               print("Si se guardo!")
               _datos=extraerDatos(_a.filename)
               _encontrados=ParseoTexto(_datos)
               _encontrados2=ParseoTexto2(_datos)
               if _encontrados:
                   _vac = request.form.get('vac')
                   Modelo.Insertarpostulante(_encontrados, _vac, _nomarchivo)
                   return render_template('Gracias.html')
               elif _encontrados2: 
                    _vac = request.form.get('vac')                 
                    Modelo.Insertarpostulante(_encontrados2, _vac,_nomarchivo)
                    return render_template('Gracias.html')
               else:
                   _encontrados3=ParseoForm2(_datos)
                   if _encontrados3:
                       _encontrados3=_encontrados3[0]
                   else:
                       _encontrados3=''
                   _encontrados4=ParseoForm3(_datos)
                   if _encontrados4:
                       _encontrados4=_encontrados4[0]
                   else:
                       _encontrados4=''
                   _encontrados5=ParseoForm4(_datos)
                   if _encontrados5:
                       _encontrados5=_encontrados5[0]
                   else:
                       _encontrados5=''
                   _encontrados6=ParseoForm5(_datos)
                   if _encontrados6:
                       _encontrados6=_encontrados6[0]
                   else:
                       _encontrados6=''
                   _encontrados7=ParseoForm6(_datos)
                   if _encontrados7:
                       _encontrados7=_encontrados7[0]
                   else:
                       _encontrados7=''
                   _encontrados8=ParseoForm7(_datos)
                   if _encontrados8:
                       _encontrados8=_encontrados8[0]
                   else:
                       _encontrados8=''
                   _encontrados9=ParseoForm8(_datos)
                   if _encontrados9:
                       _encontrados9=_encontrados9[0]
                   else:
                       _encontrados9=''
                   _encontrados10=ParseoForm9(_datos)
                   if _encontrados10:
                       _encontrados10=_encontrados10[0]
                   else:
                       _encontrados10=''
                   _encontrados11=ParseoForm10(_datos)
                   if _encontrados11:
                       _encontrados11=_encontrados11[0]
                   else:
                       _encontrados11=''
                   _encontrados12=ParseoForm11(_datos)
                   if _encontrados12:
                       _encontrados12=_encontrados12[0]
                   else:
                       _encontrados12=''
                   _encontrados13=ParseoForm12(_datos)
                   if _encontrados13:
                       _encontrados13=_encontrados13[0]
                   else:
                       _encontrados13=''
                   print(_encontrados3[0])
                   _name=request.form['name']
                   _vac=request.form['vac']
                   _pdf=Modelo.Eventocv(_nomarchivo)
                   return render_template('Form2.html', pdfs=_pdf, name=_name, correo=_encontrados3, edad=int(_encontrados4), dir=_encontrados5, lic=_encontrados6, esc=_encontrados7, prom=_encontrados8, idi=_encontrados9, exp=_encontrados10, cur=_encontrados11, cel= int(_encontrados12), vac=_vac)
            else:
                _openvacante=Modelo.openvacante()
                return render_template('form.html', openvacantes=_openvacante, alert='Tu archivo no es PDF')

    except:
        return redirect(url_for('errorr')) 
    _openvacante=Modelo.openvacante()
    return render_template('form.html', openvacantes=_openvacante, alert='')

               

def extraerDatos(_nombrearchivo):
    pdf_reader=PdfFileReader(os.path.join(app.config['UPLOAD_PATH'], _nombrearchivo))
    output_file_path= Path.cwd() / "TextoParaParseo.txt"
    with output_file_path.open(mode="w") as output_file:
        title = pdf_reader.documentInfo.title
        num_pages = pdf_reader.getNumPages()
        output_file.write(f"{title}\\nNumber of pages: {num_pages}\\n\\n")
        for page in pdf_reader.pages:
            text=page.extractText()
            output_file.write(text)
    time.sleep(3)
    _textoaparsear=open('TextoParaParseo.txt', 'r')  
    _contenido=_textoaparsear.read()
    print("Contenido ",_contenido)
    return _contenido

def guardarArchivo(_archivo):
    if _archivo.filename != '':
        file_ext=os.path.splitext(_archivo.filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            return False
        _archivo.save(os.path.join(app.config['UPLOAD_PATH'], _archivo.filename))
        return True
    return False


def ParseoTexto(_texto):
    _patron = (r"NOMBRE:(.*\n"
	r".*\n"
	r".*\n"
	r".*)\n"
	r"CORREO:(.*\n"
	r".*\n"
	r".*)\n"
	r"EDAD:(.*\n"
	r".*\n"
	r".*)\n"
	r"DIRECCION:(.*\n"
	r".*\n"
	r".*\n"
	r".*)\n"
	r"LICENCIATURA(.*\n"
	r".*\n"
	r".*\n"
	r".*)\n"
	r"ESCUELA:(.*\n"
	r".*\n"
	r".*\n"
	r".*)\n"
	r"PROMEDIO:(.*\n"
	r".*\n"
	r".*\n"
	r".*)\n"
	r"IDIOMAS:(.*\n"
	r".*\n"
	r".*\n"
	r".*)\n"
	r"EXPERIENCIA:(.*\n"
	r".*\n"
	r".*\n"
	r".*\n"
	r".*)\n"
	r"CURSOS:(.*\n"
	r".*\n"
	r".*\n"
	r".*\n"
	r".*\n"
	r".*\n"
	r".*)\n"
	r"CELULAR:(.*\n"
	r".*\n"
	r".*\n"
	r".*)\n"
	r"APTITUDES:(.*\n"
	r".*\n"
	r".*\n"
	r".*\n"
	r".*\n"
	r".*\n"
	r".*\n"
	r".*)\n"
    r".*\n"
	r".*\n")

    _todos=re.findall(_patron, _texto, re.MULTILINE)
    return _todos 

def ParseoTexto2(_texto):
    _patron2 = (r"NOMBRE:(.*\n"
	r".*\n"
	r".*\n"
	r".*\n"
	r".*)\n"
	r"CORREO:(.*\n"
	r".*\n"
	r".*\n"
	r".*)\n"
	r"EDAD:(.*\n"
	r".*\n"
	r".*\n"
	r".*)\n"
	r"DIRECCION:(.*\n"
	r".*\n"
	r".*\n"
	r".*)\n"
	r"LICENCIATURA:(.*\n"
	r".*\n"
	r".*\n"
	r".*)\n"
	r"ESCUELA:(.*\n"
	r".*\n"
	r".*\n"
	r".*)\n"
	r"PROMEDIO:(.*\n"
	r".*\n"
	r".*\n"
	r".*)\n"
	r"IDIOMAS:(.*\n"
	r".*\n"
	r".*\n"
	r".*)\n"
	r"EXPERIENCIA:(.*\n"
	r".*\n"
	r".*\n"
	r".*\n"
	r".*\n"
	r".*\n"
	r".*)\n"
	r"CURSOS:(.*\n"
	r".*\n"
	r".*\n"
	r".*\n"
	r".*\n"
	r".*)\n"
	r"CELULAR:(.*\n"
	r".*\n"
	r".*\n"
	r".*)\n"
	r"APTITUDES:(.*\n"
	r".*\n"
	r".*\n"
	r".*\n"
	r".*\n"
	r".*)\n"
    r".*\n"
	r".*\n")

    _todos=re.findall(_patron2, _texto, re.MULTILINE)
    return _todos 

def ParseoForm2(_texto):
    _patron2 = (r"CORREO:(.*\n"
	r".*\n"
	r".*)")
    _todos=re.findall(_patron2, _texto, re.MULTILINE)
    return _todos 

def ParseoForm3(_texto):
    _patron2 = (r"Edad:(.*\n"
	r".*\n"
	r".*)")
    _todos=re.findall(_patron2, _texto, re.MULTILINE)
    return _todos 

def ParseoForm4(_texto):
    _patron2 = (r"DIRECCION:(.*\n"
	r".*\n"
	r".*)")
    _todos=re.findall(_patron2, _texto, re.MULTILINE)
    return _todos 

def ParseoForm5(_texto):
    _patron2 = (r"LICENCIATURA:(.*\n"
	r".*\n"
	r".*)")
    _todos=re.findall(_patron2, _texto, re.MULTILINE)
    return _todos

def ParseoForm6(_texto):
    _patron2 = (r"ESCUELA:(.*\n"
	r".*\n"
	r".*)")
    _todos=re.findall(_patron2, _texto, re.MULTILINE)
    return _todos

def ParseoForm7(_texto):
    _patron2 = (r"PROMEDIO:(.*\n"
	r".*\n"
	r".*)")
    _todos=re.findall(_patron2, _texto, re.MULTILINE)
    return _todos

def ParseoForm8(_texto):
    _patron2 = (r"IDIOMAS:(.*\n"
	r".*\n"
	r".*)")
    _todos=re.findall(_patron2, _texto, re.MULTILINE)
    return _todos

def ParseoForm9(_texto):
    _patron2 = (r"EXPERIENCIA:(.*\n"
	r".*\n"
	r".*)")
    _todos=re.findall(_patron2, _texto, re.MULTILINE)
    return _todos

def ParseoForm10(_texto):
    _patron2 = (r"CURSOS:(.*\n"
	r".*\n"
	r".*)")
    _todos=re.findall(_patron2, _texto, re.MULTILINE)
    return _todos

def ParseoForm11(_texto):
    _patron2 = (r"CELULAR:(.*\n"
	r".*\n"
	r".*)")
    _todos=re.findall(_patron2, _texto, re.MULTILINE)
    return _todos

def ParseoForm12(_texto):
    _patron2 = (r"APTITUDES:(.*\n"
	r".*\n"
	r".*)")
    _todos=re.findall(_patron2, _texto, re.MULTILINE)
    return _todos

if __name__ == "__main__":
    app.run()
