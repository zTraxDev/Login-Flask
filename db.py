import pymysql

def DataBase():
 return pymysql.connect(user="root", host="localhost", password="", db="login")