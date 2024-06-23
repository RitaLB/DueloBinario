from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import simpledialog
from dog.dog_interface import DogPlayerInterface
from dog.dog_actor import DogActor
import tkinter as tk

from Placar import Placar

class PlayerInterface(DogPlayerInterface):
    def __init__(self):
        self.main_Window = Tk()
        self.main_Window.title("Duelo Binário")
        #self.main_Window.iconbitmap("images/icon.ico")
        #self.main_Window.geometry("1400x900")
        self.main_Window.geometry("1000x650")
        self.main_Window.resizable(False, False)
        self.main_Window["bg"] = "white"

        # FALTA ADICIONAR IMAGEM DE REGRA DE ORDEM DO NÚMERO

        # Criando um menu 
        self.menu_bar = Menu(self.main_Window)
        # Criando uma opção de menu "Jogo"
        self.jogo_menu = Menu(self.menu_bar, tearoff=0)
        self.jogo_menu.add_command(label="Iniciar Jogo", command=self.iniciar_jogo)
        self.jogo_menu.add_command(label="Novo Jogo", command=self.novo_jogo)
        # Adicionando o menu "Jogo" à barra de menu
        self.menu_bar.add_cascade(label="Menu", menu=self.jogo_menu)
        # Configurando a barra de menu
        self.main_Window.config(menu=self.menu_bar)

        #Título
        titulo_image = Image.open("imagens/titulo.png")
        l, h = titulo_image.size
        nl = int(l * 0.7)
        nh = int(h * 0.7)
        titulo_image = titulo_image.resize((nl, nh))
        # Cria um objeto PhotoImage a partir da imagem redimensionada
        self.titulo_image = ImageTk.PhotoImage(titulo_image)

        self.titulo_frame = Frame(self.main_Window, padx=4,  pady=1, bg="white")
        self.titulo_frame.grid(row=0, column=1)
        self.label_titulo = Label(self.titulo_frame, image = self.titulo_image)
        self.label_titulo.grid(row=0, column= 0, columnspan=3)

        #Regras
        regras_image = Image.open("imagens/regras.png")
        l, h = regras_image.size
        nl = int(l * 0.8)
        nh = int(h * 0.8)
        regras_image = regras_image.resize((nl, nh))
        # Cria um objeto PhotoImage a partir da imagem redimensionada
        self.regras_image = ImageTk.PhotoImage(regras_image)
        #self.regras_image = PhotoImage(file="imagens/regras.png")
        self.regras_frame = Frame(self.main_Window, padx=4,  pady=1, bg="white")
        self.regras_frame.grid(row=1, column=2)
        self.label_regras = Label(self.regras_frame, image = self.regras_image)
        self.label_regras.grid(row=2, column= 0, columnspan=3)

        #Placar
        self.placar_frame = Frame(self.main_Window, padx=4,  pady=1, bg="white", borderwidth=1, relief="solid")
        self.placar_frame.grid(row=1, column=0)
        #self.label_placar = Label(self.placar_frame, image = self.placar_image)
        #self.label_placar.grid(row=2, column= 0, columnspan=3)
        
        self.placar = Placar(self.placar_frame, "Player 1", "Player 2", 0, 0, "red", "blue")
        self.placar.pack()

        #Terceira linha frame
        self.linha_frame = Frame(self.main_Window, padx=4,  pady=1, bg="white")
        self.linha_frame.grid(row=2, column=1)

        #"Está na vez de"
        vez_image = Image.open("imagens/vez.png")
        l, h = vez_image.size
        nl = int(l * 0.7)
        nh = int(h * 0.7)
        vez_image = vez_image.resize((nl, nh))
        # Cria um objeto PhotoImage a partir da imagem redimensionada
        self.vez_image = ImageTk.PhotoImage(vez_image)
        #self.vez_image = PhotoImage(file="imagens/vez.png"))
        self.label_vez = Label(self.linha_frame, image = self.vez_image)
        self.label_vez.grid(row=0, column= 0)


        #Botão enviar jogada
        self.enviar_jogada_button = Button(self.linha_frame , text = "Enviar jogada", command= self.enviar_jogada )
        self.enviar_jogada_button.grid(row=0, column=1)


        # Tabuleiro
        self.main_Frame = Frame(self.main_Window, padx=32, pady=25, bg="white")
        self.main_Frame.grid(row=1, column=1)

        # Criando Tabuleiro
        self.tabuleiro = self.criar_tabuleiro()

        # Configurações DOG
        player_name = simpledialog.askstring(title="Player identification", prompt="Qual o seu nome?")
        # Atualizar nome do jogador local no placar
        self.placar.update_player_names(player_name, 1)
        #continuar conexão com DOG
        self.dog_server_interface = DogActor()
        message = self.dog_server_interface.initialize(player_name, self)
        messagebox.showinfo(message=message)

        self.main_Window.mainloop()

    # Funções dígito
    def right_click(self, event, linha, coluna):
        self.tabuleiro[linha-1][coluna-1].configure(image=self.zero_preto)
        #self.tabuleiro[linha % len(self.tabuleiro)][coluna % len(self.tabuleiro[0])] = 0
                
    def left_click(self, event, linha, coluna):
        self.tabuleiro[linha-1][coluna-1].configure(image=self.um_preto)
        #self.tabuleiro[linha % len(self.tabuleiro)][coluna % len(self.tabuleiro[0])] = 0

    # Função botão
    def enviar_jogada(self):
        messagebox.showinfo("enviar jogada", "Você clicou em 'enviar jogada' !")

    # Funções menu
    def iniciar_jogo(self): #Deveria ser "iniciar partida"?
        messagebox.showinfo("iniciar jogo", "Você clicou em 'iniciar jogo' !")
        start_status = self.dog_server_interface.start_match(2)
        j = start_status.get_players()
        jogador_2 = start_status.get_players()[1][0] 
        self.placar.update_player_names(jogador_2, 2)
        message = start_status.get_message()
        messagebox.showinfo(message=message)

    def novo_jogo(self):
        messagebox.showinfo("novo jogo", "Você clicou em 'novo jogo' !")

    #Funções DOG
    def receive_start(self, start_status):
        message = start_status.get_message()
        messagebox.showinfo(message=message)
        jogador_2 = start_status.get_players()[1][0] 
        self.placar.update_player_names(jogador_2, 2)

    def criar_tabuleiro(self) -> list[Label]:

        #Imagens Tabuleiro
        #Casas brancas
        img_empty_white = Image.open("imagens/white_square.png")
        l, h = img_empty_white.size
        nl = int(l * 0.7)
        nh = int(h * 0.7)
        img_empty_white = img_empty_white.resize((nl, nh))
        self.empty_white = ImageTk.PhotoImage(img_empty_white) #Porque prescisa do self? 

        #Casas pretas
        img_empty_black = Image.open("imagens/black_square.png")
        l, h = img_empty_black.size
        nl = int(l * 0.7)
        nh = int(h * 0.7)
        img_empty_black = img_empty_black.resize((nl, nh))
        self.empty_black = ImageTk.PhotoImage(img_empty_black)

        # Dígito 1
        um_preto= Image.open("imagens/um.png")
        l, h = um_preto.size
        nl = int(l * 0.7)
        nh = int(h * 0.7)
        um_preto = um_preto.resize((nl, nh))
        self.um_preto = ImageTk.PhotoImage(um_preto)

        # Dígito 0
        zero_preto= Image.open("imagens/0.png")
        l, h = zero_preto.size
        nl = int(l * 0.7)
        nh = int(h * 0.7)
        zero_preto = zero_preto.resize((nl, nh))
        self.zero_preto = ImageTk.PhotoImage(zero_preto)

        boardView = []
        for y in range(12):
            viewTier = []
            for x in range(12):
                if (x + y) % 2 == 0:
                    aLabel = Label(self.main_Frame, bd=2, relief="solid", image=self.empty_black)
                else:
                    aLabel = Label(self.main_Frame, bd=2, relief="solid", image=self.empty_white)
                    aLabel.bind("<Button-3>", lambda event, line=y+1, column=x+1: self.right_click(event, line, column))
                    aLabel.bind("<Button-1>", lambda event, line=y+1, column=x+1: self.left_click(event, line, column))
                aLabel.grid(row=x , column=y)
                viewTier.append(aLabel)
            boardView.append(viewTier)

        return boardView


PlayerInterface()

