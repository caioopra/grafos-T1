from Grafo import Grafo


class Dijkstra:
    def __init__(self, grafo: Grafo, indice_vertice: int):
        self.grafo = grafo
        self.vertice_s = self.grafo.vertices[indice_vertice]

        self.__distancias = {}  # D
        self.__visitados = {}  # C
        self.__antecessores = {}  # A

    def run(self):
        self.__dijkstra()
        self.__print_result()

    def __dijkstra(self):
        # inicialização
        for i in range(1, self.grafo.qtdVertices() + 1):
            self.__distancias[i] = float("inf")
            self.__visitados[i] = False
            self.__antecessores[i] = None
    
        self.__visitados[self.vertice_s.indice] = True
        self.__distancias[self.vertice_s.indice] = 0
        self.__antecessores[self.vertice_s.indice] = self.vertice_s.indice

        # enquanto tiver aresta não visitada
        while False in self.__visitados.values():
            # dicionário com vértices não visitados: {index : distancia}
            vertices_nao_visitados = {}
            for indice, visitado in self.__visitados.items():
                if not visitado:
                    vertices_nao_visitados[indice] = self.__distancias[indice]
            # valor da distância do vértice com menor distância
            menor_dist_nao_visitado = min(vertices_nao_visitados.values())
            key_menor_dist = [key for key, value in vertices_nao_visitados.items() if value == menor_dist_nao_visitado][0] # primeiro com aquele valor
            vertice_procurado = [vertice for _, vertice in self.grafo.vertices.items() if vertice.indice == key_menor_dist][0]  # u 

            self.__visitados[key_menor_dist] = True
            
            # vizinhos de vertice_procurado
            # foreach v ∈ N(u) : Cv = false do
            for vertice_v in vertice_procurado.vizinhos:
                if not self.__visitados[vertice_v.indice]:
                    # procurando aresta e sua direcao
                    aresta = None
                    for x in self.grafo.arestas.keys():  # keys = (indice1, indice2)
                        if x == (vertice_procurado.indice, vertice_v.indice):
                            aresta = self.grafo.arestas[(vertice_procurado.indice, vertice_v.indice)]
                            break
                        elif x == (vertice_v.indice, vertice_procurado.indice):
                            aresta = self.grafo.arestas[(vertice_v.indice, vertice_procurado.indice)]
                            break
                    
                    if self.__distancias[vertice_v.indice] > (self.__distancias[key_menor_dist] + aresta.peso):
                        self.__distancias[vertice_v.indice] = (self.__distancias[key_menor_dist] + aresta.peso)
                        self.__antecessores[vertice_v.indice] = key_menor_dist

    def __caminho(self):
        caminhos = {}
        
        for key in self.__antecessores.keys():
            caminhos[key] = [key]
            while True:
                antecessor = caminhos[key][0]  # garantir que sempre vai pegar apenas um
                if antecessor == self.vertice_s.indice:
                    break
                caminhos[key].insert(0, self.__antecessores[antecessor])

        return caminhos
                    
    def __print_result(self):
        caminho = self.__caminho()
        
        for k in caminho.keys():
            lista_str = str(caminho[k]).replace(" ", "").replace("[", "").replace("]", "")
            print(f"{k}: {lista_str}; d={self.__distancias[k]}")
