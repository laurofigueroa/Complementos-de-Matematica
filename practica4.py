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
  while no_proc != []:
    minimo = [None, None, None]
    for v1 in sol:
      for v2 in no_proc:
        for e in E:
          if (v1 == e[0] and v2 == e[1]) or (v1 == e[1] and v2 == e[0])and not((v1 == minimo[0] and v2 == minimo[1]) or (v1 == minimo[1] and v2 == minimo[0])):
            if minimo[2] == None:
              minimo = [v1, v2, e[2]]
            if minimo[2] > e[2] :
              minimo = [v1, v2, e[2]]

    sol.append(minimo[1])
    del no_proc[no_proc.index(v2)]
    aristas.append(tuple(minimo))

  return aristas


def kruskal(grafo):
  '''
  Dado un grafo (en formato de listas con pesos), aplica el algoritmo de 
  Kruskal y retorna el MST correspondiente (o un bosque, en el caso de que 
  no sea conexo).
  '''
  pass

def main():

  g = leeGraphML("myGraph.graphml")
  print g
  aristas = prim(g)
  print aristas
  

if __name__ == "__main__":
    main()
