import mysql.connector

class database:

    def __init__(self, user, password, host, name_of_database, port):
        self.user = user
        self.password = password
        self.host = host
        self.name_of_database = name_of_database
        self.port = port

    def conn_to_database(self):
        print("Attempting to connect a user: " + self.user)
        try:
            global my_database
            my_database = mysql.connector.connect(
                host=str(self.host),
                user=str(self.user),
                password=str(self.password),
                database = str(self.name_of_database),
                port = str(self.port)
                ) 
            print("Connect to database was successful")
        except mysql.connector.Error as e:  
            print(e)

    def insert_to_database(self,sql):
        cursor = my_database.cursor()
        cursor.execute(sql)
        my_database.commit()

    def select_from_database(self,sql):
        try:
            cursor = my_database.cursor()
            cursor.execute(sql)
            return cursor.fetchall()
        except:
            return 10

    def close_database(self):
        try:
            user = self.user
            my_database.close()
            print("Connections is closed for " + user)
            return 1
        except:
            print("Connections isn't closed for " + user)
            return 0
