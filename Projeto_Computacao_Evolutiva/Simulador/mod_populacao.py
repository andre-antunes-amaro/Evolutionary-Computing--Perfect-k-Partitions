import random as r

class populacao:
    def __init__(self):
        self._numIndividuos = 0
        self._listaIndividuos = []

    def add(self,ind):
        self._numIndividuos += 1
        self._listaIndividuos.append(ind)

    def remocaoEmMassa(self,P):
        for i in filter(P,self._listaIndividuos):
            self._listaIndividuos.remove(i)
            self._numIndividuos-=1

    def remover(self,ind):
        self._listaIndividuos.remove(ind)
        self._numIndividuos-=1

    def estaPresente(self, ind):
        return (ind in self._listaIndividuos)

    def randIndividuo(self):
        return r.choice(self._listaIndividuos)

    def numIndividuos(self):
        return self._numIndividuos

    def maximizante(self,f):
        curMax = self._listaIndividuos[0]
        for ind in self._listaIndividuos:
            if f(ind)>f(curMax):
                curMax = ind
        return curMax
