import customtkinter as ctk
from PIL import Image
import variaveis as var
from janelas import *

class JogoDaVida(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('1350x750')
        self.title('Jogo da Vida')
        self.resizable(False,False)

        #questão atual --> no começo do jogo
        self.pergunta_atual_var = ctk.StringVar(value="1")          #colocar em variaveis??
        self.dados_questao_var = var.dados['perguntas'][self.pergunta_atual_var.get()]

        #Display do texto da questão
        self.pergunta_label = Label(self,bg='black',font=('consolas',25),text=self.dados_questao_var['texto'])

        #Criação da imagem do personagem
        imagem_personagem = ctk.CTkImage(Image.open(var.caminho_person_img),size=(200,300))
        imagem_label = ctk.CTkLabel(self,image=imagem_personagem,text='')
        imagem_label.pack(pady=60)

        #Frame dos butões de pergunta / Utiliza metódo de layout diferente (grid)
        self.botao_frame = BotaoFrame(self,larg=1000,alt=300)
        self.criar_botoes()

    def criar_botoes(self):
        #Criar lista com os botões de reposta para facilitar o acesso futuro
        self.botao_lista = []
        for col, (k, v) in enumerate(self.dados_questao_var['respostas'].items()):  #Fornece index(col), texto do botão(k), atributos e prox_q (v- formato: dicionario)
            btn = Botao(self.botao_frame, fg='green', font=('consolas', 20), text=k, func=self.passar_valores, col=col, valor=v)
            self.botao_lista.append(btn)

    def passar_valores(self,valor):
        print(valor)
        
        self.mudar_questao(valor)

    def mudar_questao(self,valor):
        prox_questao = valor['prox_q']
        self.pergunta_label.configure(text=var.dados['perguntas'][prox_questao]['texto'])
        for i, (k, v) in enumerate(var.dados['perguntas'][prox_questao]['respostas'].items()):
            self.botao_lista[i].configure(text=k,valor=v['prox_q'])
        
if __name__ == '__main__':
    jogo = JogoDaVida()
    jogo.mainloop()