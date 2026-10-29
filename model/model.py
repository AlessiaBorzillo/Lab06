from database.DB_connect import get_connection
from model.strumento import Strumento
from model.prestito import Prestito

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_strumenti(self) -> list[Strumento] | None:
        """
            Funzione che legge tutti gli strumenti nel database
            :return: una lista con tutti gli strumenti presenti oppure None
        """
        # TODO
        cnx = get_connection() #mi connetto al database
        strumenti = []
        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("SELECT * FROM strumento") # qui creo query
            for row in cursor:
                strumenti.append(Strumento(row["codice"], row["tipo"], row["marca"], row["anno_acquisto"], row["valore"], row["disponibile"]))
            cnx.close()
            cursor.close()
            return strumenti
        else:
            print("Nessuna connesione al database")
            return None


    def cerca_strumenti_per_tipo(self, tipo) -> list[Strumento] | None:
        """
            Funzione che recupera una lista con tutti gli strumenti presenti nel database di un certo tipo
            :param tipo: il tipo dello strumento (es. "Chitarra")
            :return: una lista con tutti gli strumenti del tipo indicato oppure None
        """
        # TODO
        cnx = get_connection()
        strumenti_per_tipo = []
        query = (""" SELECT *
                        FROM strumento
                        WHERE tipo = %s """) # %s scrittura standard: 'dovro selezionare qualcosa'
        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)
            cursor.execute(query, (tipo,))
            for row in cursor:
                strumenti_per_tipo.append(Strumento(row["codice"], row["tipo"], row["marca"],
                                           row["anno_acquisto"], row["valore"],
                                           row["disponibile"]))
            cnx.close()
            cursor.close()
            return strumenti_per_tipo
        else:
            print("Nessuna connesione al database")
            return None


        #crea struttura dati sulla base del mio database



