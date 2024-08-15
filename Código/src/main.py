import sys
import os

from DOGGamePlayerInterface import DOGPlayerInterface
from LocalGamePlayerInterface import LocalPlayerInterface

def main():
    args = sys.argv
    modo_jogo = args[1]

    if modo_jogo == "1":
        LocalPlayerInterface()

    elif modo_jogo == "2":
        DOGPlayerInterface()
    
    else:
        print("Modo de jogo inválido. Por favor, escolha 1 ou 2.")

if __name__ == '__main__':
    main()

