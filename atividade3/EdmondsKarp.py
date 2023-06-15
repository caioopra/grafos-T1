from Grafo.Grafo import Grafo
from Grafo.Vertice import Vertice


class EdmondsKarp:
    def __init__(self, grafo: Grafo, origem: int, sorvedouro: int, rede: Grafo):
        self.__grafo = grafo
        self.__origem = origem
        self.__sorvedouro = sorvedouro
        self.__rede = rede
        
        self.__C = {}
        self.__A = {}
        self.__queue = []
    
    def initialize(self):
        for i in range(self.__grafo.qtdVertices() + 1):
            self.__C[i] = False
            self.__A[i] = None
        self.__C[self.__sorvedouro] = True
        self.__queue.append(self.__grafo.vertices[self.__sorvedouro])  # armazenando objetos Vertice
        
    def search(self):
        while not len(self.__queue):
            u = self.__queue.pop()
            
            for vizinho in u.vizinhos_saintes():
                if not self.__C[vizinho.indice] and 
    
    def run(self):
        self.initialize()
        self.search()