from atividade3.ColoracaoDeVertices import ColoracaoDeVertices

def test_3_coloracaoDeVertices():
    coloracao = ColoracaoDeVertices('tests/cor3.net')
    coloracao.run()


def main():
    test_3_coloracaoDeVertices()


if __name__ == "__main__":
    main()
