from Grafo.Grafo import Grafo
from atividade2.OrdencaoTopologica import OrdencaoTopologica
from atividade2.Kruskal import Kruskal
from atividade2.CompFortementeConexas import CompFortementeConexas



def test_1_compFortementeConexa():
    testes = {
        1: "test.net",
        2: ""
    }

    comp = CompFortementeConexas(f"tests/{testes[1]}")
    comp.run()

def test_2_ordTopologica():
    testes = {
        1: "manha.net",
        2: "tcc_completo.net",
        3: "dirigido1.net",
        4: "dirigido2.net"
    }

    ordenacao = OrdencaoTopologica(f"tests/dirigidos/{testes[2]}")
    ordenacao.run()


def test_3_Kruskal():
    testes = {
        1: "agm_tiny.net",
        2: "",
    }

    kruskal = Kruskal(f"tests/{testes[1]}")
    kruskal.run()


def main():
    test_1_compFortementeConexa()
    # test_2_ordTopologica()
    # test_3_Kruskal()



if __name__ == "__main__":
    main()
