class Vertice:
    def __init__(self, indice, rotulo):
        self.indice = indice
        self.rotulo = rotulo
        self.vizinhos = []             # vizinhos para grafos não direcionais
        self.vizinhos_saintes = []     # (self, v)
        self.vizinhos_entrantes = []   # (u, self)
        self.grau = 0
        self.cor = None
