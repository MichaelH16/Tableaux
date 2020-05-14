# -*- coding: utf-8 -*-
"""
Created on Sun May 10 18:07:28 2020

@author: ACER
"""
import copy 


def is_unit_cl(lista):
    for l in lista:
        if len(l) == 1:
            return True
        elif len(l) == 2 and l[0]== "-":
            return True
    return False


def complemento(n):
	x = n
	if x[0] == '-':
		return x[1]
	else:
		return '-' + x


def unit_propagate(S, I):
    c_vacia = []
    aux = is_unit_cl(S)
    while(c_vacia not in S and aux):
        for n in S:
            if len(n) == 1:
                l = n[0]
            elif len(n) == 2 and n[0] == "-":
                l = n[0] + n[1]
        T = []
        for y in S:
            if l not in y:
                T.append(y)
        S = copy.deepcopy(T)
        for w in S:
            if complemento(l) in w:
                w.remove(complemento(l))
        if l[0] == '-':
            I[l[1]] = 0
        else:
            I[l] = 1
        aux = is_unit_cl(S)
    return S, I

def DPLL(S, I):
    S, I = unit_propagate(S, I)
    c_vacia = []
    if c_vacia in S:
        return "Es Insatisfacible!", {}
    
    elif len(S) == 0:
        return "Es Satisfacible!", I
    l = ""
    for clausula in S:
        for literal in clausula:
            if literal not in I.keys():
                l = literal
                break
    lBarra = complemento(l)
    
    if l == "":
        print("Error: ya se obtuvo una interpretacion")
        return None
    Sp = copy.deepcopy(S)
    Sp = [clausula for clausula in Sp if not l in clausula]
    
    for c in Sp:
        if lBarra in c:
            c.remove(lBarra)	
    Ip = copy.deepcopy(I)
    
    if l[0] == '-':
        Ip[l[1]] = 0
    else:
        Ip[l] = 1
    S1, I1 = DPLL(Sp, Ip)
    
    if S1 == "Es Satisfacible!":
        return S1, I1
    else:
        Spp = copy.deepcopy(S)
        for clausula in Spp:
            if complemento(l) in clausula:
                Spp.remove(clausula)
        for clausula in Spp:
            if l in clausula:
                clausula.remove(l)
        
        Ipp = copy.deepcopy(I)
        if l[0] == '-':
            Ipp[l[1]] = 1
        else:
            Ipp[l] = 0
        return DPLL(Spp, Ipp)


#S1 = [['p','q','-r'], ['r','s','t'],  ['t'] , ['p', 's'] , ['q', '-p']]
#prueba1 = DPLL(S1, {})
#print("prueba1: ", prueba1)
#
#S2 = [['p','q','r','-s'], ['p','t','s'],  ['-p','-q'] ,  ['p','r','-q','-s']]
#prueba2 = DPLL(S2, {})
#print("prueba1: ", prueba2)
#
#S3 = [['p','q','r'], ['-p','-q','-r'],  ['-p','q','r'] , ['-q', 'r'] , ['q', '-r']]
#prueba3 = DPLL(S3,{})
#print("prueba 3: " , prueba3)
#
#S4 = [['p','-q'], ['-p','-q']  , ['q','r'], ['-q', '-r'] ,['-p','-r'],['p','-r'] ]
#prueba4 = DPLL(S2, {})
#print("prueba2: ", prueba4)
#



