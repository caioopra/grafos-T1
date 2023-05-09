from Grafo.Grafo import Grafo
from atividade2.OrdencaoTopologica import OrdencaoTopologica


def test_2_ordTopologica():
    testes = {
        1: "manha.net",
        2: "tcc_completo.net",
        3: "dirigido1.net",
        4: "dirigido2.net"
    }

    ordenacao = OrdencaoTopologica(f"tests/dirigidos/{testes[2]}")
    ordenacao.run()

def main():
    test_2_ordTopologica()


if __name__ == "__main__":
    main()
