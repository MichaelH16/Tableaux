# -*- coding: utf-8 -*-

# Subrutinas para la transformacion de una
# formula a su forma clausal

# Subrutina de Tseitin para encontrar la FNC de
# la formula en la pila
# Input: A (cadena) de la forma
#                   p=-q
#                   p=(qYr)
#                   p=(qOr)
#                   p=(q>r)
# Output: B (cadena), equivalente en FNC
def enFNC(A):
    assert(len(A)==4 or len(A)==7), u"Fórmula incorrecta!"
    B = ''
    p = A[0]
    # print('p', p)
    if "-" in A:
        q = A[-1]
        # print('q', q)
        B = "-"+p+"O-"+q+"Y"+p+"O"+q
    elif "Y" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = q+"O-"+p+"Y"+r+"O-"+p+"Y-"+q+"O-"+r+"O"+p
    elif "O" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = "-"+q+"O"+p+"Y-"+r+"O"+p+"Y"+q+"O"+r+"O-"+p
    elif ">" in A:
        q = A[3]
        # print('q', q)
        r = A[5]
        # print('r', r)
        B = q+"O"+p+"Y-"+r+"O"+p+"Y-"+q+"O"+r+"O-"+p
    else:
        print(u'Error enENC(): Fórmula incorrecta!')

    return B

# Algoritmo de transformacion de Tseitin
# Input: A (cadena) en notacion inorder
# Output: B (cadena), Tseitin
def Tseitin(A, letrasProposicionalesA):
    letrasProposicionalesB = [chr(x) for x in range(256, 1200)]
    assert(not bool(set(letrasProposicionalesA) & set(letrasProposicionalesB))), u"¡Hay letras proposicionales en común!"

    #  IMPLEMENTAR AQUI ALGORITMO TSEITIN
    L = [] #inicializamos lista de conjunciones
    Pila = [] #inicializacmos pila
    I = -1 #inicializacoms contador de variables nuevas
    s = A[0] #inicializamos simbolos de trabajo
    while(len(A) > 0):
        #si es es un atomo
        #print(len(A))
        if (s in letrasProposicionalesA) and Pila != [] and Pila[-1] == '¬':
            print("entra")
            I+=1
            Atomo = LetrasProposicionalesB[I]
            Pila = Pila[:-1]
            Pila.append(Atomo)
            #
            L.append(Atomo +"@¬"+s)
            A = A[1:]
            if len(A)>0:
                s = A[0]
        elif s == ')':
            w = Pila[-1]
            u = Pila[-2]
            v = Pila[-3]
            Pila = Pila[:len(Pila)-4]
            I += 1
            Atomo = letrasProposicionalesB[I]
            #
            L.append(Atomo +"@("+v+u+w+')')
            s = Atomo
        else:
            Pila.append(s)
            A = A[1:]
            if len(A) > 0:
                s = A[0]
    b = ""
    if I < 0:
        Atomo = Pila[-1]
    else:
        Atomo = letrasProposicionalesB[I]

    for x in L:
        Y = enFNC(x) #es su respectiva FNC
        #print("b", b)
        #print("y", Y)
        b += "Y" +Y

    b = Atomo + b
    return b

# Subrutina Clausula para obtener lista de literales
# Input: C (cadena) una clausula
# Output: L (lista), lista de literales
# Se asume que cada literal es un solo caracter
def Clausula(C):

    #  IMPLEMENTAR AQUI ALGORITMO CLAUSULA
    pass

# Algoritmo para obtencion de forma clausal
# Input: A (cadena) en notacion inorder en FNC
# Output: L (lista), lista de listas de literales
def formaClausal(A):

    #  IMPLEMENTAR AQUI ALGORITMO FORMA CLAUSAL
    pass
