import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    # TODO
    def popola_genere(self):
        generi = self._model.get_generi()
        for genere in generi :
            self._view._ddGenere.options.append(ft.dropdown.Option(f"{genere}"))
        self._view.update()

    def popola_biblioteca(self):
        biblio = self._model.get_biblioteche()
        for b in biblio :
            self._view._ddBiblioteca.options.append(ft.dropdown.Option(f"{b}"))
        self._view.update()

    # CALLBACKS DROPDOWN
    # TODO
    def handler_ddBiblioteca(self, e):
        pass
    def handler_ddGenere(self, e):
        pass

    # AZIONE: MOSTRA LIBRI
    # TODO
    def mostra_libri(self, e):
        biblio_sel = self._view._ddBiblioteca.value
        genere_sel = self._view._ddGenere.value

        libri = self._model.get_libri_filtrati(biblio_sel, genere_sel)
        # Pulisco i risultati della ricerca precedente
        self._view._lista_libri.controls.clear()

        if len(libri) > 0 :
            self._view._lista_libri.controls = [ft.Text(f"{libro}") for libro in libri]
            # utilizzo di una list comprehension
        else:
            self._view.show_alert("Nessun libro trovato che soddisfi questi filtri")
        self._view.update()