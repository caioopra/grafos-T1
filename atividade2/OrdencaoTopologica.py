from Grafo.Grafo import Grafo


class OrdencaoTopologica:
    # recebe arquivo como string
    def __init__(self, arquivo: str):
        self.__grafo = Grafo()
        self.__grafo.ler(arquivo)

        self.__conhecidos = {}
        self.__tempo_conhecido = {}
        self.__tempo_final = {}

    def run(self):
        self.__DFS_ordenacao_topologica()
        self.__print_result()

    # retorna lista contendo os índices de forma ordenada topologicamente
    def __DFS_ordenacao_topologica(self) -> list[int]:
        for i in range(1, self.__grafo.qtdVertices() + 1):
            self.__conhecidos[i] = False
            self.__tempo_conhecido[i] = float("inf")
            self.__tempo_final[i] = float("inf")

        self.__tempo = 0
        self.__lista = []

        for u in self.__grafo.vertices:  # type u: int (index no dicionário)
            if not self.__conhecidos[u]:
                self.__DFS_visit_OT(u)

        return self.__lista

    def __DFS_visit_OT(self, v: int):
        self.__conhecidos[v] = True
        self.__tempo += 1
        self.__tempo_conhecido[v] = self.__tempo

        for vizinho in self.__grafo.vizinhos_saintes(v):
            if not self.__conhecidos[vizinho.indice]:
                self.__DFS_visit_OT(vizinho.indice)

        self.__tempo += 1
        self.__tempo_final[v] = self.__tempo

        self.__lista.insert(0, v)

    def __print_result(self):
        result_string = ""
        for v in self.__lista:
            result_string += ('{} -> '.format((self.__grafo.vertices[v].rotulo).replace('"', "")))

        print(result_string[0:-4] + ".")
