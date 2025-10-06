def par_impar(n):
    print('par' if n % 2 == 0 else 'impar')

def resto_divisao(x,y) : print(x % y)

def pos_neg_zero(n):
    print('positivo' if n > 0 else 'negativo' if n < 0 else 'zero')

def multiplo(x,y):
    print('multiplo' if x % y == 0 else 'não é multiplo')

def maior_de_dois(x,y):
    if x == y:
        print(f'{x} é igual a {y}')
    else:
        maior = max(x, y)
        menor = min(x, y)
        print(f'{maior} é maior que {menor}')

def dobro_triplo(n):
    print(f'dobro de {n} = {n * 2}')
    print(f'triplo de {n} = {n * 3}')

def ante_sucessor(n):
    print(f'antecessor = {n-1}')
    print(f'sucessor = {n+1}')

def area_triangulo():
    try:
        h = float(input('Altura : '))
        l = float(input('Largura : '))
        print(f'Area : {h * l / 2}')
    except ValueError:
        print('Valores inválidos.')

def convert_temp():
    try:
        celsius = float(input('Temperatura em celsius : '))
        print(f'Temperatura em fahrenheit : {((celsius*9)/5)+32}')
    except ValueError:
        print('Valor inválido.')

def media_simples():
    try:
        notas = [float(input(f'Nota {i + 1} : ')) for i in range(4)]
        print(f'Media : {sum(notas)/4}')
    except ValueError:
        print('Valor inválido.')
