from DataBase.conexion import DAO
import funciones
def lobby():
    flag = True
    while(flag):
        _continue_ = False
        while(not _continue_):
            print("==================== MENÚ PRINCIPAL ====================")
            print("1.- Preguntas")
            print("2.- Registrar Nueva Pregunta")
            print("3.- Contador valor")
            print("4.- test linea")
            print("5.-test sumas")
            print("6.-")
            print("7.-")
            print("8.-")
            print("9.-")
            print("10.- Salir")
            print("========================================================")
            menu = int(input("Seleccione una opción: "))

            if menu < 1 or menu > 10:
                print("Opción incorrecta, ingrese nuevamente...")
            elif menu == 10:
                flag = False
                print("Programa finalizado")
                break
            else:
                _continue_ = True
                nummenu(menu)


def nummenu(menu):
    dao = DAO()
    if menu == 1:
        try:
            questions = dao.arrayquestions()
            if len(questions) > 0:
                funciones.arrayquestions(questions)
            else:
                print("No se encontraron cursos...")
        except:
            print("Ocurrió un error...")
    if menu == 2:
        question = funciones.auth()
        try:
            dao.addquestions(question)
        except:
            print("Ocurrió un error...")
    else:
        print("Opción no válida...")  

    if menu == 3:
        try :
            questions = dao.sum_respuestas()
            if len(questions) > 0:
                funciones.countquestions(questions)
        except:
            print("Ocurrió un error...")
    else:
        print("Opción no válida...")
    if menu == 4:
        try :
            questions = dao.printaralgo()
            if len(questions) > 0:
                funciones.test(questions)
        except:
            print("Ocurrió un error...")
    else:
        print("Opción no válida...")
    if menu == 5:
        try :
            questions = dao.sum_preguntas()
            if len(questions) > 0:
                funciones.test(questions)
        except:
            print("Ocurrió un error...")
    else:
        print("Opción no válida...")

lobby()