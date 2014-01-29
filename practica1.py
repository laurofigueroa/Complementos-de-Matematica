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

    for v in V:
        aux = []
        for a in E:
#           esta = int(j[0] == i or j[1] == i)
            if v in a:
                if v == a[0] and v == a[1]:
                    aux.append(2)
                elif v == a[0]:
                    aux.append(-1)
                else:
                    aux.append(1)
            else:
                aux.append(0)          
        matriz.append(aux)

    return (matriz, V)
 
def incidenciaALista(grafoIncidencia):
    '''
    Transforma un grafo representado una matriz de incidencia a su 
    representacion por listas.
    '''
    matriz = grafoIncidencia[0]
    V = grafoIncidencia[1]
    
    E = []
    aux = []
    
    for j in range(len(matriz[0])):
        for i, v in enumerate(V):
            if matriz[i][j] == -1:
                aux.insert(0, v)
            if matriz[i][j] == 1:
                aux.append(v)
            if matriz[i][j] == 2:
                aux = [v,v] 
        if aux != []:
          E.append(tuple(aux))
          aux = []
    return (V,E)
                
        
def imprimeGrafoIncidencia(grafoIncidencia):
    '''
    Muestra por pantalla un grafo. 
    El argumento esta en formato de matriz de incidencia.
    '''
    matriz = grafoIncidencia[0]
    V = grafoIncidencia[1]

    for i,fila in enumerate(matriz):
        print fila,V[i]



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
          if (int((i,j) in E)) or (int((j,i) in E)):
            aux.append(int('1'))
          else:
            aux.append(int('0'))
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
              if not((V[j], V[i]) in E):
                    E.append((V[i], V[j]))            
    return (V,E)



def imprimeGrafoAdyacencia(grafoAdyacencia):
    '''
    Muestra por pantalla un grafo. 
    El argumento esta en formato de matriz de adyacencia.
    '''
    matriz = grafoAdyacencia[0]
    V = grafoAdyacencia[1]

    size = len(V)
    tmp = size

    print (""),
    while size > 0:
        print V[tmp - size], "",
        size = size - 1
    print('')

    size = tmp
    while size > 0:
        # print matriz[size-tmp-1], V[size-1]
        print matriz[tmp - size], V[tmp - size]
        size = size - 1


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
        V.append(line)
    
    while(True):
        line = entrada.readline()[:-1]
        aux = (line.split(' '))
        if (len(aux) < 2):
            break
        E.append((aux[0],aux[1]))

    entrada.close()

    return (V,E)



def main():

#    grafo = leerGrafoStdin()
#    imprimeGrafoLista(grafo)
   
    grafo = leerGrafoArchivo("grafo2.txt")
    print grafo

    # Adyacencia #
    print "Grafo original", grafo
    matriz = listaAAdyacencia(grafo)
    imprimeGrafoAdyacencia(matriz)
    g = adyacenciaALista(matriz)
    print g

    # Incidencia #
    print "Grafo original", grafo
    ady = listaAIncidencia(grafo)
    imprimeGrafoIncidencia(ady)
    g2 = incidenciaALista(ady)
    print g2
if __name__ == "__main__":
    main()

