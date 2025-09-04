import random as r
from functools import reduce

class particao:
    def __init__(self,X,k):
        self._X = X
        self._numBlocos = k
        self._lista = [0]*len(X)
        for i in range(len(X)):
            self._lista[i] = r.randrange(1,k+1)
    
    def editar(self,i,x):
        self._lista[i] = x

    def ler(self,i):
        return self._lista[i]

    def LSomaBlocos(self):
        res = [0]*self._numBlocos
        for i in range(len(self._lista)):
            res[self._lista[i]-1]+=self._X[i]
        return res

    def blocoIndice(self,i):
        return [x for x in range(len(self._lista)) if self._lista[x]==i]
    
    def soma(self,I,X):
        return reduce(lambda a,b:a+X[b], 
        filter(lambda f: self._lista[f] == I,range(len(self._lista))),0)