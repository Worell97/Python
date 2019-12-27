class Comodo:
    __largura: float
    __profundidade: float
    __altura: float

    def __init__(self, largura, profundidade):
        self.__largura = largura
        self.__profundidade = profundidade
        self.__altura = 2.9


    @property
    def largura(self):
        return float(self.__largura)

    @property
    def profundidade(self):
        return float(self.__profundidade)

    @property
    def altura(self):
        return float(self.__altura)

    @largura.setter
    def largura(self, largura):
        try:
            self.__largura = float(largura)
        except Exception:
            print('O valor informado para largura é inválido')
            exit()

    @profundidade.setter
    def profundidade(self, profundidade):
        try:
            self.__profundidade = float(profundidade)
        except Exception:
            print('O valor informado para profundidade é inválido')
            exit()
