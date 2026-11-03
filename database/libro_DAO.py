from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def read_book_from_db(self):
        db = DBConnect()
        connessione = db.get_connection()
        cursor = connessione.cursor()

        query = "SELECT * FROM libro"
        cursor.execute(query)

        lista_libri = []
        for i in cursor:
            libro = Libro(i[0], i[1], i[2], i[3], i[4], i[5])
            lista_libri.append(libro)

        cursor.close()
        connessione.close()
        return lista_libri

