

class Tree:
    def __init__(self, pLabel, pLeft, pRight):
        self.label = pLabel
        self.left = pLeft
        self.right = pRight


def codifica(f, c, Nf, Nc):
    # Funcion que codifica la fila f y columna c

    assert((f >= 0) and (f <= Nf - 1)), 'Primer argumento incorrecto! Debe ser un numero entre 0 y ' + str(Nf) - 1  + "\nSe recibio " + str(f)
    assert((c >= 0) and (c <= Nc - 1)), 'Segundo argumento incorrecto! Debe ser un numero entre 0 y ' + str(Nc - 1)  + "\nSe recibio " + str(c)

    n = Nc * f + c
    # print(u'Número a codificar:', n)
    return n



"""
Esta parte se encarga de crear las letras proposicinales

c: el carro uno o al dos
x: pos en x coordenada
y: pos en y coordenada
t: el turno como tal

"""

def codifica4(c, x, y, t, Nc, Nx, Ny, Nt):
    # Funcion que codifica tcuatroargumentos
    assert((c >= 0) and (c <= Nc - 1)), 'Primer argumento incorrecto! Debe ser un numero entre 0 y ' + str(Nf - 1) + "\nSe recibio " + str(f)
    assert((x >= 0) and (x <= Nx - 1)), 'Segundo argumento incorrecto! Debe ser un numero entre 0 y ' + str(Nc - 1) + "\nSe recibio " + str(c)
    assert((y >= 0) and (y <= Ny - 1)), 'Tercer argumento incorrecto! Debe ser un numero entre 0 y ' + str(No - 1)  + "\nSe recibio " + str(o)
    assert((t >= 0) and (t <= Nt - 1)), 'Cuarto argumento incorrecto! Debe ser un numero entre 0 y ' + str(No - 1)  + "\nSe recibio " + str(o)
    v1 = codifica(c, x, Nc, Nx)
    v2 = codifica(v1, y, Nc * Nx, Ny)
    v3 = codifica(v2, t, Nc * Nx * Ny, Nt)
    return v3



def decodifica(n, Nf, Nc):
    # Funcion que codifica un caracter en su respectiva fila f y columna c de la tabla

    assert((n >= 0) and (n <= Nf * Nc - 1)), 'Codigo incorrecto! Debe estar entre 0 y' + str(Nf * Nc - 1) + "\nSe recibio " + str(n)

    f = int(n / Nc)
    c = n % Nc
    return f, c

def decodifica4(j, Nc, Nx, Ny, Nt):
    # Funcion que codifica un caracter en su respectiva fila f, columna c y objeto o
    v1, t = decodifica(j, Nc * Ny* Nx, Nt)
    v2, y = decodifica(v1, Nc * Nx, Ny)
    c , x = decodifica(v2,Nc, Nx )

    return c,x,y,t

def inorder(arb):
    #retrona un string con como se deberia ber la formula de un arbol
    if arb.right == None:
        return arb.label
    elif arb.label == "-":
        return "-" + inorder(arb.right)
    else:
        return "(" + inorder(arb.left) + arb.label + inorder(arb.right)+ ")"


#Transformar las cadenas en arboles

def string2Tree(A, letrasProposicionales):
    #Crea una formula como tree dada una formula
    #como cadena escritra en notacion POLACA INVERSA
    #Input: A, Lista de caracteres con una formula escrita en notacon polaca iinversa
    #LetrasProposicionales, lista de letras proposicionales
    #output: formula como tree
    conectivos= ['O', 'Y', '>']
    pila = []
    for c in A:

        if c in letrasProposicionales:
            pila.append(Tree(c, None, None))
            #print(inorder(Tree(c,None,None)))
        elif c == "-":
            FormulaAux = Tree(c, None, pila[-1])
            del pila[-1]
            pila.append(FormulaAux)
        elif c in conectivos:
            FormulaAux = Tree(c, pila[-1], pila[-2])
            del pila[-1]
            del pila[-1]
            pila.append(FormulaAux)

    return pila[-1]

