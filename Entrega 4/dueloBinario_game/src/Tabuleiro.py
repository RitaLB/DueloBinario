from Posicao import Posicao

class Tabuleiro():
    def __init__(self):
        self.casa_em_modificaçao = (-1, -1)
        self.tabuleiro : list[list[Posicao]] = self.criar_tabuleiro()

    def criar_tabuleiro(self) -> list[list[Posicao]]:
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
    
    def achar_casas_pretas(self,linha_digito: int, coluna_digito: int) -> list[tuple[int, int]]:
        lin_casa_preta_0 = (linha_digito - 1) % 12
        col_casa_preta_0 = coluna_digito

        lin_casa_preta_1 = linha_digito
        col_casa_preta_1 = (coluna_digito - 1) % 12

        lin_casa_preta_2 = (linha_digito + 1) % 12
        col_casa_preta_2 = coluna_digito

        lin_casa_preta_3 = linha_digito
        col_casa_preta_3 = (coluna_digito + 1) % 12

        casas_pretas = [(lin_casa_preta_0, col_casa_preta_0),(lin_casa_preta_1, col_casa_preta_1),(lin_casa_preta_2, col_casa_preta_2),(lin_casa_preta_3, col_casa_preta_3)]

        return casas_pretas

    def atualizar_tabuleiro(self):
        pass

    def calcular_decimal(self, linha: int, coluna: int) -> int:
        pos_digito_3 = (((linha-1)% 12), coluna) 
        #print("posicao digito 3 = ", pos_digito_3)
        pos_digito_2 = (linha, ((coluna -1)% 12))
        #print("posicao digito 2 = ", pos_digito_2)
        pos_digito_1 = (((linha +1)% 12), coluna )
        #print("posicao digito 1 = ", pos_digito_1)
        pos_digito_0 = (linha, ((coluna+1)% 12)) 
        #print("posicao digito 0 = ", pos_digito_0)
        
        digito_0 = str(self.tabuleiro[pos_digito_0[0]][pos_digito_0[1]].digito)
        digito_1 = str(self.tabuleiro[pos_digito_1[0]][pos_digito_1[1]].digito)
        digito_2 = str(self.tabuleiro[pos_digito_2[0]][pos_digito_2[1]].digito)
        digito_3 = str(self.tabuleiro[pos_digito_3[0]][pos_digito_3[1]].digito)
        
        binario = digito_3 + digito_2 + digito_1 + digito_0
        #print("binario = ", binario)
        decimal_inicial = int(binario, 2)
        #print("d i = " , decimal_inicial)
        
        unidades = decimal_inicial - 10
        
        if (unidades >= 0):
            decimal = unidades + 1
        else:
            decimal = decimal_inicial

        #print("decimal = ", decimal)
        return decimal

    def confirmar_jogada(self):
        linha = self.casa_em_modificaçao[0]
        coluna = self.casa_em_modificaçao[1]
        self.tabuleiro[linha][coluna].mudar_cor_digito("preto")
        self.tabuleiro[linha][coluna].desabilitar_mudanca()
        self.reset_casa_em_modificacao()

    def contar_2s(self, cor) -> int:
        contagem = 0
        for linha in self.tabuleiro:
            for posicao in linha:
                if (posicao.decimal == 2) and (posicao.cor_jogador == cor):
                    contagem += 1
        return contagem

    def contar_1s(self, cor) -> int:
        contagem = 0
        for linha in self.tabuleiro:
            for posicao in linha:
                if (posicao.decimal == 1) and (posicao.cor_jogador == cor):
                    contagem += 1
        return contagem


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
            habilitada = self.tabuleiro[linha][coluna].habilitada
            if (habilitada):
                #print("casa branca habilitada = ", casa)
                grupo_completo = False
        return grupo_completo
                
    def inserir_decimal(self, linha: int, coluna: int, decimal: int, cor: str):
        self.tabuleiro[linha][coluna].atualizar_posicao_preta(decimal, cor)

    def inserir_digito(self, digito: int, linha: int, coluna: int) -> tuple[int, int]:
        casa_habilitada = self.verificar_casa_habilitada(linha, coluna)
        casa_antiga = self.casa_em_modificaçao
        
        if casa_habilitada:
            if self.casa_em_modificaçao[0] is not None and self.casa_em_modificaçao[1] is not None:
                casa_antiga = self.casa_em_modificaçao
                self.limpar_casa_branca(self.casa_em_modificaçao[0], self.casa_em_modificaçao[1])

            self.tabuleiro[linha][coluna].atualizar_posicao_branca(digito, "blue")
            #print("diito inserido = ", digito)
            #print("POSICAO = ", linha, coluna)
            self.set_casa_em_modificacao(linha, coluna)
        
        return casa_antiga
        
    def inserir_digito_recebido(self, digito: int, linha: int, coluna: int):
        self.tabuleiro[linha][coluna].atualizar_posicao_branca(digito, "black")
        #print("diito recebido inserido = ", digito)
        #print("POSICAO = ", linha, coluna)
        self.tabuleiro[linha][coluna].desabilitar_mudanca()

    def limpar_casa_branca(self, linha: int, coluna: int):
        self.tabuleiro[linha][coluna].limpar_posicao()

    def reiniciar_tabuleiro(self):
        self.tabuleiro = self.criar_tabuleiro()
        self.casa_em_modificaçao = (-1, -1)

    def reset_casa_em_modificacao(self):
        self.casa_em_modificaçao = (-1, -1)

    def set_casa_em_modificacao(self,linha: int, coluna: int):
        self.casa_em_modificaçao = (linha, coluna)

    def verificar_casa_habilitada(self, linha: int, coluna: int) -> bool:
        return self.tabuleiro[linha][coluna].habilitada

    def verificar_digito_inserido(self)-> bool:
        pass

    def verificar_tabuleiro_completo(self):
        completo = False
        for coluna in self.tabuleiro:
            for posicao in coluna:
                if (posicao.digito == None):
                    return False
        return True

    def verificar_preenchimento_posicao() -> bool:
        pass


