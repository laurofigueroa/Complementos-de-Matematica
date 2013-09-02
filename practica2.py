#! /usr/bin/python

# 2da Practica Laboratorio 
# Complementos Matematicos I
# Consigna: Implementar los siguientes metodos

# Un disjointSet lo representaremos como un diccionario. 
# Ejemplo: {"A":1, "B":2, "C":1} (Nodos A y C pertenecen al conjunto 
# identificado con 1, B al identificado on 2)

import practica1

def set(lista):
    '''
    Inicializa un conjunto (Lista) de modo de que todos sus elementos pasen 
    a ser conjuntos unitarios. 
    Retorna un disjointSet
    '''
    dijointSet = dict([(i,x) for x, i in enumerate(lista) ])
    return dijointSet

def find(elem, disjointSet):
    '''
    Obtiene el identificador correspondiente al conjunto al que pertenece 
    el elemento 'elem'
    '''
    if elem in disjointSet:
        return disjointSet[elem]    
    else:
        print "ERROR - Elemento {0} no se encuentra en dijointSet".format(elem)

def union(id1, id2, disjointSet):
    '''
    Une los conjuntos con identificadores id1, id2.
    Retorna la estructura actualizada
    '''
#    print id1
#    print id2
    for clave, valor in disjointSet.iteritems():
        if id1 == valor:
            disjointSet[clave] = id2
            return disjointSet
        elif id2 == valor:
            disjointSet[clave] = id1
            return disjointSet
    print "ERROR - Alguna de las claves ingresados no se encuentra en disjointSet"

def componentesConexas(grafoLista):
    '''
    Dado un grafo en representacion de lista, obtiene sus componentes conexas
    '''
    disjointSet = set (grafoLista[0])
    print disjointSet
    aristas = grafoLista[1]

    for a in aristas:
#        print "a[0] = {0} - a[1] = {1}".format(a[0],a[1])
#        print a[0] 
	id1 = find(a[0],disjointSet)
        id2 = find(a[1],disjointSet)
        if id1 != id2:
            union (id1,id2,disjointSet)

    return disjointSet

def main():
    leerGrafoArchivo = practica1.leerGrafoArchivo

    grafoLista = leerGrafoArchivo("grafo.txt")
    print grafoLista
#    dis = set(grafoLista[0])
#    print dis
#    print find("a",dis)
#    print find("b",dis)
#    print find("c",dis)
#    print find("C",dis)

#    dis = union("a","b",dis)
#    print dis

    disjointSet = componentesConexas(grafoLista)
    print disjointSet

if __name__ == "__main__":
    main()
