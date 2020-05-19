"""
Corresponde a la parte que dado un diccionario con interpretaciones sobre formulas hace el proceso de mostrarlas en la pantalla
"""

import matplotlib.pyplot as plt
import codification as codify


Nfilas = 3
Ncols = 3
#numero de carros
Ncarros = 2
#cuantos tuernos maximos hay
NMax = 5


letras = []
for k in range(Ncarros):
    for i in range(Ncols):
        for e in range(Nfilas):
            for j in range(NMax):
                v1 = codify.codifica4(k, i,e,j, Ncarros, Ncols , Nfilas, NMax)
                cod = chr(v1+256)
                print(cod, end=" ")
                letras.append(cod)
            print("")


def showIt(pDiccionario):
    fig, axes = plt.subplots()
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)
    #creando la lista con los puntos que voy a tnener en cuenta en el recuadro
    listaX = []
    listaY = []
    for a in range(3):
        for b in range(3):
            listaX.append(a)
            listaY.append(b)

    plt.plot(listaX, listaY, 'ko')

    xdata = list(range(3))
    plt.plot(xdata, [1,1,1], 'k')
    plt.plot(xdata, [2,2,2], 'k')
    plt.plot(xdata, [0,0,0], 'k')

    ydata = list(range(3))
    plt.plot([0,0,0], ydata, 'k')
    plt.plot([1,1,1], ydata, 'k')
    plt.plot([2,2,2], ydata, 'k')
    #ya se creo el tablero, ahora a mostrar lo que esta dadoen el diccionario que es dadas unas letras prop
    #las llaves son las letras y los valores, si es uno o 0

    listXSolC1= [x for x in range(NMax)]
    listYSolC1 = [x for x in range(NMax)]
    listXSolC2= [x for x in range(NMax)]
    listYSolC2 = [x for x in range(NMax)]
    for ok in pDiccionario.keys():

        if ok in letras:
            if pDiccionario[ok] == 1:
                #quisiere decir que si es uno es decir si si pasa por ese camino en este caso se descgola
                c,x,y,t = codify.decodifica4(ord(ok) - 256, Ncarros, Nfilas, Ncols, NMax)
                if c == 0:
                    listXSolC1[t] = x
                    listYSolC1[t] = y
                else:
                    listXSolC2[t] = x
                    listYSolC2[t] = y
    
    for t in range(NMax):
        plt.plot(listXSolC1[t], listYSolC1[t], "r*")
        plt.plot(listXSolC2[t], listYSolC2[t], "b*")
        plt.savefig("turno"+ str(t)+".png")
        plt.plot(listXSolC1[t], listYSolC1[t], "r*")
        plt.plot(listXSolC2[t], listYSolC2[t], "b*")   
