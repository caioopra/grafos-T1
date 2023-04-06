from queue import Queue
from collections import defaultdict
from Grafo import Grafo

class BuscaEmLargura():
    def __init__(self, grafo: Grafo, indice_vertice: int):
        self.grafo = grafo
        self.vertice_s = self.grafo.vertices[indice_vertice]
        self.__visitados = {}
        self.__distancias = {}
        self.__antecessores = {}
        self.__fila = Queue()

    def run(self):
        self.busca_em_largura()
        self.print_busca()

    #Configurando vértices e vértice de origem
    def configurar_busca(self):
        teste = self.grafo.qtdVertices()
        for i in range(1, self.grafo.qtdVertices() + 1):
            self.__visitados[i] = False
            self.__distancias[i] = float('inf')
            self.__antecessores[i] = None

        self.__visitados[self.vertice_s.indice] = True
        self.__distancias[self.vertice_s.indice] = 0

        self.__fila.put(self.vertice_s)


    def busca_em_largura(self):
        self.configurar_busca()

        while self.__fila.empty() == False:
            vertice = self.__fila.get()
            for vizinho in vertice.vizinhos:
                if self.__visitados[vizinho.indice] == False:
                    self.__visitados[vizinho.indice] = True
                    self.__distancias[vizinho.indice] = self.__distancias[vertice.indice] + 1
                    self.__antecessores[vizinho.indice] = vertice
                    self.__fila.put(vizinho)


    def print_busca(self):
        res = defaultdict(list)
        for key, value in sorted(self.__distancias.items()):
            res[value].append(key)
        res = dict(res)

        for i in range(len(res.keys())):
            list_str = str(res[i]).replace(' ', '').replace('[', '').replace(']', '')
            print(f'{i}: {list_str}')