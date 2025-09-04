class evento:
    def __init__(self,kind,instante,envolvido):
        self._kind = kind
        self._instante = instante
        self._envolvido = envolvido
    
    def kind(self):
        return self._kind
    
    def instante(self):
        return self._instante

    def envolvido(self):
        return self._envolvido
        