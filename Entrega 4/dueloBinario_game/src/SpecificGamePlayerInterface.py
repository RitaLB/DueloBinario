from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import simpledialog
from dog.dog_interface import DogPlayerInterface
from dog.dog_actor import DogActor
import tkinter as tk

from Placar import Placar

from enums import EstadoJogo
from enums import JogadorDaVez

from DueloBinario import DueloBinario

class PlayerInterface(DogPlayerInterface):
    def __init__(self):
        self.main_Window = self.criar_main_window()
        self.main_Frame = Frame(self.main_Window, padx=32, pady=25, bg="white") 
        self.main_Frame.grid(row=1, column=1) # $
        self.tabuleiro: list[Label] = self.criar_tabuleiro()
        self.board_view = [] # verificar necessidade
        self.jogador_da_vez : JogadorDaVez = None
        self.jogo = DueloBinario("", "")
        self.menu_bar = Menu(self.main_Window) 
        self.menu_file : Menu = self.criar_menu() # verificar necessidade
        self.vencedor: JogadorDaVez = None
        self.placar: Placar = self.criar_pacar()
        self.mensagem_jogador_da_vez : Label = self.criar_mensagem_jogador_da_vez() # $
        self.botao_enviar_jogada: Button = self.criar_botao_enviar_jogada() # $
        self.start_status = None

        # FALTA ADICIONAR IMAGEM DE REGRA DE ORDEM DO NÚMERO

        # Configurações DOG
        self.configurar_dog()

        self.main_Window.mainloop()


    # ----- Funções inicialização -----

    def criar_main_window(self) -> tk.Tk:
        main_Window = tk.Tk()
        main_Window.title("Duelo Binário")
        main_Window.geometry("1000x650")
        main_Window.resizable(False, False)
        main_Window["bg"] = "white"

        #Título
        titulo_image = Image.open("imagens/titulo.png")
        l, h = titulo_image.size
        nl = int(l * 0.7)
        nh = int(h * 0.7)
        titulo_image = titulo_image.resize((nl, nh))
        # Cria um objeto PhotoImage a partir da imagem redimensionada
        self.titulo_image = ImageTk.PhotoImage(titulo_image)

        self.titulo_frame = Frame(main_Window, padx=4,  pady=1, bg="white")
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
        self.regras_frame = Frame(main_Window, padx=4,  pady=1, bg="white")
        self.regras_frame.grid(row=1, column=2)
        self.label_regras = Label(self.regras_frame, image = self.regras_image)
        self.label_regras.grid(row=2, column= 0, columnspan=3)

        return main_Window

    '''
    def criar_mensagem_jogador_da_vez(self) -> Label:
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
        label_vez = Label(self.linha_frame, image = self.vez_image)
        label_vez.grid(row=0, column= 0)

        return label_vez
    '''
    def criar_botao_enviar_jogada(self) -> Button:
        #Botão enviar jogada
        self.enviar_jogada_button = Button(self.linha_frame , text = "Enviar jogada", command= self.enviar_jogada )
        self.enviar_jogada_button.grid(row=0, column=2)

    def criar_mensagem_jogador_da_vez(self) -> Label:
        # Terceira linha frame
        self.linha_frame = Frame(self.main_Window, padx=4, pady=1, bg="white")
        self.linha_frame.grid(row=2, column=1)

        # "Está na vez de:"
        label_texto = Label(self.linha_frame, text="Está na vez de:", bg="white")
        label_texto.grid(row=0, column=0)

        # Imagem colorida do jogador da vez
        cor = "gray"
        self.img_vez = tk.PhotoImage(width=30, height=30)
        self.img_vez.put(cor, to=(0, 0, 30, 30))
        label_vez = Label(self.linha_frame, image=self.img_vez, bg="black")
        label_vez.grid(row=0, column=1)

        return label_vez
    def atualizar_mensagem_jogador_da_vez(self):
        if self.jogador_da_vez == JogadorDaVez.LOCAL:
            cor = "red"
        else:
            cor = "blue"
        self.img_vez.put(cor, to=(0, 0, 30, 30))
        self.linha_frame.update()

    def criar_menu(self) -> Menu:
        menu_file = Menu(self.menu_bar, tearoff=0)
        menu_file.add_command(label="Iniciar Jogo", command=self.iniciar_partida)
        menu_file.add_command(label="Novo Jogo", command=self.novo_jogo)
        # Adicionando o menu "Jogo" à barra de menu
        self.menu_bar.add_cascade(label="Menu", menu=menu_file)
        # Configurando a barra de menu
        self.main_Window.config(menu=self.menu_bar)

        return menu_file

    def criar_pacar(self) -> Placar:
        self.placar_frame = Frame(self.main_Window, padx=4,  pady=1, bg="white", borderwidth=1, relief="solid")
        self.placar_frame.grid(row=1, column=0)
        placar = Placar(self.placar_frame, "Player 1", "Player 2", 0, 0, "red", "blue")
        placar.pack()

        return placar
    
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
                    aLabel.bind("<Button-3>", lambda event, line=y+1, column=x+1: self.click_casa_branca(event, 0, line, column))
                    aLabel.bind("<Button-1>", lambda event, line=y+1, column=x+1: self.click_casa_branca(event, 1, line, column))
                aLabel.grid(row=x , column=y)
                viewTier.append(aLabel)
            boardView.append(viewTier)

        return boardView
    


    def configurar_dog(self):
        player_name = simpledialog.askstring(title="Player identification", prompt="Qual o seu nome?")

        self.placar.update_player_names(player_name, 1)
        self.jogo.update_nome_jogador(player_name, 1)
        #continuar conexão com DOG
        self.dog_server_interface = DogActor()
        message = self.dog_server_interface.initialize(player_name, self)
        messagebox.showinfo(message=message)

    # ----- Função botão ----
    def enviar_jogada(self):
        messagebox.showinfo("enviar jogada", "Você clicou em 'enviar jogada' !")

    # --- Funções clique mouse casas ----
    def click_casa_branca(self, event, digito, linha, coluna):
        if self.jogador_da_vez == JogadorDaVez.LOCAL:
            if digito == 0:
                self.left_click(linha, coluna)
            else:
                self.right_click(linha, coluna)

    def right_click(self, linha, coluna):
        self.jogo.inserir_digito(1, linha, coluna)
        self.tabuleiro[linha-1][coluna-1].configure(image=self.zero_preto)
        #self.tabuleiro[linha % len(self.tabuleiro)][coluna % len(self.tabuleiro[0])] = 0
                
    def left_click(self, linha, coluna):
        self.jogo.inserir_digito(0, linha, coluna)
        self.tabuleiro[linha-1][coluna-1].configure(image=self.um_preto)
        #self.tabuleiro[linha % len(self.tabuleiro)][coluna % len(self.tabuleiro[0])] = 0

    # ------ Funções menu -----
    def iniciar_partida(self): #Deveria ser "iniciar partida"?
        messagebox.showinfo("iniciar jogo", "Você clicou em 'iniciar jogo' !")
        partida_em_andamento = self.jogo.verificar_andamento_partida()

        if partida_em_andamento:
            messagebox.showinfo("Partida em andamento", "Já existe uma partida em andamento!")
            return
        
        tabuleiro_estado_inicial = self.jogo.verificar_estado_inicial_tabuleiro()
        if not tabuleiro_estado_inicial:
            messagebox.showinfo("Tabuleiro não está no estado inicial", "Clique em 'Novo Jogo' para reiniciar o estado do tabuleiro!")
            return
        
        self.start_status = self.dog_server_interface.start_match(2)
        
        j = self.start_status.get_players()
        jogador_2 = self.start_status.get_players()[1][0] 
        self.placar.update_player_names(jogador_2, 2)
        self.jogo.update_nome_jogador(jogador_2, 2)

        self.set_estado_jogo(EstadoJogo.PARTIDA_EM_ANDAMENTO)
        self.set_jogador_da_vez(JogadorDaVez.LOCAL)
        self.atualizar_mensagem_jogador_da_vez()

        message = self.start_status.get_message()
        messagebox.showinfo(message=message)


    def novo_jogo(self):
        messagebox.showinfo("novo jogo", "Você clicou em 'novo jogo' !")

    def set_estado_jogo(self, estado: EstadoJogo):
        self.jogo.set_estado_jogo(estado)

    def set_jogador_da_vez(self, jogador: JogadorDaVez):
        self.jogador_da_vez = jogador
        self.jogo.set_jogador_da_vez(jogador)

    # ----- Funções DOG ----
    def receive_start(self, start_status):
        messagebox.showinfo("iniciar jogo", "Você recebeu uma solicitação de inicio de jogo!' !")
        message = start_status.get_message()
        messagebox.showinfo(message=message)
        jogador_2 = start_status.get_players()[1][0] 

        self.placar.update_player_names(jogador_2, 2)
        self.set_estado_jogo(EstadoJogo.PARTIDA_EM_ANDAMENTO)
        self.set_jogador_da_vez(JogadorDaVez.REMOTO)
        self.atualizar_mensagem_jogador_da_vez()


PlayerInterface()

