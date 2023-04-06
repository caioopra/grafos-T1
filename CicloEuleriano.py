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
            for vizinho in self.grafo.vertices[vertice].vizinhos.keys():
                if not self.visitados[vizinho]:
                    self.stack.append(vizinho)

        for vertice in self.grafo.vertices.keys():
            if not self.visitados[vertice]:
                return False
        
        return True

