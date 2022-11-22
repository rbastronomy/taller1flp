from DataBase.conexion import DAO
import funciones
dao = DAO()
idpatient = 0
def menu():
    flag = True
    while(flag==True):
        flag2 = False
        while(not flag2):
            print("========================================")
            print("1.- Ingresar como Administrador")
            print("2.- Ingresar como Paciente")
            print("3.- Salir")
            print("========================================")

            option = int(input("Seleccione una opción: "))
            

            if (option==1):
                login(1)

            elif (option==2):
                login(2)

            elif (option==3):
                flag=False
                print("Vuelva Pronto")
                break
            else:
                print("error")

def login(i):
    if (i == 1):
        info = dao.listadmin()
        
        if funciones.verificationloginadmin(info) == True:
            submenunadm()


    elif (i == 2):
        info = dao.listpatients()
        verification = funciones.verificationloginpatients(info)
        if verification[0] == True:
            global runuser
            runuser = verification[1]
            submenunpatient()

    
def submenunadm():
    flag = True
    while(flag==True):
        flag2 = False
        while(not flag2):
            print("========================================")
            print("1.- Printear Preguntas")
            print("2.- Ingresar una Pregunta")
            print("3.- Actualizar una Pregunta")
            print("4.- Eliminar una Pregunta")
            print("5.- Ingresar un Pasiente al sitema")
            print("6.- Actualizar un Pasiente")
            print("7.- Eliminar un Pasiente")
            print("8.- Ingresar Diagnostico")    
            print("9.- Buscar Pasiente")  
            print("10.- Printear Test")
            print("11.- Ingresar un nuevo Test")
            print("12.- Eliminar un Test")
            print("13.- Agregar Pregunta a Test")            
            print("14.- Salir")


            option = int(input("Seleccione una opción: "))
            

            if (option==1):
                questions = dao.arrayquestions()
                funciones.arrayquestions(questions)

            elif (option==2):
                add = funciones.addquestion()
                dao.addquestions(add)
            elif (option==3):
                info = dao.arrayquestions()
                function = funciones.Updatequestion(info)
                dao.updatequestion(function)

            elif (option==4):
                info = dao.arrayquestions()
                function = funciones.deletequestion(info)
                dao.delquestion(function)

            elif (option==5):
                add = funciones.addpatients()
                dao.addpatients(add)

            elif (option==6):
                info = dao.arraypatients()
                funciones.arraypatients(info)
                function = funciones.Updatepatient(info)
                dao.updatepatients(function)

            elif (option==7):
                info = dao.arraypatients()
                funciones.arraypatients(info)
                function = funciones.deletepatients(info)
                dao.delpatients(function)    
            elif (option==8):
                info = dao.arraypatients()
                funciones.arraypatients(info)
                function = funciones.Updateobservationpatient(info)
                dao.updateobservationpatients(function)

            elif (option==9):
                info = dao.patientssearch()
                function = funciones.searchpatient(info)
                asdasd = dao.printonepatient(function)
                funciones.arrayonepatients(asdasd)

            elif (option==10):
                questions = dao.printtest()
                funciones.arraytest(questions)
            elif(option==11):
                add = funciones.addtest()
                dao.addtest(add)
            elif(option==12):
                info = dao.printtest()
                function = funciones.deltest(info)
                dao.deltest(function)   
            elif(option==13):
                questions = dao.arrayquestionstest()
                test= dao.printtest()
                info = funciones.updatequestiontest(questions,test)
                dao.updateidtestquestion(info)

            elif (option==14):
                flag=False
                print("Vuelva Pronto")
                break
           
            else:
                print("error")  
def submenunpatient():
    flag = True
    while(flag==True):
        flag2 = False
        while(not flag2):
            print("========================================")
            print("1.- Realizar TEST")
            print("2.- Salir") 
            option = int(input("Seleccione una opción: "))
            if (option==1):
                info = dao.printidpatientrun()
                infouser = funciones.searchidpatient(info,runuser)
                test = dao.printtestpatient()
                test2 = funciones.arraytestpatient(test)
                if test2[0] == True:
                    op = dao.printquestionspatient()
                    function = funciones.arrayquestiontest(op,test2[1],infouser)
                    functionasd= funciones.idpollmax(function[3])

                    ##function[1]
                ##idmaxpoll = dao.printmaxpoll()
                ##idmaxpoll2 = funciones.maxpoll(idmaxpoll[0])
                ##information2 = dao.resultpoll(function[3])
                ##funciones.updateresult(information2)



            elif (option==2):
                information2 = dao.resultpoll(functionasd)
                funciones.updateresult(information2)
            else:
                print("error") 
               

if __name__ == "__main__":
    menu()