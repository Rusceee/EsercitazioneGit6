class Sensore:
    def __init__(self,codice,grandezza,unitaDiMisura,sogliaMassima)
        self._codice = codice
        self._grandezza = grandezza
        self._unitaDiMisura = unitaDiMisura
        self._sogliaMassima = sogliaMassima
        
    @property
    def codice(self):
        self._codice
    @property
    def grandezza(self):
        self._grandezza
    @property
    def unitaDiMisura(self):
        self._unitaDiMisura
    @property
    def sogliaMassima(self):
        self._sogliaMassima