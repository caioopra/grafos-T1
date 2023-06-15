from collections import (
    deque,
)  # https://docs.python.org/3/library/collections.html#collections.deque
from Grafo.Grafo import Grafo


class EdmondsKarp:
    def __init__(self, grafo: Grafo, inicial: int, final: int):
        self.__grafo = grafo
        self.__inicial = inicial
        self.__final = final

        self.__fluxo = -0
        self.__F = [
            [0 for _ in range(self.__grafo.qtdVertices() + 1)]
            for _ in range(self.__grafo.qtdVertices() + 1)
        ]

    def run(self):
        while True:
            caminhoAumentante = [-1 for _ in range(self.__grafo.qtdVertices() + 1)]
            caminhoAumentante[self.__inicial] = -1

            capacidadeResidual = [0 for _ in range(self.__grafo.qtdVertices() + 1)]
            capacidadeResidual[self.__inicial] = float("inf")
            
            self.__fila = deque([self.__inicial])

            fluxoCaminho, caminhoAumentante = self.BFS(
                caminhoAumentante, capacidadeResidual
            )
            
            if fluxoCaminho == 0:
                break
        
            self.__fluxo += fluxoCaminho
            verticeAtual = self.__final
            
            while verticeAtual != self.__inicial:
                vizinho = caminhoAumentante[verticeAtual]
                self.__F[vizinho][verticeAtual] += fluxoCaminho
                self.__F[verticeAtual][vizinho] -= fluxoCaminho
                verticeAtual = vizinho
    
        print(f"Fluxo máximo {self.__inicial} -> {self.__final}: {self.__fluxo}")

    def BFS(self, caminhoAumentante, capacidadeResidual):
        while len(self.__fila) > 0:
            verticeAtual = self.__fila.popleft()

            for vizinho in self.__grafo.vizinhos_saintes(verticeAtual):
                residual = (
                    self.__grafo.peso(verticeAtual, vizinho.indice)
                    - self.__F[verticeAtual][vizinho.indice]
                )
                
                if residual > 0 and caminhoAumentante[vizinho.indice] == -1:
                    caminhoAumentante[vizinho.indice] = verticeAtual
                    capacidadeResidual[vizinho.indice] = min(
                        capacidadeResidual[verticeAtual],
                        residual
                    )
                    
                    if vizinho.indice is not self.__final:
                        self.__fila.append(vizinho.indice)
                    else:
                        return capacidadeResidual[self.__final], caminhoAumentante
        
        return 0, caminhoAumentante
