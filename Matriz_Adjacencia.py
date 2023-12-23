import numpy as np 

def imprimir(N,mat):
    for i in range(N):
        for j in range(N):
            print(mat[i,j],end='    ')
        print()

def loadMatriz():
    arquivo = open('G1.txt', 'r')
    lista = arquivo.readlines()

    for i in range(len(lista)):
        linha = lista[i].split()
        if i == 0:
            N = int(linha[0])
            matrz_adj = np.zeros((N ,N),dtype=np.int64)
        else:
            matrz_adj[ int(linha[0]), int(linha[1])] = 1
            matrz_adj[ int(linha[1]), int(linha[0])] = 1
    arquivo.close()
    imprimir(N,matrz_adj)
loadMatriz()


