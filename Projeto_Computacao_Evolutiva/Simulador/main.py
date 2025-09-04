from math import log
from functools import reduce
import random as r
from funcoesEvento import *

from mod_CAP import CAP
from mod_evento import evento
from mod_individuo import individuo
from mod_particao import particao
from mod_populacao import populacao


def aleatoriaExp(v_medio):
    return -v_medio *log(r.random())

def simulador(X,k,TFim,TMorte,TMut,TRep,NInd):

    Perf = reduce(lambda x,y: x+y, X,0)/k

    Res = individuo(particao(X,k),k,X,0,Perf)
    particaoEncontrada = False

    C = CAP(TFim)

    P = populacao()

    for it in range(NInd):
        ind = individuo(particao(X,k), k,X, 0.0,Perf)

        if len(ind.BlocosPerf()) == k:
            Res = ind
            particaoEncontrada = True


        P.add(ind)
        C.add(evento("mutacao",aleatoriaExp(TMut),ind))

    C.add(evento("reproducao",aleatoriaExp(TRep), P))
    C.add(evento("morte",aleatoriaExp(TMorte),P))

    while not (C.empty() or particaoEncontrada):

        evt = C.top()
        C.delete()

        if evt.kind() == 'mutacao' and P.estaPresente(evt.envolvido()):
          
            ind = evt.envolvido()
        
            mutacao(ind,evt.instante(),X,k,Perf)
            
            C.add(evento("mutacao",
            evt.instante() + aleatoriaExp(TMut),ind))

            if len(ind.BlocosPerf()) == k:
                Res = ind
                particaoEncontrada = True
                

            
        elif (evt.kind() == 'reproducao') and (P.numIndividuos() > 1):
           
            Ind1 = P.randIndividuo()
            Ind2 = P.randIndividuo()
        
            while (Ind2 == Ind1):
                Ind2 = P.randIndividuo()
            
            existeReprod, ind = reproducao(Ind1,Ind2,evt.instante(),X,k,Perf)

            if existeReprod:
                P.add(ind)
                C.add(evento("mutacao",
                evt.instante()+aleatoriaExp(TMut),ind))

                if k==len(ind.BlocosPerf()):
                    Res = ind
                    particaoEncontrada = True


            C.add(evento("reproducao",
            evt.instante()+aleatoriaExp(TRep),P))
           
        
        elif evt.kind() == "morte":
            
            morte(evt.envolvido(),evt.instante())

            if P.numIndividuos() == 0:
                for Ind in range(NInd):

                    ind = individuo(particao(X,k),k,X,evt.instante(),Perf)
                    if len(ind.BlocosPerf()) == k:
                        Res = ind
                        particaoEncontrada = True
                    else:
                        P.add(ind)
                    
                    C.add(evento("mutacao",evt.instante()+aleatoriaExp(TMut),ind))


            C.add(evento("morte", evt.instante()+aleatoriaExp(TRep), P))
            


    if particaoEncontrada:
        print("Resultado Final (Exato): ", [[X[y] for y in range(len(X)) if Res.part().ler(y) == x  ] for x in range(1,k+1)])
    else:
        bestInd = P.maximizante(lambda ind: 1/ind.coeficiente())

        print("Resultado Final (Aproximado): ", [[X[y] for y in range(len(X)) if bestInd.part().ler(y) == x] for x in range(1,k+1)])