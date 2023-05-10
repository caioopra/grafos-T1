from Grafo.Grafo import Grafo


class Kruskal():
    def __init__(self, arquivo: str) -> None:
        self.__grafo = Grafo()
        self.__grafo.ler(arquivo)
        self.__arvore = []

    def run(self):
        self.__Find_minimal_tree()
        self.__Print_result()

    def __Find_minimal_tree(self):
        S = {}
        for vertice in self.__grafo.vertices.keys():
            S[vertice] = [vertice]

        arestas_ordenadas = []

        for x in self.__grafo.arestas.values():
            arestas_ordenadas.append((x.u.indice, x.v.indice, x.peso))

        arestas_ordenadas.sort(key=lambda item: item[2])

        for vertice in arestas_ordenadas:
            if (S[vertice[0]] != S[vertice[1]]):
                self.__arvore.append((vertice[0], vertice[1]))
                X = S[vertice[0]] + S[vertice[1]]
                for y in X:
                    S[y] = X


    def __Print_result(self):
        peso = 0
        for x in self.__arvore:
            peso += self.__grafo.arestas[(x[0], x[1])].peso
        print(peso)
        for x in range(len(self.__arvore)-1):
            print(f'{self.__arvore[x][0]}-{self.__arvore[x][1]}, ', end= '')
        print(f'{self.__arvore[len(self.__arvore)-1][0]}-{self.__arvore[len(self.__arvore)-1][1]}')