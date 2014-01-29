#! /usr/bin/python

# 3ra Practica Laboratorio 
# Complementos Matematicos I
# Consigna: Implementar los siguientes metodos


# Referencias:
# pygraphMl    : http://hadim.github.io/pygraphml/usage.html
# GraphML      : http://graphml.graphdrawing.org/
# XML          : http://www.w3schools.com/xml/
# Editores     : http://www.cs.bilkent.edu.tr/~ivis/layout/demo/lw1x.html
#                http://cytoscapeweb.cytoscape.org/demo
#                http://cytoscape.org/
# elementTree  : http://docs.python.org/2/library/xml.etree.elementtree.html 

import sys
import pygraphml

from pygraphml.GraphMLParser import *
from pygraphml.Graph import *
from pygraphml.Node import *
from pygraphml.Edge import *


def leerGrafoPesoStdin():
    '''
    Lee un grafo desde entrada estandar y devuelve su representacion como lista.
    Ejemplo Entrada: 
        3
        "A"
        "B"
        "C"
        "A" "B" 2.1
        "B" "C" -3
        "C" "B"
    Ejemplo retorno: 
        (["A","B","C"],[("A","B", 2.1),("B","C", -3),("C","B", None)])
    '''

    vertices = int(raw_input())
    E = []
    V = []

    for i in range(vertices):
        line = raw_input()
        V.append(line)

    try:
        while(True):
            line = raw_input()
            aux = (line.split(' '))
            if len(aux) < 3:
                E.append((aux[0], aux[1], None))
            else:
                E.append((aux[0], aux[1], float(aux[2])))
    except (EOFError):
            pass


    return (V,E)


def imprimeGrafoPesoLista(grafo):
    '''
    Muestra por pantalla un grafo. El argumento esta en formato de lista.
    '''
    print grafo


def leerGrafoPesoArchivo(file):
    '''
    Lee un grafo desde un archivo y devuelve su representacion como lista.
    Ejemplo Entrada: 
        3
        "A"
        "B"
        "C"
        "A" "B" 2.1
        "B" "C" -3
        "C" "B"
    Ejemplo retorno: 
        (["A","B","C"],[("A","B", 2.1),("B","C", -3),("C","B", None)])
    '''

    entrada = open(file,'r')
    
    vertices = int(entrada.readline())


    E = []
    V = []

    for i in range(vertices):
        line = entrada.readline()[:-1]
        V.append(line)
    
    while(True):
        line = entrada.readline()[:-1]
        aux = (line.split(' '))
        if (len(aux) < 2):
            break
        if len(aux) < 3:
            E.append((aux[0], aux[1], None))
	else:
            E.append((aux[0], aux[1], float(aux[2])))

    entrada.close()

    return (V,E)

def leeGraphML(file):
    '''
    Lee un grafo en formato graphML usando la libreria pygraphMl, 
    y lo devuelve como lista con pesos
    '''

    parser = GraphMLParser()
    g = parser.parse(file)

    V = []
    E = []

    for node in g.nodes():
        V.append(node['label'])

    for e in g.edges():
       source = e.node1
       target = e.node2
       try:
           peso = float(e['d1'])
       except:
            peso = None 
       E.append((source['label'], target['label'], peso))

    return (V,E)
 

def leeGraphML2(file):
    '''
    OPCIONAL
    Lee un grafo en formato graphML, recorriendo el XML con la libreria 
    elementTree (xml.etree.ElementTree), y lo devuelve como lista con pesos
    '''
    pass

def main():
#     g = leerGrafoPesoStdin()
#     print g    
#    g = leerGrafoPesoArchivo("grafo3.txt")
#    print g

    g = leeGraphML("myGraph.graphml")
    print g


if __name__ == "__main__":
    main()
