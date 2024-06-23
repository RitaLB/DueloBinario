class Posicao():
    def __init__(self,cor, posicao: tuple[int, int]):
        self.cor = cor
        self.posicao = posicao
        self.cor_digito: str = None
        self.cor_jogador: str = None
        self.decimal : int = None
        self.digito : int = None
        self.habitada = False


    def atualizar_posicao_branca(self, digito: int, cor_digito: str):
        self.digito = digito
        self.cor_digito = cor_digito

    def definirCor():
        pass

    def desabilitar_mudanca(self):
        pass

    def get_digito(self) -> int:
        return self.digito
    
    def habilitar_mudanca(self):
        pass

    def limpar_posicao():
        pass

    def mudar_cor_digito(cor: str) :
        pass
    
    def reiniciar_posicao():
        pass
    