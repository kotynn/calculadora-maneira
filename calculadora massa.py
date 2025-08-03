import math
import time

#operações
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return 'Erro: Divisão por zero'
    return a / b

def raiz_quadrada(n):
    if n < 0:
        return 'Erro: Raiz de número negativo'
    return round(math.sqrt(n), 2)

def porcentagem(numero, porc):
    return round(numero * porc / 100, 2)

def potencia(base, expoente):
    return round(math.pow(base, expoente), 2)

def seno(ang):
    return round(math.sin(math.radians(ang)), 4)

def cosseno(ang):
    return round(math.cos(math.radians(ang)), 4)

def tangente(ang):
    return round(math.tan(math.radians(ang)), 4)

def hipotenusa(co, ca):
    return round(math.hypot(co, ca), 2)

# Loop 
while True:
    metodo = input('''\nEscolha a operação: 
        [1] Soma (+)
        [2] Subtração (-) 
        [3] Multiplicação (x)
        [4] Divisão (÷)
        [5] Raiz quadrada (√)
        [6] Porcentagem (%)
        [7] Potência (^)
        [8] Seno (sen(x))
        [9] Cosseno (cos(x))
        [10] Tangente (tg(x))
        [11] Hipotenusa (C)
        [0] Sair
        Escolha uma das opções acima: ''')

    if metodo == '0':
        print('Encerrando a calculadora.')
        break

    try:
        match metodo:   
            case '1' | '2' | '3' | '4':
                n1 = float(input('Digite o primeiro número: '))
                n2 = float(input('Digite o segundo número: '))
                match metodo:
                    case '1':
                        print(f'A soma de {n1} + {n2} é {soma(n1, n2)}')
                    case '2':
                        print(f'A subtração de {n1} - {n2} é {subtracao(n1, n2)}')
                    case '3':
                        print(f'A multiplicação de {n1} * {n2} é {multiplicacao(n1, n2)}')
                    case '4':
                        print(f'A divisão de {n1} ÷ {n2} é {divisao(n1, n2)}')

            case '5':
                numero = float(input('Digite um número: '))
                print(f'A raiz quadrada de {numero} é {raiz_quadrada(numero)}')

            case '6':
                numero = float(input('Digite o número base: '))
                porc = float(input('Digite a porcentagem (%): '))
                print(f'{porc}% de {numero} é {porcentagem(numero, porc)}')

            case '7':
                base = float(input('Digite a base: '))
                expoente = float(input('Digite o expoente: '))
                print(f'{base} elevado a {expoente} = {potencia(base, expoente)}')

            case '8':
                ang = float(input('Digite o ângulo: '))
                print(f'O seno de {ang}° é {seno(ang)}')

            case '9':
                ang = float(input('Digite o ângulo: '))
                print(f'O cosseno de {ang}° é {cosseno(ang)}')

            case '10':
                ang = float(input('Digite o ângulo: '))
                print(f'A tangente de {ang}° é {tangente(ang)}')

            case '11':
                co = float(input('Digite o valor do cateto oposto: '))
                ca = float(input('Digite o valor do cateto adjacente: '))
                print(f'O valor da hipotenusa é {hipotenusa(co, ca)}')

            case _:
                print('Opção inválida. Tente novamente.')

    except ValueError:
        print('Erro, pare de ser burro e digite apenas números válidos.')

    except Exception as erro:
        print(f'Ocorreu um erro inesperado :( : {erro}')

    
    print('Aguarde...')
    time.sleep(3)
