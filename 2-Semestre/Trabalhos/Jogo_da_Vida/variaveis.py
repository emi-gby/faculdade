import json

WIN_ALTURA = 750
WIN_LARGURA = 1350

caminho_botao_img = '2-Semestre/Trabalhos/Jogo_da_Vida/imagens/Button_1.png'

caminho_person_img = '2-Semestre/Trabalhos/Jogo_da_Vida/imagens/professora.png'

caminho_bg_img = '2-Semestre/Trabalhos/Jogo_da_Vida/imagens/Background_escola2.jpg'

caminho_balao_perg = '2-Semestre/Trabalhos/Jogo_da_Vida/imagens/Balao_pergunta.png'

with open('2-Semestre/Trabalhos/Jogo_da_Vida/dados/perg_resp.json') as f:   
    dados = json.load(f) 