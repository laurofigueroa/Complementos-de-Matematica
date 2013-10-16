#! /usr/bin/python

# 5ta Practica Laboratorio 
# Complementos Matematicos I
# Consigna: Implementar los siguientes metodos


def dijkstra(grafo, vertice):
  '''
  Dado un grafo (en formato de listas con pesos), aplica el algoritmo de 
  Dijkstra para hallar el COSTO del camino mas corto desde el vertice de origen
  al resto de los vertices.
  '''
  V = grafo[0]
  E = grafo[1]

  dist = {}
  previous = {}

  for v in V:
    dist[v] = None
    previous[v] = None

  dist[vertice] = 0
  Q = V

  while Q != []:
    minimo = [None, None]
    for tupla in dist.items():
      if (tupla[1] != None and minimo[1] == None) or (tupla[1] < minimo[1]):
        minimo[0] = tupla[0]
        minimo[1] = tupla[1]
    
    u = minimo[0]
    Q.remove(u)
    if dist[u] == None:
      break
    
    for vecino in vecionos(grafo, u):
      for arista in E:
        if (vecino == arita[0] and u == arista[1]) or (u == arista[0] and veciono == arista[1]):
          peso = arista[2]
      alt = dist[u] + peso
      if atl < dist[vecino]:
        dist[vecino] = alt
        previous[vecino] = u
        Q.remove(vecino)
  
  return dist

def dijkstra2(grafo, vertice):
    '''
    Dado un grafo (en formato de listas con pesos), aplica el algoritmo de 
    Dijkstra para hallar el CAMINO mas corto desde el vertice de origen
    a cada uno del resto de los vertices.
    '''
    pass



def main():
    pass

if __name__ == "__main__":
    main()
