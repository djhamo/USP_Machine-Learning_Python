print("Problema 2 - A")
borda = list()

nohExplorado = [] #(state, cost)

grafo = {
    "A": {"D": 10, "I": 11, "J": 12},
    "B": {"E": 14, "F": 8, "G": 12},
    "C": {"D": 13, "H": 12, "I": 8},
    "D": {"A": 10, "C": 13, "H": 9, "I": 6, "J": 10},
    "E": {"B": 14, "F": 12},
    "F": {"B": 8, "E": 12, "G": 11, "H": 10, "J": 13},
    "G": {"B": 12, "F": 11, "H": 8},
    "H": {"C": 13, "D": 9, "F": 10, "G": 8, "I": 12},
    "I": {"A": 11, "C": 8, "D": 6, "H": 12},
    "J": {"A": 12, "D": 10, "F": 13},
}

nohInicial = ("C", ["C"], 0)
nohFinal = "E"

borda.append(nohInicial)

while not (borda == []):
    #print(borda)
    
    #pega o Noh de menor "custo" na fila
    curID, todasAcoes, curCusto = borda.pop()
    #print(curID)
    
    #Coloca Noh atual na lista de explorados
    nohAtual = (curID, curCusto)
    nohExplorado.append(nohAtual)

    if (curID == nohFinal):
        print("Final:", todasAcoes, curCusto)
        break

    else:
        #Lista de Sucessores (successor, action, stepCost) e examina cada um
        sucessores = grafo[curID]
        
        #print(sucessores)
        for sucID in sorted(sucessores, key=sucessores.get, reverse=True):
        
            sucCusto = sucessores[sucID]
            novaAcao = todasAcoes + [sucID]
            novoCusto = sucCusto + curCusto

            novoNoh = (sucID, novaAcao, novoCusto)

            #Checa se o sucessor jah foi visitado
            jah_foi_explorado = False
            for explorado in nohExplorado:
                exID, exCusto = explorado
                if (sucID == exID) and (novoCusto >= exCusto):
                    jah_foi_explorado = True

            #Se nao foi explorado, coloca na fronteira
            if not jah_foi_explorado:
                borda.append(novoNoh)

print("Problema 2 - B")
borda = list()

nohExplorado = [] #(state, cost)

borda.append(nohInicial)

while not (borda == []):
    
    
    #pega o Noh de menor "custo" na fila
    curID, todasAcoes, curCusto = borda.pop()
    #print(curID)
    
    #Coloca Noh atual na lista de explorados
    nohAtual = (curID, curCusto)
    nohExplorado.append(nohAtual)

    if (curID == nohFinal):
        print("Final:", todasAcoes, curCusto)
        break

    else:
        #Lista de Sucessores (successor, action, stepCost) e examina cada um
        sucessores = grafo[curID]
        #print(sucessores)
        for sucID in sorted(sucessores, key=sucessores.get, reverse=True): 
        
            sucCusto = sucessores[sucID]
            novaAcao = todasAcoes + [sucID]
            novoCusto = sucCusto + curCusto

            novoNoh = (sucID, novaAcao, novoCusto)

            #Checa se o sucessor jah foi visitado
            jah_foi_explorado = False
            for explorado in nohExplorado:
                exID, exCusto = explorado
                if (sucID == exID) and (novoCusto >= exCusto):
                    jah_foi_explorado = True

            #Se nao foi explorado, coloca na fronteira
            if not jah_foi_explorado:
                borda.append(novoNoh)
                borda = sorted(borda, key=lambda k: k[2], reverse=True) 
                #print(borda)



