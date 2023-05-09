class Vertice:
    def __init__(self, indice, rotulo):
        self.indice = indice
        self.rotulo = rotulo
        self.vizinhos = []  # outros vértices ligados a ele
        self.grau = 0
