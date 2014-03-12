#! /usr/bin/python

# 6ta Practica Laboratorio 
# Complementos Matematicos I
# Consigna: Implementar los siguientes metodos

# Para descargar py-gnuplot: http://sourceforge.net/projects/gnuplot-py/files/latest/download?source=files

import time
import math
import random
import Gnuplot


class Vector:
    ''' Estructura de vectores '''

    def __init__(self, ejex, ejey):
        self.x = ejex
        self.y = ejey

def norma(vector):
    return math.sqrt(vector.x**2 + vector.y**2)

def fa(x, k):
    return x**2/k

def fr(x, k):
    return k**2/x

def minimo(a, b):
  if a < b:
    return a
  else:
    return b

def maximo(a, b):
  if a < b:
    return b
  else:
    return a

def cool(t):
  return math.fabs(t*0.96)

class LayoutGraph():
    # opciones de layout globales
    '''    
    Opciones de layout:
    refresh: Numero de iteraciones entre actualizaciones de pantalla. 
             0 -> se grafica solo al final.
    c1: constante usada para calcular la repulsion entre nodos
    c2: constante usada para calcular la atraccion de aristas
    '''
    refresh = 0
    iter    = 50
    c1      = 1.0
    c2      = 2.5

    # Informacion del grafo 

    grafo = None
    posiciones = {}
    fuerzas = {}        
   
    ### 
    t = 10

    global posiciones
    global fuerzas
    global t

    ###
    def __init__(self, grafo, **opciones):
        
        # Guardo el grafo
        self.grafo = grafo

        # Obtener las opciones
        try:
            self.refresh = opciones["refresh"]
        except Exception:
            pass

        try:
            self.iter = opciones["iter"]
        except Exception:
            pass

        try:
            self.c1 = opciones["c1"]
        except Exception:
            pass
        
        try:
            self.c2 = opciones["c2"]
        except Exception:
            pass
    
        try:
            self.W = opciones["W"]
        except Exception:
            pass
        try:
            self.L = opciones["L"]
        except Exception:
            pass
        try:
            self.name = opciones["name"]
        except Exception:
            pass

        self.g = None

    def randomize(self):
        ''' Inicializa en forma aleatoria las posiciones de los nodos'''
        V = self.grafo[0]
        for v in V:
            posiciones[v] = Vector(random.randint(-self.W, self.W), random.randint(-self.L, self.L))
            fuerzas[v] = Vector(0, 0)
        

    # En base a fuerzas, actualizar posiciones, setear fuerzas a cero
    def step(self):
        ''' Efectua un paso de la simulacion fisica y actualiza las posiciones de los nodos en gr'''

        V = self.grafo[0]
        E = self.grafo[1]
        k = math.sqrt(self.W*self.L / len(self.grafo[0]))        
        

        # Calcular repulsiones de nodos (actualiza fuerzas)
        for v in V:
            # Cada vertice tine dos vectores: .pos y .disp 
            fuerzas[v].x = 0
            fuerzas[v].y = 0

            for u in V:
                if u != v:
                    # Delta es la diferencia entre los 2 vertices
                    delta = Vector(posiciones[v].x - posiciones[u].x, posiciones[v].y - posiciones[u].y) # Resto coordenadas 

                    # v.disp = v.disp + delta/norma(delta) * fr(norma(delta))
                    fuerzas[v].x = fuerzas[v].x + delta.x/(norma(delta)+1)* fr(norma(delta)+1, k)*self.c1
                    fuerzas[v].y = fuerzas[v].y + delta.y/(norma(delta)+1)* fr(norma(delta)+1, k)*self.c1


            # Calcular atracciones de aristas (actualiza fuerzas)
        for e in E:
            # Cada arista es un par ordenado de vertices .v y .u (e[0] y e[1])
            delta = Vector(0,0)
            delta.x = posiciones[e[0]].x - posiciones[e[1]].x
            delta.y = posiciones[e[0]].y - posiciones[e[1]].y

            # e.v.disp = e.v.disp - (delta/norma(delta)) * fa(norma(delta))
            #e.v.disp.x = e.v.disp.x - (delta.x/norma(delta)) * fa(norma(delta))
            #e.v.disp.y = e.v.disp.y - (delta.y/norma(delta)) * fa(norma(delta))
            N = norma(delta)
            fuerzas[e[0]].x = fuerzas[e[0]].x - (delta.x/(N+1)) * fa(N, k)*self.c2
            fuerzas[e[0]].y = fuerzas[e[0]].y - (delta.y/(N+1)) * fa(N, k)*self.c2


            # e.u.disp = e.v.disp + (delta/norma(delta)) * fa(norma(delta))
               
            #e.u.disp.x = e.u.disp.x - delta.x * fa(norma(delta)) # delta.x ya esta dividido por por norma(delta)
            #e.u.disp.y = e.u.disp.y - delta.y * fa(norma(delta)) # delta.y ya esta dividido por por norma(delta)
            fuerzas[e[1]].x = fuerzas[e[1]].x + delta.x * fa(norma(delta), k)*self.c2
            fuerzas[e[1]].y = fuerzas[e[1]].y + delta.y * fa(norma(delta), k)*self.c2

        # Limitar el desplazamiento de la temperatura y
        # evitar el desplazamiento fuera del frame
        for v in V:
            #v.pos = v.pos + (v.disp/norma(v.disp))*minimo(v.disp, t)
            posiciones[v].x = posiciones[v].x + (fuerzas[v].x /norma(fuerzas[v])) * minimo(norma(fuerzas[v]), t)
            posiciones[v].y = posiciones[v].y + (fuerzas[v].y /norma(fuerzas[v])) * minimo(norma(fuerzas[v]), t)

            posiciones[v].x = minimo(self.W/2, maximo(-self.W/2, posiciones[v].x))
            posiciones[v].y = minimo(self.L/2, maximo(-self.L/2, posiciones[v].y))
            #v.pos.x = minimo_(W/2, maximo(-W/2, v.pos.x))
            #v.pos.y = minimo_(L/2, maximo(-L/2, v.posy)) 
        cool(t)



    def dibujar(self):
        ''' Dibuja (o actualiza) el estado del grafo gr en pantalla'''
    
        V = self.grafo[0]
        E = self.grafo[1]

        if self.g is None:
            self.g = Gnuplot.Gnuplot()
            # Ponerle titulo
            self.g('set title "'+ self.name+ '"')
            # setear el intervalo a mostrar
            self.g('set xrange [-'+ str(self.W) +':'+ str(self.W) +']; set yrange [-'+ str(self.L)+ ':'+ str(self.L) +']')
        else:
            for i in range(len(V)+len(E)):
                self.g('unset object ' + str(i))
        

        for i, v in enumerate(V):
            self.g('set object ' +str(i+1)+ ' circle center ' + str(posiciones[v].x)+', '+str(posiciones[v].y)+ ' size 1')

        i = i+1 
        for e in E:
            self.g('set arrow '+ str(i) +' nohead from '+ str(posiciones[e[0]].x) + ',' + str(posiciones[e[0]].y) + ' to ' + str(posiciones[e[1]].x) +',' + str(posiciones[e[1]].y))
            i = i+1
        # Borra leyenda
        self.g('unset key')
        # Dibujar
        self.g('plot NaN')
        # esperar 1 segundo
        time.sleep(0.4)
        # Re-dibujar
        self.g('replot')

    def layout(self):
        '''
        Aplica el algoritmo de Fruchtermann-Reingold para obtener (y mostrar) 
        un layout        
        '''

        # Inicializamos las posiciones
        self.randomize()

        # Si es necesario, lo mostramos por pantalla
        if (self.refresh > 0):
            self.dibujar()

        # Bucle principal
        for i in range (0, self.iter):
            # Realizar un paso de la simulacion
            self.step()
                
            # Si es necesario, lo mostramos por pantalla
            if (self.refresh > 0 and 0 == i % self.refresh):
                self.dibujar()
        
        # Ultimo dibujado
        self.dibujar()


