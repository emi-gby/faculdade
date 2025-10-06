def contagem_simples():
    for i in range(1, 21):
        print(i)

def tabuada():
    try:
        numero = int(input('Insira um numero inteiro : '))
        for i in range(1, 11):
            print(f'{numero}*{i} = {numero*i}')
    except ValueError:
        print('Por favor, insira um número inteiro válido.')

def soma_numeros():
    """Calcula e printa a soma de todos os números de 1 até n, onde n é indicado pelo usuário."""
    try:
        n = int(input('Insira um numero : '))
        if n < 1:
            print('Por favor, insira um número maior que zero.')
            return
        print(f'Soma de todos os numeros = {sum(range(1, n+1))}')
    except ValueError:
        print('Por favor, insira um número inteiro válido.')

def contagem_regressiva():
    try:
        n = int(input('Insira um numero : '))
        for i in range(n, -1, -1):
            print(i)
    except ValueError:
        print('Valor inválido.')

def fatorial():
    """Calcula e printa o fatorial de n (n!), onde n é providenciado pelo usuário."""
    try:
        n = int(input('Insira um numero : '))
        if n < 0:
            print('Por favor, insira um número não-negativo.')
            return
        fat = 1
        for i in range(2, n+1):
            fat *= i
        print(f'Fatorial = {fat}')
    except ValueError:
        print('Por favor, insira um número inteiro válido.')

def quant_digitos():
    try:
        n = int(input('Insira um numero inteiro : '))
        print(f'Esse numero tem {len(str(abs(n)))} digitos')
    except ValueError:
        print('Valor inválido.')

def num_primo():
    try:
        n = int(input('insira um numero : '))
        if n < 2:
            print('Não é primo')
            return
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                print('Não é primo')
                return
        print('É primo')
    except ValueError:
        print('Valor inválido.')

def fibonacci(): 
    try:
        n = int(input('Insira um numero : '))
        fib = [1, 1][:n]
        if n <= 0:
            print([])
            return
        for _ in range(2, n):
            fib.append(fib[-1] + fib[-2])
        print(fib)
    except ValueError:
        print('Valor inválido.')

def num_perfeito():
    try:
        n = int(input('Insira um numero : '))
        divisores = [i for i in range(1, n) if n % i == 0]
        if sum(divisores) == n:
            print('numero perfeito')
        else:
            print('numero não é perfeito')
    except ValueError:
        print('Valor inválido.')

    
def media_n_numeros():
    try:
        n = int(input('Insira um Numero N : '))
        if n < 1:
            print('Por favor, insira um número maior que zero.')
            return
        numeros = []
        for i in range(n):
            while True:
                try:
                    num = float(input(f'Insira numero {i+1} : '))
                    numeros.append(num)
                    break
                except ValueError:
                    print('Por favor, insira um número válido.')
        media = sum(numeros)/n
        print(f'Media aritmética = {media:.2f}')
    except ValueError:
        print('Por favor, insira um número inteiro válido.')

def progressao_aritmetica():
    try:
        primeiro_termo = float(input('Insira o primeiro termo : '))
        quant_termos = int(input('Insira a quantidade de termos : '))
        razao = float(input('Insira a razao : '))
        progressao = [primeiro_termo + i * razao for i in range(quant_termos)]
        print(progressao)
    except ValueError:
        print('Valor inválido.')

def sistema_natacao():
    try:
        sistema_dict = {float(input(f'Insira o tempo {i+1} : ')): input(f'Insira o nome {i+1} : ') for i in range(7)}
        tempo_list = list(sistema_dict.keys())
        print(f'a.Jogador c/ melhor tempo : {sistema_dict[min(tempo_list)]}')
        print(f'b.Jogador c/ pior tempo : {sistema_dict[max(tempo_list)]}')
        print(f'c.Tempo médio : {round(sum(tempo_list)/ 7,2)}')
        quant_jogadores_1215 = sum(12 < tempo < 15 for tempo in tempo_list)
        print(f'd.Quantidade de atletas com o tempo entre 12s e 15s : {quant_jogadores_1215}')
    except ValueError:
        print('Valor inválido.')

def pesquisa_opnioes():
    try:
        n = int(input('Insira a quantidade de clientes : '))
        idade_nota = [(int(input(f'Insira idade do cliente {i+1} : ')), int(input(f'Insira a nota de satisfação do cliente {i+1} : '))) for i in range(n)]
        idade_lista = [idade for idade, _ in idade_nota]
        nota_lista = [nota for _, nota in idade_nota]
        clientes_satisfeitos = [(idade, nota) for idade, nota in idade_nota if nota >= 4]
        cliente_insatisfeito = sum(nota <= 2 for nota in nota_lista)
        if clientes_satisfeitos:
            media_idade_satisfeitos = sum(idade for idade, _ in clientes_satisfeitos) / len(clientes_satisfeitos)
        else:
            media_idade_satisfeitos = 0
        print(f'média de idade dos clientes satisfeitos = {media_idade_satisfeitos}')
        print(f'porcentagem de clientes insatisfeitos = {cliente_insatisfeito/n*100}%')
        print(f'nota média geral = {sum(nota_lista)/n}')
    except ValueError:
        print('Valor inválido.')

pesquisa_opnioes()
