import pymysql
connection = pymysql.connect(
    host= "localhost",
    user= "root",
    password= "12345678",
    db= "basedatos"
)


cursor = connection.cursor()
