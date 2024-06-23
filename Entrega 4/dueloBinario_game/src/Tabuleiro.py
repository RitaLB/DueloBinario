from Posicao import Posicao

class Tabuleiro():
    def __init__(self):
        self.casa_em_modificaçao = (None, None)
        self.tabuleiro = self.criar_tabuleiro()

    def criar_tabuleiro(self):
        tabuleiro = []
        for i in range(12):
            linha = []
            for j in range(12):
                if (i + j) % 2 == 0:
                    casa = Posicao(cor="preta", posicao=(i, j))
                else:
                    casa = Posicao(cor="branca", posicao=(i, j))
                linha.append(casa)
            tabuleiro.append(linha)
        return tabuleiro
    
    def achar_casas_pretas(linha_digito: int, coluna_digito: int) -> list[tuple[int, int]]:
        pass
    
    def atualizar_tabuleiro(self):
        pass

    def calcular_decimal(self, linha: int, coluna: int) -> int:
        pass

    def confirmar_jogada(self):
        pass

    def examinar_casas_brancas(linha: int, coluna: int) -> bool:
        pass

    def inserir_decdimal(linha: int, coluna: int, decimal: int, cor: str):
        pass

    def inserir_digito(self, digito: int, linha: int, coluna: int) -> bool:
        casa_habilitada = self.verificar_casa_habilitada(linha, coluna)

        if casa_habilitada:
            if self.casa_em_modificaçao[0] is not None and self.casa_em_modificaçao[1] is not None:
                self.limpar_casa_branca(self.casa_em_modificaçao[0], self.casa_em_modificaçao[1])

            self.tabuleiro[linha][coluna].atualizar_posicao_branca(digito, "blue")
            self.set_casa_em_modificacao(linha, coluna)
            return True
        
    def inserir_digito_recebido(self, digito: int, linha: int, coluna: int):
        pass

    def limpar_casa_branca(linha: int, coluna: int):
        pass

    def reiniciar_tabuleiro():
        pass

    def reset_casa_em_modificacao():
        pass

    def set_casa_em_modificacao(self,linha: int, coluna: int):
        self.casa_em_modificaçao = (linha, coluna)

    def verificar_casa_habilitada(linha: int, coluna: int) -> bool:
        pass

    def verificar_digito_inserido()-> bool:
        pass

    def verificar_tabuleiro_completo():
        pass

    def verificar_preenchimento_posicao() -> bool:
        pass


