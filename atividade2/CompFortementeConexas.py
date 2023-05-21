from Grafo.Grafo import Grafo


class CompFortementeConexas:
    # recebe arquivo como string
    def __init__(self, arquivo: str):
        self.__grafo = Grafo()
        self.__grafo.ler(arquivo)
        self.__conhecidos = {}
        self.__tempo_conhecido = {}
        self.__tempo_final = {}
        self.__antecessores = {}

    def run(self):
        self.DFS()
        self.__grafo.transpose()
        self.DFS_adaptado()
        self.print_result()

    def DFS(self) -> list[int]:
        for i in range(1, self.__grafo.qtdVertices() + 1):
            self.__conhecidos[i] = False
            self.__tempo_conhecido[i] = float("inf")
            self.__tempo_final[i] = float("inf")

        self.__tempo = 0
 
        for u in self.__grafo.vertices:  # type u: int (index no dicionário)
            if not self.__conhecidos[u]:
                self.DFS_visit(u)




    def DFS_adaptado(self) -> list[int]:
        for i in range(1, self.__grafo.qtdVertices() + 1):
            self.__conhecidos[i] = False
            self.__tempo_conhecido[i] = float("inf")
            self.__tempo_final[i] = float("inf")
            self.__antecessores[i] = None

        self.__tempo = 0
 
        F = dict(sorted(self.__tempo_final.items(), key=lambda item: item[0], reverse=True))
        vertices = list(F.keys())

        for u in vertices:  
            if not self.__conhecidos[u]:
                self.DFS_visit(u)



    def DFS_visit(self, v: int):
        self.__conhecidos[v] = True
        self.__tempo += 1
        self.__tempo_conhecido[v] = self.__tempo

        for vizinho in self.__grafo.vizinhos_saintes(v):
            if not self.__conhecidos[vizinho.indice]:
                self.__antecessores[vizinho.indice] = v
                self.DFS_visit(vizinho.indice)

        self.__tempo += 1
        self.__tempo_final[v] = self.__tempo


    def print_result(self):
        lista = []
        for u, v in self.__antecessores.items():
            if v is None:
                componente = []
                componente.append(u)
                self.find_componente(u,componente)
                lista.append(componente)

        for componente in lista:
            print(', '.join(map(str, componente)))


    def find_componente(self,u,lista):
        for i,v in self.__antecessores.items():
            if u == v:
                lista.append(i)
                self.find_componente(i,lista)
