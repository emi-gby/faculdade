def convert_tempo(n) : print(f'{n//60} horas e {n%60} minutos')

def media_ponderada():
    try:
        notas_pesos = [(float(input(f'Nota {i+1}: ')), float(input(f'Peso {i+1}: '))) for i in range(3)]
        nota_total = sum(n * p for n, p in notas_pesos)
        peso_total = sum(p for _, p in notas_pesos)
        print(f'Media ponderada : {nota_total/peso_total}')
    except ValueError:
        print('Valor inválido.')

    
def troca_variaveis(a,b):
    a = a + b
    b = a - b
    a = a - b
    print(f'A = {a}, B = {b}')

def raiz_bhaskara(a,b,c):
    delta = b**2 - 4 * a * c
    if delta > 0:
        raiz = delta ** 0.5
        print(f'Raiz 1 : {(-b+raiz)/(2*a)}, Raiz 2 : {(-b-raiz)/(2*a)}')
    elif delta == 0:
        print(f'Raiz : {-b/(2*a)}')
    else:
        print('Raiz imaginária')


def convert_units(m) : print(f'{m}m = {m*100}cm, {m*1000}mm, {m/1000}km')


def invert_num(n):
    u = n // 100
    d = (n % 100) // 10
    c = n % 10
    print(f'Novo numero : {c}{d}{u}')

def juros_simples():
    try:
        c = float(input('Capital : '))
        i = float(input('Juros : '))
        t = float(input('Tempo(meses) : '))
        print(f'Montante : {c + (c*i*t)}')
    except ValueError:
        print('Valor inválido.')
