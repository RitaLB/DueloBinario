from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from dog.dog_interface import DogPlayerInterface
from dog.dog_actor import DogActor

class ActorPlayer(DogPlayerInterface):
	def __init__(self):
		self.main_window = Tk()
		self.main_window.title("Jogo da velha")
		self.main_window.iconbitmap("images/icon.ico")
		self.main_window.geometry("375x440")
		self.main_window.resizable(False, False)
		self.main_window["bg"]="gray"

		self.mainFrame = Frame(self.main_window, padx=32, pady=25, bg="gray")
		self.messageFrame = Frame(self.main_window, padx=4, pady=1, bg="gray")

		self.empty = PhotoImage(file="images/empty.gif")		#pyimage1
		self.white = PhotoImage(file="images/white.gif")		#pyimage2
		self.red = PhotoImage(file="images/red.gif")			#pyimage3

		self.boardView=[]
		for y in range(3):
			viewTier = []
			for x in range(3):
				aLabel = Label(self.mainFrame, bd=2, relief="solid", image=self.empty)
				aLabel.grid(row=x , column=y)
				aLabel.bind("<Button-1>", lambda event, line=y+1, column=x+1: self.click(event, line, column))
				viewTier.append(aLabel)
			self.boardView.append(viewTier)

		self.labelMessage = Label(self.messageFrame, bg="gray", text='Clique em qualquer posição para iniciar', font="arial 14")
		self.labelMessage.grid(row=0, column=0, columnspan=3)
		self.mainFrame.grid(row=0 , column=0)
		self.messageFrame.grid(row=1 , column=0) 

		self.whiteTurn=True

		# Criação de um menu para o programa
		# Criar a barra de menu (menubar) e adicionar à janela:
		self.menubar = Menu(self.main_window)
		self.menubar.option_add('*tearOff', FALSE)
		self.main_window['menu'] = self.menubar
		# Adicionar menu(s) à barra de menu:
		self.menu_file = Menu(self.menubar)
		self.menubar.add_cascade(menu=self.menu_file, label='File')
		# Adicionar itens de menu a cada menu adicionado à barra de menu:
		self.menu_file.add_command(label='Iniciar jogo', command=self.start_match)
		self.menu_file.add_command(label='restaurar estado inicial', command=self.start_game)

		player_name = simpledialog.askstring(title="Player identification", prompt="Qual o seu nome?")
		self.dog_server_interface = DogActor()
		message = self.dog_server_interface.initialize(player_name, self)
		messagebox.showinfo(message=message)

		self.main_window.mainloop()

	def click(self, event, linha, coluna):
		label=self.boardView[linha-1][coluna-1]
		if label['imag']=='pyimage1':
			if self.whiteTurn:
				label['imag']=self.white
				self.whiteTurn=False
			else:
				label['imag']=self.red
				self.whiteTurn=True

	def start_match(self):
		start_status = self.dog_server_interface.start_match(2)
		message = start_status.get_message()
		messagebox.showinfo(message=message)

	def start_game(self):
		print('start_game')

	def receive_start(self, start_status):
		message = start_status.get_message()
		messagebox.showinfo(message=message)

ActorPlayer()
