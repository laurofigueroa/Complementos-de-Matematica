#! /usr/bin/python

# 6ta Practica Laboratorio 
# Complementos Matematicos I
# Consigna: Implementar los siguientes metodos

# Para descargar py-gnuplot: http://sourceforge.net/projects/gnuplot-py/files/latest/download?source=files

import time
import Gnuplot


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
    
    def __init__(self, grafo, **opciones):
        # Guardo el grafo
        self.grafo = grafo

        # Obtener las opciones
        try:
            self.refresh = opciones["refresh"]
        except Exception:
            pass

        try:
            self.refresh = opciones["iter"]
        except Exception:
            pass

        try:
            self.refresh = opciones["c1"]
        except Exception:
            pass
        
        try:
            self.refresh = opciones["c2"]
        except Exception:
            pass


    def randomize(self):
        ''' Inicializa en forma aleatoria las posiciones de los nodos'''
        for v in V:
            posiciones[str(v)] = (random(), random())

        for e in E:
            fuerzas[str(e)] = random()
        

    def step(self):
        ''' Efectua un paso de la simulacion fisica y actualiza las posiciones de los nodos en gr'''
        # Calcular repulsiones de nodos (actualiza fuerzas)
        # Calcular atracciones de aristas (actualiza fuerzas)
        # En base a fuerzas, actualizar posiciones, setear fuerzas a cero
        for v in V:
            # Cada vertice tine dos vectores: .pos y .disp 
            for u in V:
                if u != v:
                    # Delta es la diferencia entre los 2 vertices
                    delta = (posiciones[v][0] - posiciones[u][0], posiciones[v][1] - posiciones[u][1]) # Resto coordenadas 

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


    def dibujar(self):
        ''' Dibuja (o actualiza) el estado del grafo gr en pantalla'''
        pass

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
                self.dibujar(gr)
        
        # Ultimo dibujado
        self.dibujar(gr)


def main():
    grafo1 = ([1, 2, 3, 4, 5, 6, 7], [(1,2), (2,3), (3,4), (4,5), (5,6), (6,7), (7,1)])

    # Creamos nuestro objeto LayoutGraph
    layout_gr = LayoutGraph(grafo1, iter = 100, refresh = 1, c2 = 2.5)

    # Ejecutamos el layout
    layout_gr.layout()



if __name__ == "__main__":
    main()
