import mysql.connector 


class CiudadesBO:
    def __init__(self):
        #se crea la conexión con la base de datos
        self.db = mysql.connector.connect(host ="localhost", 
                                     user = "root", 
                                     password = "@lekz74671292", 
                                     db ="basedatos") 

    def __del__(self):
        self.db.close()

    def guardar(self, )
                                