from Vertice import Vertice


class Grafo:
    def __init__(self):
        # {indice (int): Vertice}
        self.vertices = {}
        # {(indice a, indice b): Aresta}
        self.arestas = {}

    # retorna a quantidade de vertices no grafo
    def qtdVertices(self) -> int:
        return len(self.vertices.keys())

    # retorna a quantidade de arestas no grafo
    def qtdArestas(self) -> int:
        return len(self.arestas.keys())

    # retorna grau de vértice v
    def grau(self, v: int) -> int:
        return self.vertices[v].grau

    # retorna o rotulo do vertice v
    def rotulo(self, v: int) -> str:
        return self.vertices[v].rotulo

    # caso haja aresta entre os vértices, retorna True, senão, False
    def haAresta(self, u: Vertice, v: Vertice) -> bool:
        # TODO: implementar
        ...
                    

    # retorna o peso caso exista a aresta, senão infinito (max. representavel)
    def peso(self, u: Vertice, v: Vertice) -> int:
        # TODO: implementar
        ...

    # carrega grafo a partir de texto
    def ler(self, arquivo: str):
        # TODO: implementar
        ...
