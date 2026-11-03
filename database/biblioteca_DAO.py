from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    def read_library_from_db(self):
        connessione = DBConnect.get_connection()
        cursor = connessione.cursor()

        query = "SELECT * FROM biblioteca"
        cursor.execute(query)

        lista_biblioteche = []
        for i in cursor :
            biblioteca = Biblioteca(i[0], i[1], i[2])
            lista_biblioteche.append(biblioteca)

        cursor.close()
        connessione.close()
        return lista_biblioteche

