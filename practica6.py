#! /usr/bin/python

# 6ta Practica Laboratorio 
# Complementos Matematicos I
# Consigna: Implementar los siguientes metodos

# Para descargar py-gnuplot: http://sourceforge.net/projects/gnuplot-py/files/latest/download?source=files

import time
import Gnuplot

class Vector:
    ''' Estructura de vectores '''

    def __init__(self, ejex, ejey):
        self.x = ejex
        self.y = ejey

def norma(x,y):
    return sqrt(x**2 + y**2)

def fa(x):
    return x**2/k

def fr(x):
    return k**2/x

def run_layout(grafo):
    '''
    Dado un grafo (en formato de listas), aplica el algoritmo de 
    Fruchtermann-Reingold para obtener (y mostrar) un layout
    '''

    V = grafo[0]
    E = grafo[1]

    W = 100  # width
    L = 100  # length
    area = W * L

    k = sqrt(area/len(V))

    for i in ITER:
       # Calcular fuerzas repulsivas

        for v in V:
            # Cada vertice tine dos vectores: .pos y .disp 
            v.disp = Vector(0,0)
            for u in V:
                if u != v:
                    # Delta es la diferencia entre los 2 vertices
                    delta = Vector(v.pos.x - u.pos.y, v.pos.y - u.pos.y) # Resto coordenadas 

                    # v.disp = v.disp + delta/norma(delta) * fr(norma(delta))
                    disp.x = v.disp.x + delta.x/norma(delta)* fr(norma(delta))
                    disp.y = v.disp.y + delta.y/norma(delta)* fr(norma(delta))


            # Calcular fuerzas atractivas
            for e in E:
                # Cada arista es un par ordenado de vertices .v y .u
                delta = Vector(0,0)
                delta.x = e.v.pos.x - e.u.pos.x
                delta.y = e.v.pos.y - e.u.pos.y

                # e.v.disp = e.v.disp - (delta/norma(delta)) * fa(norma(delta))
                e.v.disp.x = e.v.disp.x - (delta.x/norma(delta)) * fa(norma(delta))
                e.v.disp.y = e.v.disp.y - (delta.y/norma(delta)) * fa(norma(delta))

                # e.u.disp = e.v.disp + (delta/norma(delta)) * fa(norma(delta))
                e.u.disp.x = e.u.disp.x - delta.x * fa(norma(delta)) # delta.x ya esta dividido por por norma(delta)
                e.u.disp.y = e.u.disp.y - delta.y * fa(norma(delta)) # delta.y ya esta dividido por por norma(delta)

            # Limitar el desplazamiento de la temperatura y
            # evitar el desplazamiento fuera del frame
            for v in V:
                v.pos = v.pos + (v.disp/norma(v.disp))*minimo(v.disp, t)
                v.pos.x = minimo_(W/2, maximo(-W/2, v.pos.x))
                v.pos.y = minimo_(L/2, maximo(-L/2, v.posy)) 
            # t = cool(t) ?????
 

def ejemplo_gnuplot():
    g = Gnuplot.Gnuplot()
    # Ponerle titulo
    g('set title "TITULO"')
    # setear el intervalo a mostrar
    g('set xrange [0:100]; set yrange [0:100]')
    # Dibujar un rectangulo en 10, 20
    g('set object 1 rectangle center 10,20 size 5,5 fc rgb "black"')
    # Dibujar un circulo en 30, 40
    g('set object 2 circle center 30,40 size 3 ')
    # Dibujar una arista
    g('set arrow nohead from 10,20 to 30,40')
    # Borra leyenda
    g('unset key')
    # Dibujar
    g('plot NaN')
    # esperar 1 segundo
    time.sleep(1)
    # Borrar objeto 1
    g('unset object 1')
    # Re-dibujar
    g('replot')

def main():
    ejemplo_gnuplot()

if __name__ == "__main__":
    main()
