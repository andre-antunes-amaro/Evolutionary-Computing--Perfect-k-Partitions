
class CAP:
    def __init__(self,Tfim):
        self._numEventos = 0
        self._tempoLimite = Tfim
        self._cadeia = []

    def top(self):
        return self._cadeia[-1]

    def delete(self):
        self._cadeia.pop()
        self._numEventos-=1

    def add(self,E):
        tempo = E.instante()
        if tempo < self._tempoLimite:
            l = 0
            acabarPesquisa = False
            while l<self._numEventos and not acabarPesquisa:
                if self._cadeia[l].instante()<tempo:
                    acabarPesquisa = True
                else:
                    l+=1
            if acabarPesquisa:
                self._cadeia = self._cadeia[:l] + [E] +self._cadeia[l:]
            else:
                self._cadeia.append(E)

            self._numEventos+=1
            
    def empty(self):
        return self._numEventos == 0