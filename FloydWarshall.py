from Grafo import Grafo

class FloydWarshall():
    def __init__(self, grafo: Grafo):
        self.grafo = grafo
        self.__matriz_adj = self.cria_matriz_adjacencias()

    def run(self):
        distancias = self.algoritmo()
        self.print_saida(distancias)

    def cria_matriz_adjacencias(self):
        adj = {}
        numV = self.grafo.qtd_vertices()
        for u in range(1, numV+1):
            linha = {}
            for v in range(1, numV+1):
                if u == v:
                    linha[v] = 0
                elif self.grafo.haAresta(u, v):
                    linha[v] = self.grafo.peso(u, v)
                else:
                    linha[v] = float('inf')
            adj[u] = linha
        return adj

    def algoritmo(self):
        copia_matriz = self.__matriz_adj.copy()
        quantidade_vertices = self.grafo.qtd_vertices()

        for k in range(1, quantidade_vertices + 1):
            for u in range(1, quantidade_vertices + 1):
                for v in range(1, quantidade_vertices + 1):
                    copia_matriz[u][v] = min(copia_matriz[u][v], copia_matriz[u][k] + copia_matriz[k][v])
        return copia_matriz

    def print_saida(self, d: dict):
        numV = self.grafo.qtd_vertices()
        for vertice in range(1, numV + 1):
            aux = []
            for v in range(1, numV + 1):
                numero = d[vertice][v]
                if (numero - int(numero)) == 0:
                    aux.append(int(numero))
                else:
                    aux.append(numero)
            list_str = str(aux).replace(
                ' ', '').replace('[', '').replace(']', '')
            print(f'{vertice}:{list_str}')