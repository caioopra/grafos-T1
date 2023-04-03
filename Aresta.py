from Vertice import Vertice


class Aresta:
    def __init__(self, u: Vertice, v: Vertice, peso: int):
        self.u = u
        self.v = v
        self.peso = peso
