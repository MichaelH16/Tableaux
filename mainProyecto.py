
import codification as codify
import visualizadorProyecto as vs

#psewudomian

#hace referencia al corro uno donde comiuenza
x_st_c1 = 0
y_st_c1 = 0
#donde deberia terminar
x_ob_c1 = 2
y_ob_c1 = 2
#el tamano de donde lo vamos a hacer
Nfilas = 4
Ncols = 4
#numero de carros
Ncarros = 2
#cuantos tuernos maximos hay
#NMax = Nfilas - 1 + Ncols - 1
NMax = 1
#solo un carro en la visualizacion
letras = []
for k in range(Ncarros):
    for i in range(Nfilas):
        for e in range(Ncols):
            for j in range(NMax):
                v1 = codify.codifica4(k, i,e,j, Ncarros, Nfilas, Ncols, NMax)
                cod = chr(v1+256)
                print(cod, end=" ")
                letras.append(cod)
            print("")


def crear_regla0():
    #cada carro en un solo x, y en dado turno
    iniciaRegla = True
    for  t in range(NMax):
        for c in range(Ncarros):
            for x in range(Ncols):
                for y in range(Nfilas):
                    inicializaClausula = True
                    for i in range(Ncols):
                        for j in range(Nfilas):
                            print("i", i, "j", j)
                            if not(i == 0 and j == 0):
                                if inicializaClausula:
                                    claus = chr(256+codify.codifica4(c,(x+i+1)%Ncols,(y+j+1)%Nfilas,t, Ncarros, Ncols, Nfilas, NMax))
                                    inicializaClausula = False
                                    print("se inicializo la clausula",claus)

                                else:
                                    #a->b = ba->
                                    claus+= chr(256+codify.codifica4(c,(x+i+1)%Ncols,(y+j+1)%Nfilas,t, Ncarros, Ncols, Nfilas, NMax))+ "O"
                                    print("clausula else", claus)
                    #P(c,x,y,t)->¬
                    f = codify.string2Tree(claus, letras)
                    print("aca va la clausula")
                    print(codify.inorder(f))

                    if iniciaRegla:
                        regla = claus+"-"+chr(256+codify.codifica4(c,x,y,t, Ncarros, Ncols, Nfilas, NMax))+">"
                        iniciaRegla = False
                    else:
                        regla += claus+"-"+chr(256+codify.codifica4(c,x,y,t, Ncarros, Ncols, Nfilas, NMax))+">"+"Y"

    return regla



print("***********************************")
print("REGLA 0")
stringRe = crear_regla0()
print(stringRe)
print("************************************")
print("INORDER")

print(codify.inorder(codify.string2Tree(stringRe,letras)))

"""

def crear_regla1():
    #esta regla establece que si un carro toma toma una via, ningun otro puede llegar a tomar la misma
    regla = ""
    #p->q en notacion polca inversa es qp->
    cons =  + "-"


def crear_regla2():
    #corresponde a la regla que hace referencia a que un carro que sale de x_0 lugar debe llegar  a y_1 lugar en t turnos
    cons = ""
    inciar_imp = ""
    for c in range(Ncarros):
        Obj = codify.codifica4(c, x_ob_c1, y_ob_c1, NMax-1, Ncarros, Ncols, Nfilas, NMax)
        inicial_imp = True
        for n in range(NMax):
            inicial_con = True
            for k in range(n + 1,NMax):
                if inicial_con:
                    cons = chr(codify.codifica4(c, x_ob_c1, y_ob_c1, k, Ncarros, Ncols, Nfilas, NMax) + 256)
                    inicial_con = False
                else:
                    cons += chr(codify.codifica4(c, x_ob_c1, y_ob_c1, k, Ncarros, Ncols, Nfilas, NMax) + 256) + "Y"

            if cons != "":
                if inicial_imp:
                    imp = cons + chr(codify.codifica4(c, x_ob_c1, y_ob_c1, n, Ncarros, Ncols, Nfilas, NMax) + 256) + ">"
                else:
                    imp += cons + chr(codify.codifica4(c, x_ob_c1, y_ob_c1, n, Ncarros, Ncols, Nfilas, NMax) + 256) + ">" + "Y"
#cear todas las letras proposicinales

        imp+= chr(Obj+256)+"Y"

    return imp

#cear todas las letras proposicinales



print("***************")

def crear_regla3():
    #esta regla establece que si hay un carro en cierta ubicacion en dado momento el otro no puede estar en esa misma ubicacion en el mismo momentoo

    regla = ""
    #si P(C1,x ,y, n) -> -(P(C2, x, y, n)
    #sin variar el carro
    inicicial_re = True
    inicicial_re2 = True
    for t in range(NMax):
        for x in range(Ncols):
            for y in range(Nfilas):
                if(inicicial_re):
                    ##a->b = >ab =ba->
                    #P Y -(q O r)//YP-Oqr  // p->-q
                    #//>p-q // q-p>
                    claus =  chr(codify.codifica4(0,x,y, t, Ncarros, Ncols, Nfilas, NMax)+ 256)+ "-" +chr(codify.codifica4(1,x,y, t, Ncarros, Ncols, Nfilas, NMax)+ 256)+">"
                    claus += chr(codify.codifica4(1,x,y, t, Ncarros, Ncols, Nfilas, NMax)+ 256)+ "-" +chr(codify.codifica4(0,x,y, t, Ncarros, Ncols, Nfilas, NMax)+ 256)+">" + "Y"
                    inicicial_re = False
                else:
                    claus += chr(codify.codifica4(0,x,y, t, Ncarros, Ncols, Nfilas, NMax)+ 256)+ "-" +chr(codify.codifica4(1,x,y, t, Ncarros, Ncols, Nfilas, NMax)+ 256)+">" + "Y"
                    claus += chr(codify.codifica4(1,x,y, t, Ncarros, Ncols, Nfilas, NMax)+ 256)+ "-" +chr(codify.codifica4(0,x,y, t, Ncarros, Ncols, Nfilas, NMax)+ 256)+">" + "Y"


    return claus




#aca simplemente es una prueba para ver como se decodifica
for l in letras: #corresponde a bien sea
    c,x,y,t = codify.decodifica4(ord(l) - 256, Ncarros, Nfilas, Ncols, NMax)
    print(l, "Se decodifica como:", c, x, y, t)


#prueba para ver si la visualizacion funciona de manera corrrecta
diccionario = {}
for a in letras:
    #si la letra es la que necesito entonces la pongo en uno
    if ord(a) == 256  or a == 'č' or a == 'Ĝ':
        diccionario[a] = 1

    else:
        diccionario[a] = 0






vs.showIt(diccionario)

"""
