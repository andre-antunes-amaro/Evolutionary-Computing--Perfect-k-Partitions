from functools import reduce

class individuo:

    def __init__(self,p,k,X,tempo,Perf):
        self._particao = p
        self._numBlocos = k
        self._Blocos = []
        self._Perf = Perf
        self._X = X

        somas = p.LSomaBlocos()
        for b in range(k):
            self._Blocos.append([somas[b] == Perf,  tempo])

    def part(self):
        return self._particao

    def BlocosPerf(self):
        return [b for b in range(1,self._numBlocos+1) if self._Blocos[b-1][0]]
        

    def coeficiente(self):
        return reduce(lambda a,b: a + abs(b-self._Perf),self._particao.LSomaBlocos(),0)/self._numBlocos

    def instanteFormacao(self,i):
        return self._Blocos[i-1][1]

    def alterarParticao(self,i,b,instante):
        blocoOriginal = self._particao.ler(i)
        self._particao.editar(i,b)

        self._Blocos[b-1] = [self._particao.soma(b,self._X) == self._Perf,  instante]
        self._Blocos[blocoOriginal-1] = [self._particao.soma(blocoOriginal,self._X) == self._Perf,  instante]
    
    def associarBloco(self,i,B,instante):
        alterado = [False] * self._numBlocos
        for e in B:
            alterado[self._particao.ler(e)-1] = True
            self._particao.editar(e,i)
        self._Blocos[i-1] = [self._particao.soma(i,self._X) == self._Perf,   instante]
        for x in filter(lambda x: alterado[x], range(self._numBlocos)):
            self._Blocos[x] = [self._particao.soma(x+1,self._X) == self._Perf,   instante]
      