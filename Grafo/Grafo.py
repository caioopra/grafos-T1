from Grafo.Aresta import Aresta
from Grafo.Vertice import Vertice

from math import inf


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

    def vizinhos(self, v: int) -> list[int]:
        return self.vertices[v].vizinhos
    
    def vizinhos_saintes(self, v: int) -> list[int]:
        return self.vertices[v].vizinhos_saintes
    
    def vizinhos_entrantes(self, u: int) -> list[int]:
        return self.vertices[u].vizinhos_entrantes

    # caso haja aresta entre os vértices, retorna True, senão, False
    def haAresta(self, u: int, v: int) -> bool:
        if ((u, v) in self.arestas) or ((v, u) in self.arestas):
            return True
        return False

    # retorna o peso caso exista a aresta, senão infinito (max. representavel)
    # "inf" é float da biblioteca math
    def peso(self, u: int, v: int) -> int:
        if (u, v) in self.arestas:
            return self.arestas[(u, v)].peso
        if (v, u) in self.arestas:
            return self.arestas[(v, u)].peso

        return inf

    # carrega grafo a partir de texto
    def ler(self, arquivo: str):
        arquivo = open(arquivo, "r").read().split("\n")

        arestas = False

        for linha in arquivo:
            # casos em que não faz nada
            if linha == "" or "*vertices" in linha:
                continue
            # comeca a ler as arestas
            elif "*edges" in linha or "*arcs" in linha:
                arestas = True

            # caso esteja lendo vertices
            elif not arestas:
                indice, rotulo = linha.split(" ", 1)
                indice = int(indice)

                vertice = Vertice(indice, rotulo)
                self.vertices[indice] = vertice

            # lendo arestas
            else:
                valores = linha.split()
                u = self.vertices[int(valores[0])]
                v = self.vertices[int(valores[1])]
                peso = float(valores[2])

                aresta = Aresta(u, v, peso)
                self.arestas[(u.indice, v.indice)] = aresta

                u.vizinhos.append(v)
                u.vizinhos_saintes.append(v)
                u.grau += 1
                v.vizinhos.append(u)
                v.vizinhos_entrantes.append(u)
                v.grau += 1
