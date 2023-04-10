from Grafo import Grafo

class FloydWarshall():
    def __init__(self, grafo: Grafo):
        self.grafo = grafo
        self.__matriz_adj = self.cria_matriz_adjacencias()
        self.__copia_matriz = dict()

    def run(self):
        self.run_algoritmo()
        self.print_distancias()

    def run_algoritmo(self):
        self.__copia_matriz = self.__matriz_adj.copy()
        quantidade_vertices = self.grafo.qtdVertices()

        for k in range(1, quantidade_vertices + 1):
            for u in range(1, quantidade_vertices + 1):
                for v in range(1, quantidade_vertices + 1):
                    self.__copia_matriz[u][v] = min(self.__copia_matriz[u][v], self.__copia_matriz[u][k] + self.__copia_matriz[k][v])

    def print_distancias(self):
        quantidade_vertices = self.grafo.qtdVertices()

        for vertice in range(1, quantidade_vertices + 1):
            lista_auxiliar = []
            for indice_vertice in range(1, quantidade_vertices + 1):
                valor = self.__copia_matriz[vertice][indice_vertice]
                if (valor - int(valor)) == 0:
                    lista_auxiliar.append(int(valor))
                else:
                    lista_auxiliar.append(valor)

            distancias_formatadas = str(lista_auxiliar).replace(
                ' ', '').replace('[', '').replace(']', '')
            print(f'{vertice}:{distancias_formatadas}')

    def cria_matriz_adjacencias(self):
        matriz_adjacencias = {}
        quantidade_vertices = self.grafo.qtdVertices()

        for u in range(1, quantidade_vertices+1):
            linha = {}
            for v in range(1, quantidade_vertices+1):
                if u == v:
                    linha[v] = 0
                elif self.grafo.haAresta(u, v):
                    linha[v] = self.grafo.peso(u, v)
                else:
                    linha[v] = float('inf')
            matriz_adjacencias[u] = linha
        return matriz_adjacencias