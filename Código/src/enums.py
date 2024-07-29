from enum import Enum

class EstadoJogo(Enum):
    INICIAL = 1
    PARTIDA_EM_ANDAMENTO = 2
    PARTIDA_FINALIZADA = 3
    PARTIDA_ABANDONADA = 4

class JogadorDaVez(Enum):
    LOCAL = 1
    REMOTO = 2