from Grafo import Grafo
from BuscaEmLargura import BuscaEmLargura
grafo = Grafo()
#grafo.ler("tests/facebook_santiago.net")

#for key in grafo.vertices.keys():
#    print(f"{key}: {grafo.vertices[key].indice} - {grafo.vertices[key].rotulo}")

# for key in grafo.arestas.keys():
#     print(f"{key}: {grafo.arestas[key].u.indice}, {grafo.arestas[key].v.indice}  - {grafo.arestas[key].peso}")

# TESTE DA QUESTAO 2
grafo2 = Grafo()
grafo2.ler("tests/adjnoun.net")
indice_vertice = int(input("Digite o indice do vertice s:"))

busca = BuscaEmLargura(grafo2, indice_vertice)
busca.run()