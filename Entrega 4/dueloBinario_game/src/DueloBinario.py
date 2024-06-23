
from Jogador import Jogador
from Tabuleiro import Tabuleiro

from enums import EstadoJogo
from enums import JogadorDaVez

class DueloBinario():
    def __init__(self, nome_jogador_local: str, nome_jogador_remoto: str):
        self.digito_inserido: int = None
        self.digito_foi_inserido: bool = False
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
        pass

    def avaliar_consequencias_digito(self, linha_digito: int, coluna_digito: int):
        pass

    def avaliar_fim_partida(self):
        pass

    def calcular_pontos(self, decimal: int) -> int: # Verificar se tem retorno msm
        pass

    def confirmar_jogada(self):
        pass

    def get_cor_jogador_da_vez(self) -> str:
        pass

    def get_dados_jogada(self) -> tuple[int, int, int]: # digito, coluna, linha
        pass

    def get_digito_foi_inserido(self) -> bool:
        pass

    def get_estado_jogo(self) -> EstadoJogo:
        pass

    def get_vecedor(self) -> JogadorDaVez:
        pass

    def inserir_digito(self, digito: int, linha: int, coluna: int) :
        self.digito_foi_inserido = self.Tabuleiro.inserir_digito(digito, linha, coluna)
        if self.digito_foi_inserido:
            self.digito_inserido = digito
            self.posicao_digito_inserido = (linha, coluna)

    def obter_nomes_jogadores(self) -> tuple[str, str]: # inserir tipo de retorno no diagrama
        pass

    def receber_jogada(self, digito: int, linha: int, coluna: int):
        pass

    def reiniciar_placar(self): # Verificar se é usado mesmo ou se não é responsa da interface
        pass

    def reiniciar_tabuleiro(self):
        pass

    def set_estado_jogo(self, estado: EstadoJogo):
        pass

    def set_digito_foi_inserido(self, valor: bool):
        pass

    def set_digito_inserido(self, digito: int): #Atualizar argumento no diagrama
        pass

    def set_jogador_da_vez(self, jogador: JogadorDaVez):
        self.jogador_da_vez = jogador

    def set_posicao_digito_inserido(self, linha: int, coluna: int): # verificar e atualizar argumentos no diagrama e aqui
        pass
    
    def set_vencedor(self, jogador: JogadorDaVez): # verificar e atualizar argumentos no diagrama e aqui
        pass
    
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


