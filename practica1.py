#! /usr/bin/python

# 1ra Practica Laboratorio 
# Complementos Matematicos I
# Consigna: Implementar los siguientes metodos

import sys

def leerGrafoStdin():
    '''
    Lee un grafo desde entrada estandar y devuelve su representacion como lista.
    Ejemplo Entrada: 
        3
        "A"
        "B"
        "C"
        "A" "B"
        "B" "C"
        "C" "B"
    Ejemplo retorno: 
        (["A","B","C"],[("A","B"),("B","C"),("C","B")])
    '''
    vertices = int(raw_input("Ingrese la cantidad de vertices: "));
    E = []
    V = []

    for i in range(vertices):
        line = raw_input()
        V.append(line)
    try:
    	while(True):
            line = raw_input()
#      		E.append((line.split(' ')))
            aux = (line.split(' '))
            E.append((aux[0],aux[1]))
    except (EOFError):
            pass

    return (V,E)


def imprimeGrafoLista(grafo):
    '''
    Muestra por pantalla un grafo. El argumento esta en formato de lista.
    '''
    print grafo


def listaAIncidencia(grafoLista):
    '''
    Transforma un grafo representado por listas a su representacion 
    en matriz de incidencia.
    '''

    V = grafoLista[0]
    E = grafoLista[1]
    
    matriz = []
    esta = 0

    for i in V:
        aux = []
        for j in E:
           esta = int(j[0] == i or j[1] == i)
           aux.append(esta)
        matriz.append(aux)

    return matriz
 
def incidenciaALista(grafoIncidencia):
    '''
    Transforma un grafo representado una matriz de incidencia a su 
    representacion por listas.
    '''
    pass


def imprimeGrafoIncidencia(grafoIncidencia):
    '''
    Muestra por pantalla un grafo. 
    El argumento esta en formato de matriz de incidencia.
    '''
    pass


def listaAAdyacencia(grafoLista):
    '''
    Transforma un grafo representado por listas a su representacion 
    en matriz de adyacencia.
    '''
    V = grafoLista[0]
    E = grafoLista[1]

    matriz = []
    
    for i in V:
        aux = []
        for j in V:
	    aux.append(int((i,j) in E))
        matriz.append(aux)           
    return (matriz,V)


def adyacenciaALista(grafoAdyacencia):
    '''
    Transforma un grafo representado una matriz de adyacencia a su 
    representacion por listas.
    '''
    matriz = grafoAdyacencia[0]
    V = grafoAdyacencia[1]
    E = []
    size = len(V)
    for i in range(size):
        for j in range(size):
            if matriz[i][j] == 1:
                E.append((V[i], V[j]))            
    return (V,E)



def imprimeGrafoAdyacencia(grafoAdyacencia):
    '''
    Muestra por pantalla un grafo. 
    El argumento esta en formato de matriz de adyacencia.
    '''
    pass


def leerGrafoArchivo(file):
    '''
    Lee un grafo desde un archivo y devuelve su representacion como lista.
    Ejemplo Entrada: 
        3
        "A"
        "B"
        "C"
        "A" "B"
        "B" "C"
        "C" "B"
    Ejemplo retorno: 
        (["A","B","C"],[("A","B"),("B","C"),("C","B")])
    '''
    entrada = open(file,'r')
    
    vertices = int(entrada.readline())


    E = []
    V = []

    for i in range(vertices):
        line = entrada.readline()[:-1]
#        print "Este es [" + line + "]"
        V.append(line)
    
    while(True):
        line = entrada.readline()[:-1]
#           print "Este es [" + line + "]"
#      		E.append((line.split(' ')))
#            print "Este es " + str(line)
        aux = (line.split(' '))
        if (len(aux) < 2):
            break
        E.append((aux[0],aux[1]))

    entrada.close()

    return (V,E)



def main():

#   grafo = leerGrafoStdin()
#    print grafo
#    imprimeGrafoLista(grafo)
   
#    listaAIncidencia(grafo)
#    matriz = listaAAdyacencia(grafo)
#    grafo2= adyacenciaALista(matriz)
#    imprimeGrafoLista(grafo2)
#    grafo = leerGrafoArchivo("grafo.txt")
#    print grafo
    pass

if __name__ == "__main__":
    main()
