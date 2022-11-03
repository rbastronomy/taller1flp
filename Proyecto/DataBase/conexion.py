import mysql.connector

from mysql.connector import Error

class DAO():

    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                ##password='123456',
                db='proyecto1'
            )
        except Error as ex:
            print("Error al intentar la conexión: {0}".format(ex))

    def arrayquestions(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM preguntas")
                result = cursor.fetchall()
                return result
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def addquestions(self, questions):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO preguntas (IDPREGUNTAS, DES, VAL) VALUES ('{0}', '{1}', {2})"
                cursor.execute(sql.format(questions[0], questions[1], questions[2]))
                self.conexion.commit()
                print("¡Pregunta registrada!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))


    def sum_respuestas(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("select SUM(RESPUESTA) from relationship_1;")
                result = cursor.fetchall()
                return result
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def sum_preguntas(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("select SUM(VAL) from preguntas;")
                result = cursor.fetchall()
                return result
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    




    