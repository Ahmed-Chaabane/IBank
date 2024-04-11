import cx_Oracle

class Database:
    connect = None

    def __init__(self):
        """
        Constructor of the class
        """
        self.username = "bourse"
        self.password = "admin"
        self.host = "localhost"
        self.port = 1521
        self.service_name = "orcl"

        try:
            print("Connecting to the Oracle database...")
            conn_str = f"{self.username}/{self.password}@{self.host}:{self.port}/{self.service_name}"
            self.connect = cx_Oracle.connect(conn_str)
            print("Connection with Oracle database established successfully.")
        except cx_Oracle.DatabaseError as e:
            print("Database connection failed!")
            print(e)

    @staticmethod
    def get_instance():
        """
        Static method to get the database connection instance
        """
        if not Database.connect:
            Database.connect = Database()
        return Database.connect

    def connect_to_database(self):
        """
        Method to connect to the database
        """
        if self.connect:
            print("Already connected to the database.")
        else:
            try:
                self.connect = cx_Oracle.connect(f"{self.username}/{self.password}@{self.host}:{self.port}/{self.service_name}")
                print("Connection with Oracle database established successfully.")
            except cx_Oracle.DatabaseError as e:
                print("Database connection failed!")
                print(e)

    def disconnect(self):
        """
        Method to disconnect from the database
        """
        if self.connect:
            self.connect.close()
            self.connect = None
            print("Disconnected from the Oracle database.")
        else:
            print("Not connected to the database.")

    def authenticate_user(self, username, password):
        cursor = self.connect.cursor()
        query = "SELECT COUNT(*) FROM users WHERE username = :username AND password = :password"
        result = cursor.execute(query, username=username, password=password).fetchone()[0]
        cursor.close()

        return result == 1
