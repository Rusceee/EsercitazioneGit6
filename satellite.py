from sensore import Sensore


class Satellite:

    def __init__(self, nome):
        self.nome = nome
        self.sensori = {}
        self.letture = []

    def aggiungi_sensore(self, sensore):
        self.sensori[sensore.codice] = sensore

    def registra_lettura(self, codice, valore):
        if codice not in self.sensori:
            print(f"Sensore {codice} non trovato")
            return

        s = self.sensori[codice]
        self.letture.append(
            {
                "sensore": codice,
                "grandezza": s.grandezza,
                "valore": valore,
                "unita": s.unita,
                "allarme": valore > s.soglia_massima,
            }
        )

    def elenca_oltre_soglia(self):
        return [l for l in self.letture if l["allarme"]]

    def stampa_riepilogo(self):
        print(f"Sensori: {len(self.sensori)}")
        print(f"Letture: {len(self.letture)}")
        print("Allarmi:", self.elenca_oltre_soglia())