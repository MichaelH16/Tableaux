
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
Nfilas = 3
Ncols = 3
#numero de carros
Ncarros = 2
#cuantos tuernos maximos hay
NMax = Nfilas - 1 + Ncols - 1



def crear_regla1():
    #esta regla establece que si un carro toma toma una via, ningun otro puede llegar a tomar la misma
    regla = ""
    #p->q en notacion polca inversa es qp->
    cons =  + "-"

def crear_regla2():
    #corresponde a la regla que hace referencia a que un carro que sale de x_0 lugar debe llegar  a y_1 lugar en t turnos
    for c in range(2):
        Obj = codifica4(c, x_ob_c1, y_ob_c1, NMax)
        inicial_imp = True
        for n in range(NMax):
            inicial_con = True
            for k in range(n + 1:NMax):
                if inicial_con:
                    cons = chr(codifica4(c, x_ob_c1, y_ob_c1, k) + 256)
                    inicial_con = False
                else:
                    cons += chr(codifica4(c, x_ob_c1, y_ob_c1, k) + 256) + "Y"

            if inicial_imp:
                imp = cons + chr(codifica4(c, x_ob_c1, y_ob_c1, n) + 256) + ">"
            else:
                imp += cons + chr(codifica4(c, x_ob_c1, y_ob_c1, n) + 256) + ">" + "Y"
#crear todas las letras proposicinales
"""
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


print("***************")



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
