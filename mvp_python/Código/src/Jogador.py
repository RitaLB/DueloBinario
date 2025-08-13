
class Jogador():
    def __init__(self, nome: str, pontuacao: tuple[int, int]):
        self.nome: str = nome
        self.pontuacao: tuple[int,int] = pontuacao

    def __str__(self):
        return f'Nome: {self.nome} | Pontuação: {self.pontuacao}'
    
    def get_nome(self) -> str:
        return self.nome
    
    def set_nome(self, nome: str):
        self.nome = nome

    def get_pontuacao(self) -> tuple[int,int]:
        return self.pontuacao
    
    def set_pontuacao(self, pontuacao: tuple[int,int]):
        self.pontuacao = pontuacao

    