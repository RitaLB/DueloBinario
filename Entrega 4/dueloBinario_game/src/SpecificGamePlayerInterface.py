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
# FALTA CONFIGURAR MUDANÇA NA COR DO DÍGITO INSERIDO AO CLICAR EM "ENVIAR JOGADA"
class PlayerInterface(DogPlayerInterface):
    def __init__(self):
        self.main_Window = self.criar_main_window()
        self.main_Frame = Frame(self.main_Window, padx=32, pady=25, bg="white")
        self.main_Frame.grid(row=1, column=1) # $
        self.tabuleiro: list[Label] = self.criar_tabuleiro()
        self.board_view = []
        self.dados_jogada_atual: dict = None
        self.estado_jogo : EstadoJogo = EstadoJogo.INICIAL
        self.jogador_da_vez : JogadorDaVez = None
        self.jogo = DueloBinario("", "")
        self.menu_bar = Menu(self.main_Window)
        self.menu_file : Menu = self.criar_menu() # verificar necessidade
        self.vencedor: JogadorDaVez = None
        self.mensagem_jogador_da_vez : Label = self.criar_mensagem_jogador_da_vez() # $
        self.botao_enviar_jogada: Button = self.criar_botao_enviar_jogada() # $
        self.start_status = None
        self.inicializar_imagem_decimais()

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
        self.regras_frame = Frame(main_Window, padx=4,  pady=4, bg="white")
        self.regras_frame.grid(row=1, column=2)
        self.label_regras = Label(self.regras_frame, image = self.regras_image)
        self.label_regras.grid(row=2, column= 0)

        #Placar e ordem digitos

        self.placar_e_ordem_frame = Frame(main_Window, padx=7,  pady=1, bg="white")
        self.placar_e_ordem_frame.grid(row=1, column=0)

            #placar
        self.placar_frame = Frame(self.placar_e_ordem_frame, padx=4,  pady=4, bg="white", borderwidth=1, relief="solid")
        self.placar_frame.grid(row=0, column=0)
        self.placar = Placar(self.placar_frame, "Player 1", "Player 2", 0, 0, "red", "blue")

            #Regra de ordem dos dígitos
        img_ordem = Image.open("imagens/ordem.png")
        l, h = img_ordem.size
        nl = int(l * 0.8)
        nh = int(h * 0.8)
        img_ordem = img_ordem.resize((nl, nh))
        self.img_ordem = ImageTk.PhotoImage(img_ordem)
        self.ordem_frame = Frame(self.placar_e_ordem_frame, padx=4,  pady=4, bg="white")
        self.ordem_frame.grid(row=1, column=0)
        self.label_ordem = Label(self.ordem_frame, image = self.img_ordem)
        self.label_ordem.grid(row=2, column= 0)


        return main_Window

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


    def criar_menu(self) -> Menu:
        menu_file = Menu(self.menu_bar, tearoff=0)
        menu_file.add_command(label="Iniciar Jogo", command=self.iniciar_partida)
        menu_file.add_command(label="Reiniciar Tabuleiro", command=self.novo_jogo)
        # Adicionando o menu "Jogo" à barra de menu
        self.menu_bar.add_cascade(label="Menu", menu=menu_file)
        # Configurando a barra de menu
        self.main_Window.config(menu=self.menu_bar)

        return menu_file



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

        # Dígito 1 preto
        um_preto= Image.open("imagens/um.png")
        l, h = um_preto.size
        nl = int(l * 0.7)
        nh = int(h * 0.7)
        um_preto = um_preto.resize((nl, nh))
        self.um_preto = ImageTk.PhotoImage(um_preto)

        # Dígito 1 azul
        um_azul= Image.open("imagens/1A.png")
        l, h = um_azul.size
        nl = int(l * 0.7)
        nh = int(h * 0.7)
        um_azul = um_azul.resize((nl, nh))
        self.um_azul = ImageTk.PhotoImage(um_azul)

        # Dígito 0 preto
        zero_preto= Image.open("imagens/0.png")
        l, h = zero_preto.size
        nl = int(l * 0.7)
        nh = int(h * 0.7)
        zero_preto = zero_preto.resize((nl, nh))
        self.zero_preto = ImageTk.PhotoImage(zero_preto)

        # Dígito 0 azul
        zero_azul= Image.open("imagens/0A.png")
        l, h = zero_azul.size
        nl = int(l * 0.7)
        nh = int(h * 0.7)
        zero_azul = zero_azul.resize((nl, nh))
        self.zero_azul = ImageTk.PhotoImage(zero_azul)

        boardView = []
        for x in range(12):
            viewTier = []
            for y in range(12):
                if (x + y) % 2 == 0:
                    aLabel = Label(self.main_Frame, bd=2, relief="solid", image=self.empty_black)
                else:
                    aLabel = Label(self.main_Frame, bd=2, relief="solid", image=self.empty_white)
                    aLabel.bind("<Button-3>", lambda event, line=x, column=y: self.click_casa_branca(event, 0, line, column))
                    aLabel.bind("<Button-1>", lambda event, line=x, column=y: self.click_casa_branca(event, 1, line, column))
                aLabel.grid(row=x , column=y)
                viewTier.append(aLabel)
            boardView.append(viewTier)

        return boardView

    def inicializar_imagem_decimais(self):
        d0_v= Image.open("imagens/D0_V.png")
        l, h = d0_v.size
        nl = int(l * 0.7)
        nh = int(h * 0.7)
        d0_v = d0_v.resize((nl, nh))
        self.D0_vermelho = ImageTk.PhotoImage(d0_v)

        d0_A= Image.open("imagens/D0_A.png")
        l, h = d0_A.size
        nl = int(l * 0.7)
        nh = int(h * 0.7)
        d0_A = d0_A.resize((nl, nh))
        self.D0_azul = ImageTk.PhotoImage(d0_A)

        d1_v= Image.open("imagens/D1_V.png")
        l, h = d1_v.size
        nl = int(l * 0.7)
        nh = int(h * 0.7)
        d1_v = d1_v.resize((nl, nh))
        self.D1_vermelho = ImageTk.PhotoImage(d1_v)

        d1_A= Image.open("imagens/D1_A.png")
        l, h = d1_A.size
        nl = int(l * 0.7)
        nh = int(h * 0.7)
        d1_A = d1_A.resize((nl, nh))
        self.D1_azul = ImageTk.PhotoImage(d1_A)

        d2_v= Image.open("imagens/D2_V.png")
        l, h = d2_v.size
        nl = int(l * 0.7)
        nh = int(h * 0.7)
        d2_v = d2_v.resize((nl, nh))
        self.D2_vermelho = ImageTk.PhotoImage(d2_v)

        d2_A= Image.open("imagens/D2_A.png")
        l, h = d2_A.size
        nl = int(l * 0.7)
        nh = int(h * 0.7)
        d2_A = d2_A.resize((nl, nh))
        self.D2_azul = ImageTk.PhotoImage(d2_A)

        d3_v= Image.open("imagens/D3_V.png")
        l, h = d3_v.size
        nl = int(l * 0.7)
        nh = int(h * 0.7)
        d3_v = d3_v.resize((nl, nh))
        self.D3_vermelho = ImageTk.PhotoImage(d3_v)

        d3_A= Image.open("imagens/D3_A.png")
        l, h = d3_A.size
        nl = int(l * 0.7)
        nh = int(h * 0.7)
        d3_A = d3_A.resize((nl, nh))
        self.D3_azul = ImageTk.PhotoImage(d3_A)

        d4_v= Image.open("imagens/D4_V.png")
        l, h = d4_v.size
        nl = int(l * 0.7)
        nh = int(h * 0.7)
        d4_v = d4_v.resize((nl, nh))
        self.D4_vermelho = ImageTk.PhotoImage(d4_v)

        d4_A= Image.open("imagens/D4_A.png")
        l, h = d4_A.size
        nl = int(l * 0.7)
        nh = int(h * 0.7)
        d4_A = d4_A.resize((nl, nh))
        self.D4_azul = ImageTk.PhotoImage(d4_A)

        d5_v= Image.open("imagens/D5_V.png")
        l, h = d5_v.size
        nl = int(l * 0.7)
        nh = int(h * 0.7)
        d5_v = d5_v.resize((nl, nh))
        self.D5_vermelho = ImageTk.PhotoImage(d5_v)

        d5_A= Image.open("imagens/D5_A.png")
        l, h = d5_A.size
        nl = int(l * 0.7)
        nh = int(h * 0.7)
        d5_A = d5_A.resize((nl, nh))
        self.D5_azul = ImageTk.PhotoImage(d5_A)

        d6_v= Image.open("imagens/D6_V.png")
        l, h = d6_v.size
        nl = int(l * 0.7)
        nh = int(h * 0.7)
        d6_v = d6_v.resize((nl, nh))
        self.D6_vermelho = ImageTk.PhotoImage(d6_v)

        d6_A= Image.open("imagens/D6_A.png")
        l, h = d6_A.size
        nl = int(l * 0.7)
        nh = int(h * 0.7)
        d6_A = d6_A.resize((nl, nh))
        self.D6_azul = ImageTk.PhotoImage(d6_A)

        d7_v= Image.open("imagens/D7_V.png")
        l, h = d7_v.size
        nl = int(l * 0.7)
        nh = int(h * 0.7)
        d7_v = d7_v.resize((nl, nh))
        self.D7_vermelho = ImageTk.PhotoImage(d7_v)

        d7_A= Image.open("imagens/D7_A.png")
        l, h = d7_A.size
        nl = int(l * 0.7)
        nh = int(h * 0.7)
        d7_A = d7_A.resize((nl, nh))
        self.D7_azul = ImageTk.PhotoImage(d7_A)

        d8_v= Image.open("imagens/D8_V.png")
        l, h = d8_v.size
        nl = int(l * 0.7)
        nh = int(h * 0.7)
        d8_v = d8_v.resize((nl, nh))
        self.D8_vermelho = ImageTk.PhotoImage(d8_v)

        d8_A= Image.open("imagens/D8_A.png")
        l, h = d8_A.size
        nl = int(l * 0.7)
        nh = int(h * 0.7)
        d8_A = d8_A.resize((nl, nh))
        self.D8_azul = ImageTk.PhotoImage(d8_A)

        d9_v= Image.open("imagens/D9_V.png")
        l, h = d9_v.size
        nl = int(l * 0.7)
        nh = int(h * 0.7)
        d9_v = d9_v.resize((nl, nh))
        self.D9_vermelho = ImageTk.PhotoImage(d9_v)

        d9_A= Image.open("imagens/D9_A.png")
        l, h = d9_A.size
        nl = int(l * 0.7)
        nh = int(h * 0.7)
        d9_A = d9_A.resize((nl, nh))
        self.D9_azul = ImageTk.PhotoImage(d9_A)

    def configurar_dog(self):
        player_name = simpledialog.askstring(title="Player identification", prompt="Qual o seu nome?")

        self.placar.update_player_names(player_name, 1)
        self.jogo.update_nome_jogador(player_name, 1)
        #continuar conexão com DOG
        self.dog_server_interface = DogActor()
        message = self.dog_server_interface.initialize(player_name, self)
        messagebox.showinfo(message=message)

    def reiniciar_tabuleiro(self):
        for x in range(12):
            for y in range(12):
                if (x + y) % 2 == 0:
                    self.tabuleiro[x][y].configure(image=self.empty_black)
                else:
                    self.tabuleiro[x][y].configure(image=self.empty_white)

    def reiniciar_placar(self):
        self.placar.update_player_score(0, 0)
        self.placar.update_player_score(1, 0)


    # --- Funções clique mouse casas ----
    def click_casa_branca(self, event, digito, linha, coluna):
        if self.jogador_da_vez == JogadorDaVez.LOCAL and self.estado_jogo == EstadoJogo.PARTIDA_EM_ANDAMENTO:
            if digito == 0:
                self.left_click(linha, coluna)

            else:
                self.right_click(linha, coluna)

    def right_click(self, linha, coluna):
        casa_antiga = self.jogo.inserir_digito(0, linha, coluna)
        if casa_antiga:
            if casa_antiga[0] != -1:
                self.tabuleiro[casa_antiga[0]][casa_antiga[1]].configure(image=self.empty_white)
            self.tabuleiro[linha][coluna].configure(image=self.zero_azul)
            self.dados_jogada_atual = {"digito": 0, "linha": linha, "coluna": coluna}


    def left_click(self, linha, coluna):
        casa_antiga = self.jogo.inserir_digito(1, linha, coluna)
        if casa_antiga:
            if casa_antiga[0] != -1:
                self.tabuleiro[casa_antiga[0]][casa_antiga[1]].configure(image=self.empty_white)
            self.tabuleiro[linha][coluna].configure(image=self.um_azul)
            self.dados_jogada_atual = {"digito": 1, "linha": linha, "coluna": coluna}


    # ------ Funções menu -----
    def iniciar_partida(self):
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

        try:
            jogador_2 = self.start_status.get_players()[1][0]
        except Exception as e:
            print("Erro ao tentar iniciar partida: ", e)
            messagebox.showinfo("Erro", "Não há outro jogador disponível no momento!")
            self.placar.update_player_names("Jogador 2", 2)
            return

        self.placar.update_player_names(jogador_2, 2)
        self.jogo.update_nome_jogador(jogador_2, 2)

        self.set_estado_jogo(EstadoJogo.PARTIDA_EM_ANDAMENTO)
        self.set_jogador_da_vez(JogadorDaVez.LOCAL)
        self.atualizar_mensagem_jogador_da_vez()

        message = self.start_status.get_message()
        messagebox.showinfo(message=message)


    def novo_jogo(self):
        if self.jogo.get_estado_jogo() == EstadoJogo.PARTIDA_EM_ANDAMENTO:
            messagebox.showinfo("Partida em andamento", "Não é possível reiniciar o jogo enquanto a partida estiver em andamento!")
            return
        if self.jogo.get_estado_jogo() == EstadoJogo.INICIAL:
            messagebox.showinfo("Estado inicial", "O jogo já está em seu estado inicial. Inicie uma partida para jogar!")
            return

        self.jogo.reiniciar_jogo()
        self.set_estado_jogo(EstadoJogo.INICIAL)
        self.reiniciar_tabuleiro()
        self.reiniciar_placar()
        self.placar.update_player_names("Jogador 2", 2)
        messagebox.showinfo("Tabuleiro reiniciado", "Clique em 'Iniciar Jogo' para começar uma nova partida!")

    # ----- Funcoes set ,  get e atualização-----
    def atualizar_mensagem_jogador_da_vez(self):
        if self.jogador_da_vez == JogadorDaVez.LOCAL:
            cor = "red"
        else:
            cor = "blue"
        self.img_vez.put(cor, to=(0, 0, 30, 30))
        self.linha_frame.update()

    def set_estado_jogo(self, estado: EstadoJogo):
        self.jogo.set_estado_jogo(estado)
        self.estado_jogo = estado

    def set_jogador_da_vez(self, jogador: JogadorDaVez):
        self.jogador_da_vez = jogador
        self.jogo.set_jogador_da_vez(jogador)

    def atualizar_tabuleiro(self, casas_modificadas: list[tuple[int, int, int]]):
        # casas_modificadas = list[tuple(decimal: int, linha: int , coluna: int]]
        for casa in casas_modificadas:
            decimal = casa[0]
            linha = casa[1]
            coluna = casa[2]

            self.atualizar_casa_preta(decimal, linha, coluna)

    def atualizar_casa_preta(self, decimal, linha, coluna):
        match decimal:
            case 0:
                if self.jogador_da_vez == JogadorDaVez.LOCAL:
                    self.tabuleiro[linha][coluna].configure(image=self.D0_vermelho)
                else:
                    self.tabuleiro[linha][coluna].configure(image=self.D0_azul)
            case 1:
                if self.jogador_da_vez == JogadorDaVez.LOCAL:
                    self.tabuleiro[linha][coluna].configure(image=self.D1_vermelho)
                else:
                    self.tabuleiro[linha][coluna].configure(image=self.D1_azul)
            case 2:
                if self.jogador_da_vez == JogadorDaVez.LOCAL:
                    self.tabuleiro[linha][coluna].configure(image=self.D2_vermelho)
                else:
                    self.tabuleiro[linha][coluna].configure(image=self.D2_azul)
            case 3:
                if self.jogador_da_vez == JogadorDaVez.LOCAL:
                    self.tabuleiro[linha][coluna].configure(image=self.D3_vermelho)
                else:
                    self.tabuleiro[linha][coluna].configure(image=self.D3_azul)
            case 4:
                if self.jogador_da_vez == JogadorDaVez.LOCAL:
                    self.tabuleiro[linha][coluna].configure(image=self.D4_vermelho)
                else:
                    self.tabuleiro[linha][coluna].configure(image=self.D4_azul)
            case 5:
                if self.jogador_da_vez == JogadorDaVez.LOCAL:
                    self.tabuleiro[linha][coluna].configure(image=self.D5_vermelho)
                else:
                    self.tabuleiro[linha][coluna].configure(image=self.D5_azul)
            case 6:
                if self.jogador_da_vez == JogadorDaVez.LOCAL:
                    self.tabuleiro[linha][coluna].configure(image=self.D6_vermelho)
                else:
                    self.tabuleiro[linha][coluna].configure(image=self.D6_azul)
            case 7:
                if self.jogador_da_vez == JogadorDaVez.LOCAL:
                    self.tabuleiro[linha][coluna].configure(image=self.D7_vermelho)
                else:
                    self.tabuleiro[linha][coluna].configure(image=self.D7_azul)
            case 8:
                if self.jogador_da_vez == JogadorDaVez.LOCAL:
                    self.tabuleiro[linha][coluna].configure(image=self.D8_vermelho)
                else:
                    self.tabuleiro[linha][coluna].configure(image=self.D8_azul)
            case 9:
                if self.jogador_da_vez == JogadorDaVez.LOCAL:
                    self.tabuleiro[linha][coluna].configure(image=self.D9_vermelho)
                else:
                    self.tabuleiro[linha][coluna].configure(image=self.D9_azul)

    def inserir_digito_recebido(self, digito: int, linha: int, coluna: int):
        match digito:
            case 0:
                self.tabuleiro[linha][coluna].configure(image=self.zero_preto)
            case 1:
                self.tabuleiro[linha][coluna].configure(image=self.um_preto)

   # ----- Função botão ----
    def enviar_jogada(self):
        if self.jogador_da_vez == JogadorDaVez.LOCAL:
            if self.dados_jogada_atual:
                digito = self.dados_jogada_atual["digito"]
                linha = self.dados_jogada_atual["linha"]
                coluna = self.dados_jogada_atual["coluna"]
                # casas modificadas -> casas modificadas :
                # list[tuple(decimal: int, linha: int , coluna: int]]
                # pontuacao_nova: int ;
                consequencias_jogada : dict = self.jogo.confirmar_jogada()

                casas_modificadas: list[tuple[int, int, int]] = consequencias_jogada["casas_modificadas"]

                if digito == 0:
                    self.tabuleiro[linha][coluna].configure(image=self.zero_preto)
                else:
                    self.tabuleiro[linha][coluna].configure(image=self.um_preto)
                self.atualizar_tabuleiro(casas_modificadas)

                self.placar.update_player_score(0, consequencias_jogada["pontuacao_nova"])
                self.jogador_da_vez = JogadorDaVez.REMOTO

                self.set_estado_jogo(self.jogo.get_estado_jogo())

                if self.estado_jogo == EstadoJogo.PARTIDA_FINALIZADA:

                    self.vencedor = self.jogo.get_vecedor()
                    messagebox.showinfo("Fim de jogo", f"Dados do vencedor:\n {self.vencedor}")
                    self.dados_jogada_atual["match_status"]= "finished"
                else:
                    self.atualizar_mensagem_jogador_da_vez()
                    self.dados_jogada_atual["match_status"]= "next"

                self.dog_server_interface.send_move(self.dados_jogada_atual)
            else:
                messagebox.showinfo("Jogada inválida", "Você precisa selecionar uma casa para jogar!")

        elif self.jogador_da_vez == JogadorDaVez.REMOTO:
            messagebox.showinfo("Jogada inválida", "Ainda não é a sua vez de jogar!")
            return

    # ----- Funções DOG ----
    def receive_start(self, start_status):
        messagebox.showinfo("iniciar jogo", "Você recebeu uma solicitação de inicio de jogo!' !")
        message = start_status.get_message()
        messagebox.showinfo(message=message)
        jogador_2 = start_status.get_players()[1][0]

        self.placar.update_player_names(jogador_2, 2)
        self.jogo.update_nome_jogador(jogador_2, 2)
        self.set_estado_jogo(EstadoJogo.PARTIDA_EM_ANDAMENTO)
        self.set_jogador_da_vez(JogadorDaVez.REMOTO)
        self.atualizar_mensagem_jogador_da_vez()

    def receive_move(self, a_move: dict):
        messagebox.showinfo("receber jogada", "Você recebeu uma jogada!' !")
        digito = a_move["digito"]
        linha = a_move["linha"]
        coluna = a_move["coluna"]

        self.inserir_digito_recebido(digito, linha, coluna)
        consequencias_jogada = self.jogo.receber_jogada(digito, linha, coluna)

        casas_modificadas = consequencias_jogada["casas_modificadas"]
        self.atualizar_tabuleiro(casas_modificadas)

        self.placar.update_player_score(1, consequencias_jogada["pontuacao_nova"])

        estado_jogo = self.jogo.get_estado_jogo()
        self.set_estado_jogo(estado_jogo)
        if self.estado_jogo == EstadoJogo.PARTIDA_FINALIZADA:

            self.vencedor = self.jogo.get_vecedor()
            messagebox.showinfo("Fim de jogo", f"Dados do vencedor:\n {self.vencedor}")
        else:
            self.atualizar_mensagem_jogador_da_vez()
            self.set_jogador_da_vez(JogadorDaVez.LOCAL)

            self.atualizar_mensagem_jogador_da_vez()

    def receive_withdrawal_notification(self):
        messagebox.showinfo("receber notificação de desistência", "O outro jogador desistiu!' !")
        self.set_estado_jogo(EstadoJogo.PARTIDA_ABANDONADA)
        self.vencedor = JogadorDaVez.LOCAL
        messagebox.showinfo("Fim de jogo", f"O jogador {self.vencedor.value} venceu!")



#PlayerInterface()

