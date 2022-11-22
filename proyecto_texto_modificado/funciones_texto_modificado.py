from multiprocessing.sharedctypes import Value
from DataBase.conexion import DAO

dao = DAO()

def listadmins(info):
    for cur in info:
        datos = "{0} {1} {2}"
        datos.format(cur[0], cur[1], cur[2])


def verificationloginadmin(info):
    flag = False
    run = int(input("RUN: "))
    password = input("PASSWORD: ")
    for cur in info:
        if (cur[0] == run) and (cur[1]==password):
            flag = True
            break
    if flag == True:
        print("Bienvenido ",cur[2])
        return True  
    else:
        print("No estas Registrado") 
        return False


def listpatients(info):
    for cur in info:
        datos = "{0} {1} {2}"
        datos.format(cur[0], cur[1], cur[2])

def verificationloginpatients(info):
    flag = False
    run = int(input("RUN: "))
    password = input("PASSWORD: ")
    for cur in info:
        if (cur[0] == run) and (cur[1]==password):
            flag = True
            break
    if flag == True:
        print("Bienvenido",cur[2])
        return (True,run)
    else:
        print("No estas Registrado")  
        return (False,0)   

def arrayquestions(questions):
    print("\nPreguntas: \n")
    for cur in questions:
        info = "ID: {0} | IDTEST: {1} | Valor: '{2}' | Pregunta: '{3}' | Descripcion: '{4}'"
        print(info.format(cur[0], cur[1], cur[2],cur[3],cur[4]))
    print(" ")

def arraypatients(patients):
    print("\nPasientes: \n")
    for cur in patients:
        info = "ID: {0} | RUN: {1} | DIGITO VERIFICADOR: '{2}' | NOMBRES: '{3}' | APELLIDO PATERNO: '{4}'  | APELLIDO MATERNO: '{5}' | GENERO: '{6}' | FECHA NACIMIENTO '{7}' | OBSERVACION '{8}'" 
        print(info.format(cur[0], cur[1], cur[2],cur[3],cur[4],cur[5],cur[6],cur[7],cur[8]))
    print(" ")

def arrayobservationpatients(patients):
    print("\nPasientes: \n")
    for cur in patients:
        info = "ID: {0} | RUN: {1} | DIGITO VERIFICADOR: '{2}' | NOMBRES: '{3}' | APELLIDO PATERNO: '{4}'  | APELLIDO MATERNO: '{5}' | GENERO: '{6}' | FECHA NACIMIENTO '{7}' | OBSERVACION '{8}'" 
        print(info.format(cur[0], cur[1], cur[2],cur[3],cur[4],cur[5],cur[6],cur[7],cur[8]))
    print(" ")

def arrayonepatients(patients):
    print("\nPasiente: \n")
    for cur in patients:
        info = "ID: {0} | RUN: {1} | DIGITO VERIFICADOR: '{2}' | NOMBRES: '{3}' | APELLIDO PATERNO: '{4}'  | APELLIDO MATERNO: '{5}' | GENERO: '{6}' | FECHA NACIMIENTO '{7}' | OBSERVACION '{8}'" 
        print(info.format(cur[0], cur[1], cur[2],cur[3],cur[4],cur[5],cur[6],cur[7],cur[8]))
    print(" ")


def addquestion():
    questions = input("Ingrese una pregunta: ")
    description = input("Descripcion para la pregunta: ")
    add = (questions, description)
    return add

def Updatequestion(info):
    arrayquestions(info)
    id = int(input("Ingrese el código de la pregunta a editar: "))
    questions = input("Ingrese una pregunta: ")
    description = input("Descripcion para la pregunta: ") 
    for cur in info:
        if cur[0] == id:
            add=(questions,description,id)
            return add

def deletequestion(info):
    arrayquestions(info)
    id = int(input("Ingrese el código de la pregunta a eliminar: "))
    borrado = 1
    for cur in info:
        if cur[0] == id:
            delete = (borrado,id)
            return delete

def deletepatients(info):
    arraypatients(info)
    id = int(input("Ingrese el código del pasiente a eliminar: "))
    borrado = 1
    for cur in info:
        if cur[0] == id:
            delete = (borrado,id)
            return delete

def addpatients():
    run = int(input("Ingrese el run del pasiente: "))
    dv = input("Ingrese el digito verificador: (Numeros del 1 al 9 o k)")
    name_pa = input("Ingrese el nombre: (Ejemplo: Diego Andres)")
    father_nam = input("Ingrese el apellido paterno: ")
    mother_nam = input("Ingrese el apellido materno: ")
    gener = input("Ingrese el genero al que se identifica: ")
    birthday = input("Ingrese su cumpleaños: (Ejemplo = DD/MM/YY)")
    password= input("Ingrese su contraseña: ")


    add = (run, dv,name_pa,father_nam,mother_nam,gener,birthday,password)
    return add

