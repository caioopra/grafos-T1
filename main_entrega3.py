from Grafo.Grafo import Grafo
from atividade3.ColoracaoDeVertices import ColoracaoDeVertices
from atividade3.EdmondsKarp import EdmondsKarp

def test_1_edmonds_karp():
    testes = {
        1: {
            "grafo": "wiki.net",
            "entrada": [1, 5]  # [init, ent]
        },
        2: {
            "grafo": "fluxo_m2.net",
            "entrada": [2, 6]
        }
    }    
    current_test = testes[2]
    file_name = current_test['grafo']
    init, end = current_test["entrada"]
    
    grafo = Grafo()
    grafo.ler(f"tests/dirigidos/{file_name}")
    
    edmonds_karp = EdmondsKarp(grafo, init, end)
    edmonds_karp.run()

def test_2_hopcroft_karp():
    ...


def test_3_coloracaoDeVertices():
    coloracao = ColoracaoDeVertices("tests/cor3.net")
    coloracao.run()


def main():
    test_1_edmonds_karp()
    # test_3_coloracaoDeVertices()


if __name__ == "__main__":
    main()
