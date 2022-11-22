from DataBase.conexion import DAO
import funciones
dao = DAO()
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
        if funciones.verificationloginpatients(info) == True:
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
            print("13.- Salir")


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
                info = dao.arraypatients()
                funciones.searchpatient(info)

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


            elif (option==13):
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
                test = dao.printtestpatient()
                if funciones.arraytestpatient(test) == True:
                    op = dao.printquestionspatient()
                    funciones.arrayquestiontest(op)

            elif (option==2):
                flag=False
                print("Vuelva Pronto")
            else:
                print("error")  

if __name__ == "__main__":
    submenunpatient()