def Updatepatient(info):
    listpatients(info)
    id = int(input("Ingrese el código del pasiente a editar: "))
    password = input("Ingrese una nueva contraseña: ") 
    for cur in info:
        if cur[0] == id:
            add=(password,id)
            return add

def Updateobservationpatient(info):
    listpatients(info)
    id = int(input("Ingrese el código del pasiente a editar: "))
    observation = input("Ingrese su diagnostico: ") 
    for cur in info:
        if cur[0] == id:
            add=(observation,id)
            return add

def searchpatient(info):
    flag = False
    run = int(input("RUN: "))
    dv = input("Digito Verificador: ")
    for cur in info:
        if (cur[0] == run) and (cur[1]==dv):
            flag = True
    if flag == True:
        information =(run,dv)
        return information
    else:
        print("No estas Registrado o no estas Disponible")  


def arraytest(tests):
    print("\nTests: \n")
    for cur in tests:
        info = "ID: {0} | NAME: '{1}' | PUNTAJE DE CORTE: '{2}' | VALOR TEST(MAX): '{3}' | DESCRIPCION: '{4}'"
        print(info.format(cur[0], cur[1], cur[2],cur[3],cur[4]))
    print(" ")

def addtest():
    name = input("Ingrese el nombre del test: ")
    cut_point = int(input("Ingrese el puntaje de corte: "))
    max_point = int(input("Ingrese el puntaje max del test: "))
    observations = input("Ingrese la descripcion del test: ")
    add = (name,cut_point,max_point,observations)
    return add

def updatequestiontest(questions,test):
    arrayquestionstest(questions)
    idquestion = int(input("Ingrese que pregunta quiere agregar: "))
    arraytest(test)
    idtest = int(input("Ingrese al test que pregunta quiere agregar: "))
    return (idtest,idquestion)

def arrayquestionstest(questions):
    print("\nPreguntas Disponibles: \n")
    for cur in questions:
        info = "ID: {0} | IDTEST: {1} | Pregunta: '{2}' | Descripcion: '{3}'"
        print(info.format(cur[0], cur[1], cur[2],cur[3]))
    print(" ")

def deltest(info):
    arraytest(info)
    id = int(input("Ingrese el código del pasiente a eliminar: "))
    borrado = 1
    for cur in info:
        if cur[0] == id:
            delete = (borrado,id)
            return delete

def arraytestpatient(tests):
    print("\nTests: \n")
    for cur in tests:
        info = "ID: {0} NAME: '{1}' | DESCRIPCION: '{2}'"
        print(info.format(cur[0], cur[1], cur[2]))
    print(" ")

    option = int(input("Que test decea realizar: "))
    for cur in tests:
        if cur[0] == option:
            print("estas haciendo el test numero ",cur[0])
            return (True,cur[0])
        else:
            return (False,0)

def arrayquestiontest(tests,idtest,idpatient):
    print("\nPreguntas: \n")
    poll= dao.printmaxpoll()
    a = maxpoll(poll[0])
    if a==None:
        a = 1
        group =(a,idtest,idpatient)
        dao.addidpoll(group)
    else:
        a=a+1
        group =(a,idtest,idpatient)
        dao.addidpoll(group)
    for cur in tests:
        info = " '{0}' '{1}'  {2} '{3}'"
        info.format(cur[0], cur[1], cur[2], cur[3])
        print("PREGUNTA: ",cur[1], "| EXPLICACION: ",cur[2])
        add = addanswerd(cur[0],a)
        dao.addaswerd(add)
        
        print(" ")
    return add

def addanswerd(dato,a):
        aswerd = int(input("Cual es su Respuesta(Ejemplo= 1): "))
        text = input("Argumentar Respuesta (opcional): ")
        add = (dato,aswerd,text,a)
        return (add)

            
def maxpoll(tests):
    dato = tests[0]
    return dato

def idpoll(tests):
    dato = tests[0]
    return dato


def verification(info):
    flag = False
    password = input("PASSWORD: ")
    for cur in info:
        if (cur[1]==password):
            flag = True
            break
    if flag == True:
        print("Confirmado")
        return True   
    else:
        print("No esta Confirmada esta Encuesta")  
        return False   

def passwordprint(tests):
    password = tests[0]
    return password

def searchidpatient(info,run):
    flag = False
    for cur in info:
        if (cur[1]==run):
            flag = True
    if flag == True:
        return (cur[0])   

def updateresult(info):
    for cur in info:
        info = " {0} | {1} | {2}"
        print(info.format(cur[0], cur[1], cur[2]))
    print(" ")

#def countquestions(questions):
#    print("\nValor: \n")
#    for cur in questions:
#        info = "num preguntas es {0} "
#        print(info.format(cur[0]))
#        suma = 0
#        suma = cur[0] / 2
#        print (suma)
#    print(" ")

#def test(questions):
#    print("\nValor: \n")
#    for cur in questions:
#        info = "{0}"
#        print(info.format(cur[0]))
#    print(" ")
