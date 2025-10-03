def calculdora_simples():
    try:
        x = float(input('Numero 1 : '))
        y = float(input('Numero 2 : '))
        op = input('Operação (+,-,*,/): ')
        if op not in '+-*/':
            raise ValueError('Operação inválida')
        result = eval(f'{x}{op}{y}')
        print(f'Resultado : {result}')
    except Exception:
        print('Operação falha. Coloque valores adequados.')


def classificacao_nota():
    try:
        notas = [float(input(f'Nota {i+1} : ')) for i in range(3)]
        if any(n < 0 or n > 10 for n in notas):
            print('Nota invalida')
            return
        media = sum(notas) / 3
        if media >= 7:
            print(f'Media = {media}, status = aprovado')
        elif 5 <= media < 7:
            print(f'Media = {media}, status = recuperação')
        else:
            print(f'Media = {media}, status = reprovado')
    except ValueError:
        print('Valor inválido.')


def grandezas_eletricas():
    print('''***********************************************************
                CÁLCULO DE GRANDEZAS ELÉTRICAS
***********************************************************
1. Tensão (em Volt)
2. Resistência (em Ohm)
3. Corrente (em Ampére)
********************************************************''')
    grandeza = input('Qual grandeza deseja calcular ? ')
    try:
        if grandeza == '1':
            r = float(input('resistencia : '))
            c = float(input('corrente : '))
            print(f'tensao = {r*c} volts')
        elif grandeza == '2':
            t = float(input('tensao : '))
            c = float(input('corrente : '))
            print(f'resistencia = {t/c} ohms')
        elif grandeza == '3':
            t = float(input('tensao : '))
            r = float(input('resistencia : '))
            print(f'corrente = {t/r} amperes')
        else:
            print('Opção inválida.')
    except ValueError:
        print('Valor inválido.')

    
def existe_triangulo():
    try:
        x1, y1 = float(input('x1 : ')), float(input('y1 : '))
        x2, y2 = float(input('x2 : ')), float(input('y2 : '))
        x3, y3 = float(input('x3 : ')), float(input('y3 : '))
        p1 = ((x1-x2)**2 + (y1-y2)**2)**0.5
        p2 = ((x1-x3)**2 + (y1-y3)**2)**0.5
        p3 = ((x3-x2)**2 + (y3-y2)**2)**0.5
        lados = [p1, p2, p3]
        if all(l > 0 for l in lados) and (
            (p1+p2>p3 and abs(p1-p2)<p3) or
            (p1+p3>p2 and abs(p1-p3)<p2) or
            (p3+p2>p1 and abs(p3-p2)<p1)):
            if p1 == p2 == p3:
                status = 'equilatero'
            elif len(set(lados)) == 3:
                status = 'escaleno'
            else:
                status = 'isoceles'
            print(f'lado 1 = {round(p1,2)}, lado 2 = {round(p2,2)}, lado 3 = {round(p3,2)}, status = {status}.')
        else:
            print('Nenhum triângulo formado com os pontos informados.')
    except ValueError:
        print('Valor inválido.')


def estatura_decres():
    try:
        estatura = [float(input(f'Altura {i+1} : ')) for i in range(3)]
        print(sorted(estatura, reverse=True))
    except ValueError:
        print('Valor inválido.')

def logistica_entregras():
    try:
        distancia = float(input('Digite a distância (km): '))
        veiculo = input('Digite o veículo (1 - carro, 2 - moto ou 3 - bicicleta):')
        if distancia > 0 and veiculo in ('1', '2', '3'):
            if veiculo == '1':
                print(f'Valor total da corrida de carro: {10 + 5*distancia}')
            elif veiculo == '2':
                print(f'Valor total da corrida de moto: {10 + 3.5*distancia}')
            else:
                print(f'Valor total da corrida de bicicleta: {10 + 2*distancia}')
        else:
            print('Distancia ou veiculo invalido(s).')
    except ValueError:
        print('Valor inválido.')
