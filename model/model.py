from database.biblioteca_DAO import BibliotecaDAO
from database.libro_DAO import LibroDAO

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di BibliotecaDAO e LibroDAO)
'''

class Model:
    def __init__(self):
        self._biblioteca_dao = BibliotecaDAO()
        self._libro_dao = LibroDAO()

    # --- LIBRI ---
    def get_libri_filtrati(self, biblioteca:str, genere:str):
        """Restituisce la lista di tutti i libri filtrati per biblioteca e/o genere (filtri opzionali)."""
        # TODO
        lista_libri_filtrati = []
        if genere == "Nessun filtro" and biblioteca == "Nessun filtro":
            return self._libro_dao.read_book_from_db()
        # devo fare prima un join
        id_biblio = None
        for biblio in self._biblioteca_dao.read_library_from_db() :
            if biblio.nome in biblioteca :
                id_biblio = biblio.id


        for i in self._libro_dao.read_book_from_db():
            if i.genere == genere and i.id_biblioteca == id_biblio:
                lista_libri_filtrati.append(i)
            elif genere == "Nessun filtro" :
                if i.id_biblioteca == id_biblio:
                    lista_libri_filtrati.append(i)
            elif biblioteca == "Nessun filtro" :
                if i.genere == genere:
                    lista_libri_filtrati.append(i)
        return lista_libri_filtrati


    def get_generi(self):
        """Restituisce la lista di tutti i generi."""
        # TODO
        lista_generi = ["Nessun filtro"]
        for i in self._libro_dao.read_book_from_db() :
            if i.genere not in lista_generi:
                lista_generi.append(i.genere)
        return lista_generi

    # --- BIBLIOTECHE ---
    def get_biblioteche(self):
        """ Restituisce la lista di tutte le biblioteche."""
        # TODO
        lista_biblioteche = self._biblioteca_dao.read_library_from_db()
        lista_biblioteche.insert(0,"Nessun filtro")
        return lista_biblioteche
