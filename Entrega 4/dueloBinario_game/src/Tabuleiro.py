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
        pos_digito_0 = (linha, coluna + 1)
        pos_digito_1 = (linha + 1, coluna)
        pos_digito_2 = (linha, coluna - 1)
        pos_digito_3 = (linha - 1, coluna)
        
        digito_0 = self.tabuleiro[pos_digito_0[0]][pos_digito_0[1]]
        digito_1 = self.tabuleiro[pos_digito_1[0]][pos_digito_1[1]]
        digito_2 = self.tabuleiro[pos_digito_2[0]][pos_digito_2[1]]
        digito_3 = self.tabuleiro[pos_digito_3[0]][pos_digito_3[1]]
        
        binario = digito_3 + digito_2 + digito_1 + digito_0
        
        decimal_inicial = int(binario)
        
        unidades = decimal_inicial - 10
        
        if (unidades >= 0):
            decimal = unidades + 1
        else:
            decimal = unidades
        return decimal

    def confirmar_jogada(self):
        pass

    def examinar_casas_brancas(self, linha: int, coluna: int) -> bool:
        lin_casa_branca_0 = (linha -1) % 12
        col_casa_branca_0 = coluna
        
        lin_casa_branca_1 = linha
        col_casa_branca_1 = (coluna - 1) % 12
        
        lin_casa_branca_2 = (linha + 1) % 12
        col_casa_branca_2 = coluna
        
        lin_casa_branca_3 = linha
        col_casa_branca_3 = (coluna + 1) % 12
        
        casas_brancas = [(lin_casa_branca_0, col_casa_branca_0),
                         (lin_casa_branca_1, col_casa_branca_1),
                         (lin_casa_branca_2, col_casa_branca_2),
                         (lin_casa_branca_3, col_casa_branca_3)]
        
        grupo_completo = True
        
        for casa in casas_brancas:
            linha = casa[0]
            coluna = casa[1]
            habilitada = self.tabuleiro[linha][coluna].habilitada()
            if (habilitada):
                grupo_completo = False
        return grupo_completo
                
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


