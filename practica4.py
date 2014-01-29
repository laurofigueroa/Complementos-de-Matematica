#! /usr/bin/python

# 4ta Practica Laboratorio 
# Complementos Matematicos I
# Consigna: Implementar los siguientes metodos

from practica3 import*

def prim(grafo):
  '''
  Dado un grafo (en formato de listas con pesos), aplica el algoritmo de Prim
  y retorna el MST correspondiente. 
  NOTA: El grafo de entrada se asume conexo.
  '''
  V = grafo[0]
  E = grafo[1]

  if V == []:
    print "ERROR, GRAFO VACIO - PRIM"
    return

  aristas = []
  sol = [V[0]]

  no_proc = V[1:]
  minimo = [None, None, None]
  while no_proc != []:
    for v1 in sol:
      for v2 in no_proc:
        for e in E:
#          print v1, v2, e
#          print minimo
          if ((v1 == e[0] and v2 == e[1]) or (v1 == e[1] and v2 == e[0])):
              if minimo[2] == None:
                minimo = [v1, v2, e[2]]
#              elif((v1 == minimo[0] and v2 == minimo[1]) or (v1 == minimo[1] and v2 == minimo[0])):
              if minimo[2] > e[2] and e[2] != None :
                minimo = [v1, v2, e[2]]

    if minimo[1] == None:
      break
#    print minimo[1]
#    print no_proc
    no_proc.remove(minimo[1])
    sol.append(minimo[1])
#    print no_proc
    aristas.append(tuple(minimo))
#    print sol, no_proc, aristas
    minimo = [None, None, None]

  return aristas


def kruskal(grafo):
  '''
  Dado un grafo (en formato de listas con pesos), aplica el algoritmo de 
  Kruskal y retorna el MST correspondiente (o un bosque, en el caso de que 
  no sea conexo).
  '''

  sol = []
  E = grafo[1]
  disjoinSet = set(grafo[0])

  while True:
    ordenado = 1
    for i in range(len(E)-1):
      if E[i][2] > E[i+1][2]:
        aux = E[i]
        E[i] = E[i+1]
        E[i+1] = aux
        ordenado = 0
    if ordenado == 1:
      break

  for e in E:
    if disjoinSet[e[0]] != disjoinSet[e[1]]:
      sol.append(e)

  return sol

def main():

  g = leeGraphML("myGraph.graphml")
  print g
  aristas = prim(g)
  print aristas
  g = leerGrafoPesoArchivo("grafo3.txt")
  print g
  aristas = prim(g)
  print aristas
  
  aristas = kruskal(g)
  print aristas

if __name__ == "__main__":
    main()
