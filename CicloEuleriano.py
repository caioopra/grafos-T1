from collections import defaultdict
from Grafo import Grafo
from copy  import copy
class CicloEuleriano():
    def __init__(self, grafo: Grafo):
        self.grafo = grafo

    def isEulerian(self) -> bool:
        for key in self.grafo.vertices:
            if self.grafo.vertices[key].grau % 2 != 0:
                return False
        return True

    def hierholzer(self):
        arestas_visitadas = {}  
        arestas = list(self.grafo.arestas.values())

        for x in arestas:
            arestas_visitadas[(x.u.indice, x.v.indice)] = False

        v = list(self.grafo.vertices.values())[0].indice

        r, ciclo = self.buscarSubcicloEuleriano(v, arestas_visitadas)    
        if r == False:
            return False, None
        
        else:
            if False in arestas_visitadas.values():
                return False, None
            else:
                return True, ciclo

    def buscarSubcicloEuleriano(self, v, arestas_visitadas):
        ciclo = [v]
        t = v
        
        while True:

            if not False in arestas_visitadas.values():
                return False, None
            else:
                nao_visitados = [k for k, i in arestas_visitadas.items() if i is False and v in k]
                vertice = v
                v = nao_visitados[0][0]
                u = nao_visitados[0][1]
                arestas_visitadas[(v, u)] = True
                if u != vertice:
                    v = u

            
                ciclo.append(v)

            if v == t:
                break

        vertices_no_ciclo = [self.grafo.vertices[x] for x in ciclo]
        vizinhos_abertos = []

        for x in vertices_no_ciclo:
            for y in x.vizinhos:
                if (x.indice, y.indice) in arestas_visitadas:
                    if arestas_visitadas[(x.indice, y.indice)] == False:
                        vizinhos_abertos.append(x)

                elif (y.indice, x.indice) in arestas_visitadas:
                    if arestas_visitadas[(y.indice, x.indice)] == False:
                        vizinhos_abertos.append(x)

        if not vizinhos_abertos:
            return True, ciclo

        for x in vizinhos_abertos:
            r, ciclo_2 = self.buscarSubcicloEuleriano(x.indice, arestas_visitadas)

            for x in ciclo:
                if x == ciclo_2[0]:
                    index = ciclo.index(x)
                    ciclo[index+1:index+1] = ciclo_2
                    ciclo.pop(index)
                    break

            return True, ciclo


    def printEulerian(self):
        if not self.isEulerian():
            print(0)
        else:
            print(1)
            r, ciclo = self.hierholzer()
            for x in range(len(ciclo)-1):
                print(ciclo[x], end=',')
            print(ciclo[-1])
