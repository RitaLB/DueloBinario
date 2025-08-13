class Posicao():
    def __init__(self,cor, posicao: tuple[int, int]):
        self.cor = cor
        self.posicao = posicao
        self.cor_digito: str = None
        self.cor_jogador: str = None
        self.decimal : int = None
        self.digito : int = None
        self.habilitada = True


    def atualizar_posicao_branca(self, digito: int, cor_digito: str):
        self.digito = digito
        self.cor_digito = cor_digito

    def atualizar_posicao_preta(self, decimal: int, cor: str):
        self.decimal = decimal
        self.cor_jogador = cor

    def desabilitar_mudanca(self):
        self.habilitada = False

    def get_digito(self) -> int:
        return self.digito
    
    def limpar_posicao(self):
        self.digito = None
        self.cor_digito = None

    def mudar_cor_digito(self, cor: str) :
        self.cor_digito = cor

    