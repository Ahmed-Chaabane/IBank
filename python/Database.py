import cx_Oracle

class Database:
    connect = None

    def __init__(self):
        """
        Constructeur de la classe
        """
        self.username = "bourse"
        self.password = "admin"
        self.host = "localhost"
        self.port = 1521
        self.service_name = "orcl"

        try:
            print("Connexion à la base de données Oracle...")
            conn_str = f"{self.username}/{self.password}@{self.host}:{self.port}/{self.service_name}"
            self.connect = cx_Oracle.connect(conn_str)
            print("Connexion à la base de données Oracle établie avec succès.")
        except cx_Oracle.DatabaseError as e:
            print("Échec de la connexion à la base de données!")
            print(e)

    @staticmethod
    def get_instance():
        """
        Méthode statique pour obtenir l'instance de connexion à la base de données
        """
        if not Database.connect:
            Database.connect = Database()
        return Database.connect

    def connect_to_database(self):
        """
        Méthode pour se connecter à la base de données
        """
        if self.connect:
            print("Déjà connecté à la base de données.")
        else:
            try:
                self.connect = cx_Oracle.connect(f"{self.username}/{self.password}@{self.host}:{self.port}/{self.service_name}")
                print("Connexion à la base de données Oracle établie avec succès.")
            except cx_Oracle.DatabaseError as e:
                print("Échec de la connexion à la base de données!")
                print(e)

    def disconnect(self):
        """
        Méthode pour se déconnecter de la base de données
        """
        if self.connect:
            self.connect.close()
            self.connect = None
            print("Déconnexion de la base de données Oracle.")
        else:
            print("Pas connecté à la base de données.")

    def authenticate_user(self, username, password):
        cursor = self.connect.cursor()
        query = "SELECT COUNT(*) FROM users WHERE username = :username AND password = :password"
        result = cursor.execute(query, username=username, password=password).fetchone()[0]
        cursor.close()

        return result == 1