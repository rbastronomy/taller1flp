import mysql.connector
from mysql.connector import Error

class DAO():

    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                db='FLP'
            )
        except Error as ex:
            print("Error al intentar la conexión: {0}".format(ex))

    def listadmin(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("select run,password, name_us from users;")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))    
    
    def conectionloginadmin(self,curso):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "select *from users where run = {0} and password = '{1}';"
                cursor.execute(sql.format(curso[0], curso[1]))
                self.conexion.commit()
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def listpatients(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("select run,password, name_pa from patients;")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex)) 
    
    def conectionloginpatients(self,curso):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "select *from patients where run = {0} and password = '{1}';"
                cursor.execute(sql.format(curso[0], curso[1]))
                self.conexion.commit()
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))    
    
    def arrayquestions(self):
        if self.conexion.is_connected():
            cursor = self.conexion.cursor()
            cursor.execute("Select *from questions where DELETED_AT=False;")
            result = cursor.fetchall()
            return result

    def arraypatients(self):
        if self.conexion.is_connected():
            cursor = self.conexion.cursor()
            cursor.execute("select idpatient,run,dv,NAME_PA,FATHER_NAME,MOTHER_NAME,GENDER,BIRTHDAY,OBSERVATIONS from patients where DELETED_AT = 0;")
            result = cursor.fetchall()
            return result
           
    def addquestions(self, questions):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "insert into QUESTIONS(idtest,questions,descriptions,deleted_at) values (NULL,'{0}','{1}',False);"
                cursor.execute(sql.format(questions[0], questions[1]))
                self.conexion.commit()
                print("¡Pregunta registrada!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def updatequestion(self, info):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "update questions set questions = '{0}', descriptions = '{1}' where idquestion = {2};"
                cursor.execute(sql.format(info[0], info[1], info[2]))
                self.conexion.commit()
                print("Pregunta actualizada!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def delquestion(self, info):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "update questions set DELETED_AT = {0} where idquestion = {1}; "
                cursor.execute(sql.format(info[0],info[1]))
                self.conexion.commit()
                print("¡Pregunta eliminada!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def delpatients(self, info):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "update patients set DELETED_AT = {0} where idpatient = {1}; "
                cursor.execute(sql.format(info[0],info[1]))
                self.conexion.commit()
                print("¡Pasiente eliminado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))   

    def addpatients(self, questions):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "insert into patients (run,dv,NAME_PA,FATHER_NAME,MOTHER_NAME,GENDER,BIRTHDAY,PASSWORD,OBSERVATIONS,DELETED_AT) values ({0},'{1}','{2}','{3}','{4}','{5}','{6}','{7}',NULL,0);"
                cursor.execute(sql.format(questions[0], questions[1], questions[2], questions[3], questions[4], questions[5], questions[6], questions[7]))
                self.conexion.commit()
                print("¡Pregunta registrada!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def updatepatients(self, info):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "update questions set questions = '{0}', descriptions = '{1}' where idquestion = {2};"
                cursor.execute(sql.format(info[0], info[1], info[2]))
                self.conexion.commit()
                print("Pregunta actualizada!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def updatepatients(self, info):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "update patients set password = '{0}' where idpatient = {1};"
                cursor.execute(sql.format(info[0], info[1]))
                self.conexion.commit()
                print("Pasiente actualizado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))    

    def updateobservationpatients(self, info):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "update patients set OBSERVATIONS = '{0}' where idpatient = {1};"
                cursor.execute(sql.format(info[0], info[1]))
                self.conexion.commit()
                print("Pasiente actualizado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))  


    def printtest(self): 
        if self.conexion.is_connected():
            cursor = self.conexion.cursor()
            cursor.execute("Select *from tests where DELETED_AT=False;")
            result = cursor.fetchall()
            return result 

    def addtest(self, test):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                
                sql = "insert into tests (name,cut_point,max_point,observations,deleted_at) values ('{0}',{1},{2},'{3}',False);"
                cursor.execute(sql.format(test[0], test[1], test[2], test[3]))
                self.conexion.commit()
                print("¡Test registrado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
    
    def deltest(self, info):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "update tests set DELETED_AT = {0} where idtest = {1}; "
                cursor.execute(sql.format(info[0],info[1]))
                self.conexion.commit()
                print("¡Test eliminado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))


    def printtestpatient(self): 
        if self.conexion.is_connected():
            cursor = self.conexion.cursor()
            cursor.execute("select idtest,name,observations from tests where deleted_at = 0;")
            result = cursor.fetchall()
            return result 

    def printquestionspatient(self): 
        if self.conexion.is_connected():
            cursor = self.conexion.cursor()
            cursor.execute("select idquestion,questions,descriptions,tests.idtest,tests.name from questions join tests on questions.idtest = tests.idtest;")
            result = cursor.fetchall()
            return result    
    
    def addaswerd(self, test):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "insert into answers (idquestion,points,text,idpoll) values ({0},{1},'{2}',{3});"
                cursor.execute(sql.format(test[0], test[1], test[2], test[3]))
                self.conexion.commit()
                print("¡Respuesta registrada!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))  

    def printmaxpoll(self): 
        if self.conexion.is_connected():
            cursor = self.conexion.cursor()
            cursor.execute("select  MAX(idpoll) from poll;")
            result = cursor.fetchall()
            return result 

    def addidpoll(self,test):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql ="insert into poll (idpoll) value ({0});"
                cursor.execute(sql(test[0]))
                self.conexion.commit()
                print("¡pol agregada!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))




    #def arrayquestionstest():


    #def sum_respuestas(self):
    #    if self.conexion.is_connected():
    #        try:
    #            cursor = self.conexion.cursor()
    #            cursor.execute("select SUM(RESPUESTA) from relationship_1;")
    #            result = cursor.fetchall()
    #            return result
    #        except Error as ex:
    #            print("Error al intentar la conexión: {0}".format(ex))

    #def sum_preguntas(self):
    #    if self.conexion.is_connected():
    #        try:
    #            cursor = self.conexion.cursor()
    #            cursor.execute("select SUM(VAL) from preguntas;")
    #            result = cursor.fetchall()
    #            return result
    #        except Error as ex:
    #            print("Error al intentar la conexión: {0}".format(ex))
