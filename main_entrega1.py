from Grafo.Grafo import Grafo
from atividade1.BuscaEmLargura import BuscaEmLargura
from atividade1.CicloEuleriano import CicloEuleriano
from atividade1.Dijkstra import Dijkstra
from atividade1.FloydWarshall import FloydWarshall
grafo = Grafo()

# questao 1
# ======================================

# grafo = Grafo()
# grafo.ler("tests/facebook_santiago.net")

# for key in grafo.vertices.keys():
#    print(f"{key}: {grafo.vertices[key].indice} - {grafo.vertices[key].rotulo}")

# for key in grafo.arestas.keys():
#     print(f"{key}: {grafo.arestas[key].u.indice}, {grafo.arestas[key].v.indice}  - {grafo.arestas[key].peso}")

# ======================================


# questao 2
# ======================================

# grafo2 = Grafo()
# grafo2.ler("tests/adjnoun.net")
# indice_vertice = int(input("Digite o indice do vertice s:"))

# busca = BuscaEmLargura(grafo2, indice_vertice)
# busca.run()
# ======================================


# questao 3
# ======================================

# grafo3 = Grafo()
# grafo3.ler("tests/test.net")

# ciclo = CicloEuleriano(grafo3)
# ciclo.printEulerian()

# ======================================


# questao 4
# ======================================

# grafo4 = Grafo()
# grafo4.ler("tests/test.net")
# grafo4.ler("tests/adjnoun.net")

# dijkstra = Dijkstra(grafo4, 2)
# dijkstra.run()

# ======================================


# ======================================
# questao 5
# grafo5 = Grafo()
# grafo5.ler("tests/adjnoun.net")
# floyd = FloydWarshall(grafo5)

# floyd.run()
# ======================================