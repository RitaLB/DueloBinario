
from Jogador import Jogador
from Tabuleiro import Tabuleiro

from enums import EstadoJogo
from enums import JogadorDaVez

class DueloBinario():
    def __init__(self, nome_jogador_local: str, nome_jogador_remoto: str):
        self.casa_antiga: tuple[int, int] = None
        self.digito_inserido: int = None
        self.estado_jogo: EstadoJogo = EstadoJogo.INICIAL # VERIFICAR
        self.jogada_em_andamento: bool = None
        self.jogador_da_vez : JogadorDaVez = None
        self.jogador_local: Jogador = Jogador(nome_jogador_local, 0)
        self.jogador_remoto: Jogador = Jogador(nome_jogador_remoto, 0)
        self.partida_em_andamento: bool = False
        self.posicao_digito_inserido: tuple[int, int] = None
        self.rodada_atual: int = None
        self.Tabuleiro: Tabuleiro = Tabuleiro()
        self.vencedor: str = None # str ou Jogador?

    def atualizar_pontuacao_jogador_da_vez(self, pontos: int):
        if self.jogador_da_vez == JogadorDaVez.LOCAL:
            pontuacao_atual= self.jogador_local.get_pontuacao()
        else:
            pontuacao_atual = self.jogador_remoto.get_pontuacao()
        
        pontuacao_parcial = pontuacao_atual + pontos
        while pontuacao_parcial >= 10:
            unidades = pontuacao_parcial % 10
            dezenas = (pontuacao_parcial - unidades) / 10
            pontuacao_parcial = unidades + dezenas

        nova_pontuacao = pontuacao_parcial

        if self.jogador_da_vez == JogadorDaVez.LOCAL:
            self.jogador_local.set_pontuacao(nova_pontuacao)
        else:
            self.jogador_remoto.set_pontuacao(nova_pontuacao)

    def avaliar_consequencias_digito(self, linha_digito: int, coluna_digito: int) ->dict:  # Retorno com dicionario. casas modificadas : list[tuple(decimal: int, linha: int , coluna: int]] pontuacao_nova: int
        casas_modificadas = []
        casas_pretas = self.Tabuleiro.achar_casas_pretas(linha_digito, coluna_digito)
        #print("casas pretas encontradas = ", casas_pretas)
        for casa in casas_pretas:
            pontos = 0
            grupo_completo = self.Tabuleiro.examinar_casas_brancas(casa[0], casa[1])
            if grupo_completo:
                #print("grupo completo = ", grupo_completo)
                decimal = self.Tabuleiro.calcular_decimal(casa[0], casa[1])
                cor = self.get_cor_jogador_da_vez()
                self.Tabuleiro.inserir_decimal(casa[0], casa[1], decimal, cor)
                pontos += self.calcular_pontos(decimal)
                casas_modificadas.append((decimal, casa[0], casa[1]))
            
            self.atualizar_pontuacao_jogador_da_vez(pontos)
        
        return {"casas_modificadas": casas_modificadas, "pontuacao_nova": self.get_pontuacao_jogador_da_vez()}

    def avaliar_fim_partida(self):
        if (self.Tabuleiro.verificar_tabuleiro_completo()):
            if (self.jogador_local.pontuacao == 1):
                self.set_vencedor(self.jogador_local)
            elif (self.jogador_remoto.pontuacao == 1):
                self.set_vencedor(self.jogador_remoto)
            else: 
                if self.jogador_local.pontuacao > self.jogador_remoto.pontuacao:
                    self.set_vencedor(self.jogador_local)
                else:
                    self.set_vencedor(self.jogador_remoto)
            self.partida_em_andamento = False
            return True   #partida acabou
        else:
            return False  #partida nao acabou
                

    def calcular_pontos(self, decimal: int) -> int: # Verificar se tem retorno msm
        match decimal:
            case 0:
                if self.jogador_da_vez == JogadorDaVez.LOCAL:
                    pontuacao_jogador_da_vez = self.jogador_local.get_pontuacao()
                else:
                    pontuacao_jogador_da_vez = self.jogador_remoto.get_pontuacao()
                pontos = -1 * pontuacao_jogador_da_vez
                return pontos
            case 1:
                numero_1s = self.Tabuleiro.contar_1s()
                if ((numero_1s % 3) == 0):
                    pontos = 1
                else:
                    pontos = 0
                return pontos
            case 2:
                numero_2s = self.Tabuleiro.contar_2s()
                if ((numero_2s % 3) == 0):
                    pontos = 2
                else: 
                    pontos = 0
                return pontos
            case 6:
                pontos = 2
                return pontos
            case 9:
                pontos = 3
                return pontos
        if ((decimal % 2) == 1):
            pontos = -1
            return pontos
        else:
            pontos = -2
        return pontos
        
        
    def confirmar_jogada(self) -> dict: # Retorno com dicionario. casas modificadas : list[tuple(decimal: int, linha: int , coluna: int]] pontuacao_nova: int
        self.Tabuleiro.confirmar_jogada()
        consequencias_jogada = self.avaliar_consequencias_digito(self.posicao_digito_inserido[0], self.posicao_digito_inserido[1])
        print("consequencias_jogada dentro de confirmar jogada DB = ", consequencias_jogada)
        self.set_jogador_da_vez(JogadorDaVez.REMOTO)
        self.casa_antiga = None
        self.digito_inserido = None
        self.posicao_digito_inserido = None
        partida_finalizada = self.avaliar_fim_partida()

        if partida_finalizada:
            self.estado_jogo = EstadoJogo.PARTIDA_FINALIZADA

        return consequencias_jogada
    

    def get_cor_jogador_da_vez(self) -> str:
        if self.jogador_da_vez == JogadorDaVez.LOCAL:
            return "red"
        else:
            return "blue"

    def get_dados_jogada(self) -> tuple[int, int, int]: # digito, coluna, linha
        return tuple()

    def get_digito_foi_inserido(self) -> bool:
        return self.digito_inserido

    def get_estado_jogo(self) -> EstadoJogo:
        return self.estado_jogo

    def get_pontuacao_jogador_da_vez(self) -> int:
        if self.jogador_da_vez == JogadorDaVez.LOCAL:
            return self.jogador_local.get_pontuacao()
        else:
            return self.jogador_remoto.get_pontuacao()
        
    def get_vecedor(self) -> JogadorDaVez:
        return self.vencedor

    def inserir_digito(self, digito: int, linha: int, coluna: int) -> tuple[int, int]:
        self.casa_antiga = self.Tabuleiro.inserir_digito(digito, linha, coluna)
        
        if self.casa_antiga is not None:
            self.digito_inserido = digito
            self.posicao_digito_inserido = (linha, coluna)

        return self.casa_antiga

    def obter_nomes_jogadores(self) -> tuple[str, str]: # inserir tipo de retorno no diagrama
        pass

    def receber_jogada(self, digito: int, linha: int, coluna: int) -> dict:
        self.Tabuleiro.inserir_digito_recebido(digito, linha, coluna)
        consequencias_jogada = self.avaliar_consequencias_digito(linha, coluna)
        
        partida_finalizada = self.avaliar_fim_partida()
        if partida_finalizada:
            self.estado_jogo = EstadoJogo.PARTIDA_FINALIZADA

        return consequencias_jogada

    def reiniciar_placar(self): # Verificar se é usado mesmo ou se não é responsa da interface
        pass

    def reiniciar_tabuleiro(self):
        pass

    def set_estado_jogo(self, estado: EstadoJogo):
        self.estado_jogo = estado

    def set_digito_foi_inserido(self, valor: bool):
        pass

    def set_digito_inserido(self, digito: int): #Atualizar argumento no diagrama
        pass

    def set_jogador_da_vez(self, jogador: JogadorDaVez):
        self.jogador_da_vez = jogador

    def set_posicao_digito_inserido(self, linha: int, coluna: int): # verificar e atualizar argumentos no diagrama e aqui
        pass
    
    def set_vencedor(self, jogador: JogadorDaVez): # verificar e atualizar argumentos no diagrama e aqui
        self.vencedor = jogador
    
    def update_nome_jogador(self, nome: str, jogador: int):
        if jogador == 1:
            self.jogador_local.set_nome(nome)
        else:
            self.jogador_remoto.set_nome(nome)
    
    def verificar_andamento_partida(self) -> bool:
        return self.partida_em_andamento

    def verificar_estado_inicial_tabuleiro(self) -> bool:
        if self.estado_jogo == EstadoJogo.INICIAL:
            return True
        else:
            return False

    def verificar_jogada(self) -> bool:
        pass
    
    def contar_um(self) -> int:
        pass


