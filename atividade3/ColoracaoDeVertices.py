from Grafo.Grafo import Grafo

class ColoracaoDeVertices:
    def __init__(self, arquivo):        
        self.__grafo = Grafo()
        self.__grafo.ler(arquivo)
    
    def run(self):
        vertices = sorted(self.__grafo.vertices.values(), key=lambda vertice: len(vertice.vizinhos), reverse=True)

        cores = []

        for vertice in vertices:
            cores_aux = [True] * len(vertices)

            for vizinho in vertice.vizinhos:
                if vizinho.cor != None:
                    cores_aux[vizinho.cor] = False

            for cor, isDisponivel in enumerate(cores_aux):
                if isDisponivel:
                    vertice.cor = cor
                    vertice.hasCor = True

                    if cor not in cores:
                        cores.append(cor)
                    break

        self.print_saida()

    def print_saida(self):
        for vertice in self.__grafo.vertices.values():
            print(f'O vértice {vertice.indice} possui a coloração {vertice.cor}')
