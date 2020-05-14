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
NMax = Nfilas - 1 + Ncols - 1


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

    listXSolC1= []
    listYSolC1 = []
    listXSolC2= []
    listYSolC2 = []
    for ok in pDiccionario.keys():
        if pDiccionario[ok] == 1:
            #quisiere decir que si es uno es decir si si pasa por ese camino en este caso se descgola
            c,x,y,t = codify.decodifica4(ord(ok) - 256, Ncarros, Nfilas, Ncols, NMax)
            if t == 0:
                if c == 0:
                    plt.plot(x,y,"r*")
                elif c== 1:
                    plt.plot(x,y,"b*")
            elif t == 1:
                if c == 0:
                    plt.plot(x,y,"r.")
                elif c== 1:
                    plt.plot(x,y,"b.")
            elif t == 2:
                if c == 0:
                    plt.plot(x,y,"r,")
                elif c== 1:
                    plt.plot(x,y,"b,")
            elif t == 3:
                if c == 0:
                    plt.plot(x,y,"rs")
                elif c== 1:
                    plt.plot(x,y,"bs")

    #TODO:incluir el t, una figura diferente

    #ya con los caminos que tomaron ahora si se va a mostrar en pantlla
    #plt.plot(listXSolC1, listYSolC1, 'r*')
    #plt.plot(listXSolC2, listYSolC2, 'r*')




    #plt.grid()
    plt.show()

"""
POSIBLE SOLUCION DEL PROBLEMA A MANO
plt.plot([0],[0],'r*')
plt.plot([1],[0],'r*')
plt.plot([2],[0],'r*')
plt.plot([2],[1],'r*')
plt.plot([2],[2],'r*')

Supongamos entonces que como hay varios turnos, van a haber vaerios carros del mismo color
es decir, se va a mostrar un recorrio, s
"""
#plt.ylabel("some numebr")
