from collections import defaultdict
from Grafo import Grafo

class CicloEuleriano():
    def __init__(self, grafo: Grafo):
        self.grafo = grafo
        self.stack = [list(self.grafo.vertices.keys())[0]]
        self.visitados = defaultdict(bool)

    def is_eulerian(self) -> bool:
        for key in self.grafo.vertices:
            if self.grafo.vertices[key].grau % 2 != 0:
                return False
        return True

    def has_eulerian_cycle(self) -> bool:
        if not self.is_eulerian():
            return False

        while self.stack:
            vertice = self.stack.pop()
            self.visitados[vertice] = True
            for vizinho in self.grafo.vertices[vertice].vizinhos:
                if not self.visitados[vizinho.indice]:
                    self.stack.append(vizinho.indice)

        for vertice in self.grafo.vertices.keys():
            if not self.visitados[vertice]:
                return False
        
        return True

    def find_eulerian_cycle(self):
        if not self.has_eulerian_cycle():
            return 0

        vertive_inicial = list(self.grafo.vertices.keys())[0]
        ciclo = [vertive_inicial]

        while True:
            proximo_vertice = None
            for vizinho in self.grafo.vertices[ciclo[-1]].vizinhos:
                if vizinho.indice not in ciclo:
                    proximo_vertice = vizinho.indice
                    break
                elif (len(ciclo) == len(self.grafo.vertices)) and (vizinho.indice == ciclo[0]):
                    ciclo.append(ciclo[0])
                    return ciclo


            if proximo_vertice is None:
                if len(ciclo) == len(self.grafo.vertices):
                    return ciclo
                else:
                    return None

            index = ciclo.index(ciclo[-1])
            ciclo = ciclo[:index+1] + [proximo_vertice] + ciclo[index+1:]

    def print_eulerian(self):
        if not self.has_eulerian_cycle():
            print(0)
        else:
            print(1)
            print(self.find_eulerian_cycle())


