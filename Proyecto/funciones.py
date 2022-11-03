from multiprocessing.sharedctypes import Value


def arrayquestions(questions):
    print("\nPreguntas: \n")
    for cur in questions:
        info = "ID: {0} | Description: {1} ({2} Value)"
        print(info.format(cur[0], cur[1], cur[2]))
    print(" ")


def auth():
    flagid = False
    while(not flagid):
        id = input("Ingrese código: ")
        if len(id)<4:
            flagid = True
        else:
            print("Código incorrecto: Debe tener hasta 4 dígitos.")

    description = input("Ingrese una pregunta: ")

    flagvalue = False
    while(not flagvalue):
        Value = input("Ingrese valor: ")
        if Value.isnumeric():
            if (int(Value) > 0 and int(Value) < 6):
                flagvalue = True
                Value = int(Value)
            else:
                print("Los créditos deben ser mayor a 0 y menor a 5.")
        else:
            print("Créditos incorrectos: Debe ser un número únicamente.")

    questions = (id, description, Value)
    return questions

def countquestions(questions):
    print("\nValor: \n")
    for cur in questions:
        info = "num preguntas es {0} "
        print(info.format(cur[0]))
        suma = 0
        suma = cur[0] / 2
        print (suma)
    print(" ")

def test(questions):
    print("\nValor: \n")
    for cur in questions:
        info = "{0}"
        print(info.format(cur[0]))
    print(" ")
