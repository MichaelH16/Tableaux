#-*-coding: utf-8-*-
from random import choice
##############################################################################
# Variables globales
##############################################################################

# Crea las letras minúsculas a-z
letrasProposicionales = [chr(x) for x in range(97, 123)]
# inicializa la lista de interpretaciones
listaInterpsVerdaderas = []
# inicializa la lista de hojas
listaHojas = []

letrasProposicionales2 = ['p','-p']
##############################################################################
# Definición de objeto tree y funciones de árboles
##############################################################################

class Tree(object):
	def __init__(self, label, left, right):
		self.left = left
		self.right = right
		self.label = label

def Inorder(f):
    # Imprime una formula como cadena dada una formula como arbol
    # Input: tree, que es una formula de logica proposicional
    # Output: string de la formula
	if f.right == None:
		return f.label
	elif f.label == '-':
		return f.label + Inorder(f.right)
	else:
		return "(" + Inorder(f.left) + f.label + Inorder(f.right) + ")"

def StringtoTree(A):
    # Crea una formula como tree dada una formula como cadena escrita en notacion polaca inversa
    # Input: A, lista de caracteres con una formula escrita en notacion polaca inversa
             # letrasProposicionales, lista de letras proposicionales
    # Output: formula como tree

	# OJO: DEBE INCLUIR SU CÓDIGO DE STRING2TREE EN ESTA PARTE!!!!!

	p = letrasProposicionales[0] # ELIMINE ESTA LINEA LUEGO DE INCLUIR EL CODIGO DE STRING2TREE
	return Tree(p, None, None) # ELIMINE ESTA LINEA LUEGO DE INCLUIR EL CODIGO DE STRING2TREE

##############################################################################
# Definición de funciones de tableaux
##############################################################################

def imprime_hoja(H):
	cadena = "{"
	primero = True
	for f in H:
		if primero == True:
			primero = False
		else:
			cadena += ", "
		cadena += Inorder(f)
	return cadena + "}"

def par_complementario(l):
	# Esta función determina si una lista de solo literales
	# contiene un par complementario
	# Input: l, una lista de literales
	# Output: True/False
	for i in range(0,len(l)-1):
		if len(l[i]) == 1: #compruebo si el primer elemento es una letra proposicional sin negar
			for j in range(i+1, len(l)):
				s = '-'+ l[i] #S es  una variable donde describe la negacion de la letra escogida.
				if l[j] == s: # se comprueba si la letra escogida es igual a su negacion
					return True
		if len(l[i]) == 2: #Se define si la letra escogida es una negacion.
			for k in range(i+1, len(l)):
				if l[i][1] == l[k]:# Se compueba si la latra escogida es igual a su negacion es decir la letra normal.
					return True
	return False
	
def es_literal(f):
	# Esta función determina si el árbol f es un literal
	# Input: f, una fórmula como árbol
	# Output: True/False
	return False

def no_literales(l):
	# Esta función determina si una lista de fórmulas contiene
	# solo literales
	# Input: l, una lista de fórmulas como árboles
	# Output: None/f, tal que f no es literal
	return False

def clasifica_y_extiende(f):
	# clasifica una fórmula como alfa o beta y extiende listaHojas
	# de acuerdo a la regla respectiva
	# Input: f, una fórmula como árbol
	# Output: no tiene output, pues modifica la variable global listaHojas
	global listahojas
    if f.label == '-':
        if f.right.label == '-':
            for l in listahojas:
                for old in l:
                    if old.right.label == f.right.label and old.right.left.label == f.right.left.label and old.right.right.label == f.right.right.label:
                        l.remove(old)
                        l.append([f.right.right])
        elif f.right.label == 'O':
            for l in listahojas:
                for old in l:
                    if old.right != None:
                        if old.right.label == f.right.label and old.right.left.label == f.right.left.label and old.right.right.label == f.right.right.label :
                            l.remove(old)
                            l.append(Tree('-',None,f.right.left))
                            l.append(Tree('-',None,f.right.right))
        elif f.right.label == '->':
            for l in listahojas:
                for old in l:
                    if old.right != None:
                        if old.right.label == f.right.label and old.right.left.label == f.right.left.label and old.right.right.label == f.right.right.label :
                            l.remove(old)
                            l.append(f.right.left)
                            l.append(Tree('-',None,f.right.right))
        elif f.right.label == 'Y':
            valores = []
            for l in listahojas:
                for old in l:
                    valores.append(old)
                    if old.right.label == f.right.label and old.right.left.label == f.right.left.label and old.right.right.label == f.right.right.label :
                        l.remove(old)
                        valores = l[:]
                        l.append(Tree('-',None,f.right.left))
                        valores.append(Tree('-',None,f.right.right))
            listahojas.append(valores)

    elif f.label == 'Y':
        for l in listahojas:
            for old in l:
                if old.label == f.label and old.left.label == f.right.left.label and old.right.label==f.right.right.label:
                    l.remove(old)
                    l.append(f.left)
                    l.append(f.right)
    
    elif f.label == 'O':
        valores = []
        for l in listahojas:
            for old in l:
                if old.label == f.label and old.left.label == f.right.left.label and old.right.label==f.right.right.label:
                    l.remove(old)
                    valores = l[:]
                    l.append(f.left)
                    valores.append(f.right)
        listahojas.append(valores)
    elif f.label == '->':
        valores = []
        for l in listahojas:
            for old in l:
                if old.label == f.label and old.left.label == f.left.label and old.right.label==f.right.label:
                    l.remove(old)
                    valores = l[:]
                    l.append(Tree('-',None,f.right.left))
                    valores.append(f.right.right)
                valores.append(old)
        listahojas.append(valores)

def Tableaux(f):

	# Algoritmo de creacion de tableau a partir de lista_hojas
	# Imput: - f, una fórmula como string en notación polaca inversa
	# Output: interpretaciones: lista de listas de literales que hacen
	#		 verdadera a f
	global listaHojas
	global listaInterpsVerdaderas

	A = string2Tree(f)
	listaHojas = [[A]]

	return listaInterpsVerdaderas