def main():
    grafo1 = ([1,2,3,4,5], [(1,2), (2,3), (3,4), (4,5), (5,1), (1,4), (1,3), (2,5), (2,4), (3, 5)])
    grafo3 = ([1, 2, 3, 4, 5, 6, 7, 8, 9], [(1,2), (1,9), (2,3), (3,4), (4,5), (5,1), (5,6), (6,7), (7,1), (8,3), (9,5)])
    grafo2 = ([1, 2, 3, 4, 5, 6, 7], [(1,2), (2,3), (3,4), (4,5), (5,6), (6,7), (7,1)])
    
    # Ejemplo 1
    # Creamos nuestro objeto LayoutGraph
    layout_gr = LayoutGraph(grafo1, name = '##  Ejemplo 1  ##', iter = 80, refresh = 1, c1 = 200 , c2 = 5,  W = 110, L = 110)

    # Ejecutamos el layout
    layout_gr.layout()

    # Ejemplo 2 (ejemplo original)
    # Creamos nuestro objeto LayoutGraph2
    layout_gr = LayoutGraph(grafo2, name = '##  Ejemplo 2  ##', iter = 50, refresh = 1, c1 = 2, c2 = 3, W = 100, L = 100)

    # Ejecutamos el layout
    layout_gr.layout()



if __name__ == "__main__":
    main()
