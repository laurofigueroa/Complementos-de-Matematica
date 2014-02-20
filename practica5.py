#! /usr/bin/python

# 5ta Practica Laboratorio 
# Complementos Matematicos I
# Consigna: Implementar los siguientes metodos

import sys
from practica3 import*

def dijkstra(grafo, vertice):
  '''
  Dado un grafo (en formato de listas con pesos), aplica el algoritmo de 
  Dijkstra para hallar el COSTO del camino mas corto desde el vertice de origen
  al resto de los vertices.
  '''
  pass

def dijkstra2(grafo, vertice):
  '''
  Dado un grafo (en formato de listas con pesos), aplica el algoritmo de 
  Dijkstra para hallar el CAMINO mas corto desde el vertice de origen
  a cada uno del resto de los vertices.
  '''
  dist = {}
  padre = {}
  for v in grafo[0]:
    dist[v] = None
    padre[v] = None
  dist[vertice] = 0

  cola = grafo[0] 

  while cola != []:
    minimo = (None, None)
    for tupla in dist.items():
      if minimo[1] == None and tupla[1] != None and tupla[0] in cola:
        minimo = tupla
      elif minimo[1] != None and tupla[1] != None and minimo[1] > tupla[1] and tupla[0] in cola:
        minimo = tupla

    u = minimo[0] #vertice
    cola.remove(u)

    if dist[u] == None:
      break
  
    vecinos = adyacentes(grafo[1], cola, u) 
    for v in vecinos:
      alt = dist[u] + peso(grafo[1], v, u)
      if dist[v] == None:
        dist[v] = alt
        padre[v] = u
      if (alt < dist[v]):
        dist[v] = alt
        padre[v] = u

  return (dist, padre)


def peso(E, v1, v2):
  for e in E:
    if (e[0] == v1 and e[1] == v2) or (e[0] == v2 and e[1] == v1):
      return e[2]


def adyacentes(E, vertices, vertice): #devuelve una lista de vetices adyacentes
  res = []
  for e in E:
    if e[0] == vertice or e[1] == vertice:
      if e[0] == vertice and e[1] in vertices:
        res.append(e[1])
      elif e[1] == vertice and e[0] in vertices:
        res.append(e[0])

  return res



def main():

  g = leerGrafoPesoArchivo("grafo5.txt")
  print g
  res = dijkstra2(g, '1')
  print res

if __name__ == "__main__":
    main()
