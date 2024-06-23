
class Jogador():
    def __init__(self, nome: str, pontuacao: int):
        self.nome: str = nome
        self.pontuacao: int = pontuacao

    def __str__(self):
        return f'Nome: {self.nome} | Pontuação: {self.pontuacao}'
    
    def get_nome(self) -> str:
        return self.nome
    
    def set_nome(self, nome: str):
        self.nome = nome

    