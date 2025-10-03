from collections import Counter, defaultdict, namedtuple

def nota_maior7():
    dic_lista = [{'Caio':3,},{'Jonas':7},{'Raeia':8}]
    for d in dic_lista:
        for k, v in d.items():
            if v >= 7:
                print(k)

def contagem_palavra():
    frase = "a casa é amarela e a porta da casa é marrom"
    contagem_dic = {}
    for palavra in frase.split():
        contagem_dic[palavra] = contagem_dic.get(palavra, 0) + 1
    print(contagem_dic)


def amigos():
    amigos_trabalho = {"Ana", "Bruno", "Carlos"}
    amigos_faculdade = {"Ana", "Daniel", "Eva"}
    # Todos os amigos (união)
    print(f'União: {list(amigos_trabalho | amigos_faculdade)}')
    # Amigos de ambos os grupos (interseção)
    print(f'Interseção: {list(amigos_trabalho & amigos_faculdade)}')
    # Amigos apenas do trabalho (diferença)
    print(f'Diferença: {list(amigos_trabalho - amigos_faculdade)}')

def maior_menor(lista):
    if not lista:   #prevenção de erros
        print('Lista Vazia')  
        return
    numero_maior, numero_menor = lista[0], lista[0]
    for num in lista[:1]:
        if num > numero_maior:
            numero_maior = num
        elif num < numero_menor:
            numero_menor = num    
    print((numero_maior,numero_menor))

def cadastro_produtos():
    """
    Sistema de cadastro e consulta de produtos com tratamento de erros.
    """
    produtos_dic = {}
    while True:
        reposta_usuario = input('1.Adicionar novo produto\n 2.Consultar preço\n q.Sair \nEscolha uma opção : ').strip().lower()
        if reposta_usuario == '1':
            produto = input('Insira o nome do produto : ').strip().capitalize()
            preco_str = input('Insira o preço do produto : ').strip().replace(',','.')
            try:
                preco = float(preco_str)
                produtos_dic[produto] = preco
            except ValueError:
                print('Preço inválido. Por favor, insira um número válido.')
        elif reposta_usuario == '2':
            if not produtos_dic:
                print('Nenhum produto cadastrado ainda.')
                continue
            print('Produtos disponíveis:', ', '.join(produtos_dic.keys()))
            consulta_produto = input('Insira o nome de um produto : ').strip().capitalize()
            preco = produtos_dic.get(consulta_produto)
            if preco is not None:
                print(f'Preço - {consulta_produto}: R$ {preco:.2f}')
            else:
                print(f'"{consulta_produto}" não está na lista de produtos.')
        elif reposta_usuario == 'q':
            print('Saindo do sistema de cadastro de produtos.')
            break
        else:
            print(f'Opção "{reposta_usuario}" inválida. Tente novamente.')


def total_vendas():
    vendas = [('produtoA', 10), ('produtoB', 5),('produtoA', 3), ('produtoB', 13)]
    resultado_dic = defaultdict(int)
    for produto, quantidade in vendas:
        resultado_dic[produto] += quantidade
    print(dict(resultado_dic))


def tuplas_config():
    # Definindo a estrutura de configuração imutável
    Configuracao = namedtuple('Configuracao', ['host_banco_dados', 'porta', 'usuario'])

    # Criando a configuração
    config = Configuracao(host_banco_dados="localhost", porta=5432, usuario="admin")

    # Acessando o valor da porta
    print(config.porta)  # Saída: 5432

def adicionar_aresta(v1, v2):
    grafo = [{'a','b'},{'c','d'},{'d','e'}]
    if {v1,v2} not in grafo:
        grafo.append({v1,v2})
        print(grafo)
    else:
        print('Aresta já está no grafo.')
