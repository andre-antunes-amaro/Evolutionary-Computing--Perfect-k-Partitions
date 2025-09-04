
from mod_individuo import individuo
from mod_particao import particao

import random as r

def mutacao(ind, tempo,X,k,Perf):
    menores=[]
    maiores=[]

    partic = ind.part()
    
    somas = partic.LSomaBlocos()
    
    for i in range(k):
        
        if somas[i]>Perf:
            maiores.append(i+1)
        elif somas[i]<Perf:
            menores.append(i+1)
            
    indbmenor = r.choice(menores)
    indbmaior = r.choice(maiores)
    
    dif = somas[indbmaior-1] - somas[indbmenor-1]
    

    indicex = r.choice(partic.blocoIndice(indbmaior))
    
    x = X[indicex]
            
    listaIndxLinha = partic.blocoIndice(indbmenor)
    SeleclistaIndxLinha = []
    somaxLinha = 0

    while len(listaIndxLinha) !=0 and somaxLinha < x-dif*0.5:
        
        indicexl = r.choice(listaIndxLinha)
        
        SeleclistaIndxLinha.append(indicexl)
        listaIndxLinha.remove(indicexl)
    
        somaxLinha += X[indicexl]
    
    ind.alterarParticao(indicex,indbmenor,tempo)
    ind.associarBloco(indbmaior,SeleclistaIndxLinha,tempo)

    

def morte(P,tempo):
    def condicaoDeMorte(ind):
        blocosPerfeitos = ind.BlocosPerf()

        if blocosPerfeitos != []:
            velho = novo = ind.instanteFormacao(blocosPerfeitos[0])
            for i in blocosPerfeitos:
                if velho > ind.instanteFormacao(i):
                    velho = ind.instanteFormacao(i)
                if novo < ind.instanteFormacao(i):  
                    novo = ind.instanteFormacao(i)

            return 2*velho < tempo-novo
            
        else:
            return False

    P.remocaoEmMassa(condicaoDeMorte)




def reproducao(pai,mae,tempo,X,k,Perf):
    existeReprod = False
    filho = individuo(particao(X,k),k,X,tempo,Perf)
    filho.associarBloco(k,list(range(len(X))),tempo)
     
    indicesBlocosPerfPai = pai.BlocosPerf()

    if indicesBlocosPerfPai != []:
        BlocoDoPai = r.choice(indicesBlocosPerfPai)
        indicesBlocosPerfMae = mae.BlocosPerf()
        
        indicesUtilizados = []
        existeReprod = True

        for x in pai.part().blocoIndice(BlocoDoPai):
            existeEmImperfeito = False
            bMae = 1
            while bMae<=k and not existeEmImperfeito:
                if not (bMae in indicesBlocosPerfMae):
                    indicesEmbMae = mae.part().blocoIndice(bMae)
                    i=0
                    while i<len(indicesEmbMae) and not existeEmImperfeito:
                        if X[indicesEmbMae[i]] == X[x] and not (indicesEmbMae[i] in indicesUtilizados):
                            indicesUtilizados.append(indicesEmbMae[i])
                            existeEmImperfeito = True
                        i+=1
                bMae+=1
            if not existeEmImperfeito:
                existeReprod = False

        if existeReprod:
            filho.associarBloco(1,indicesUtilizados,pai.instanteFormacao(BlocoDoPai))
            i = 2

            for bMae in indicesBlocosPerfMae:
                indicesDoBloco = mae.part().blocoIndice(bMae)
                filho.associarBloco(i,indicesDoBloco,mae.instanteFormacao(i))
                

                indicesUtilizados += indicesDoBloco
                i=i+1
                
            if i <=k:
                BlocosNovos = []
                for x in range(k+1-i):
                    BlocosNovos.append([])

                for x in range(len(X)):
                    if not(x in indicesUtilizados):
                        BlocosNovos[r.randrange(k+1-i)].append(x)

                for b in BlocosNovos:
                    filho.associarBloco(i,b,tempo)
                    i+=1
    

    
    return existeReprod, filho

