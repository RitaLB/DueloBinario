from tkinter import *
import tkinter as tk

class Placar(tk.Frame):
    def __init__(self, master=None, jogador1_name="", jogador2_name="", jogador1_score=0, jogador2_score=0, jogador1_color="red", jogador2_color="blue"):
        super().__init__(master, bg = "white")
        self.master = master
        self.jogador1_name = jogador1_name
        self.jogador2_name = jogador2_name
        self.jogador1_score = jogador1_score
        self.jogador2_score = jogador2_score
        self.jogador1_color = jogador1_color
        self.jogador2_color = jogador2_color
        self.create_widgets()
        self.pack()


    def create_widgets(self):
        # Título
        self.titulo = tk.Label(self, text="Placar", bg = "white")
        self.titulo.grid(row=0, column=0, columnspan=3)

        # Primeira coluna
        self.jogador1_label = tk.Label(self, text=self.jogador1_name,  bg = "white")
        self.jogador1_label.grid(row=1, column=1)
        self.jogador1_image = self.create_color_image(self.jogador1_color)
        self.jogador1_image_label = tk.Label(self, image=self.jogador1_image)
        self.jogador1_image_label.grid(row=1, column=0)

        self.jogador2_label = tk.Label(self, text=self.jogador2_name,  bg = "white")
        self.jogador2_label.grid(row=2, column=1)
        self.jogador2_image = self.create_color_image(self.jogador2_color)
        self.jogador2_image_label = tk.Label(self, image=self.jogador2_image)
        self.jogador2_image_label.grid(row=2, column=0)

        # Segunda coluna
        self.jogador1_score_label = tk.Label(self, text=str(self.jogador1_score),  bg = "white")
        self.jogador1_score_label.grid(row=1, column=2)

        self.jogador2_score_label = tk.Label(self, text=str(self.jogador2_score),  bg = "white")
        self.jogador2_score_label.grid(row=2, column=2)




    def create_color_image(self, color):
        img = tk.PhotoImage(width=30, height=30)
        img.put(color, to=(0, 0, 49, 49))
        return img

    def update_player_names(self, player_name, num_player):
        if num_player == 1:
            self.jogador1_name = player_name
            self.jogador1_label.config(text=self.jogador1_name)
        else:
            self.jogador2_name = player_name
            self.jogador2_label.config(text=self.jogador2_name)

    def update_player_score(self,jogador: int, score: int):
        if jogador == 0:
            self.jogador1_score = score
            self.jogador1_score_label.config(text=str(self.jogador1_score))
        elif jogador == 1:
            self.jogador2_score = score
            self.jogador2_score_label.config(text=str(self.jogador2_score))
        else:
            self.update_player_names("Jogador 2", 2)
            print("Player inválido!")
