import numpy as np

def newton_raphson(f, g, x0, E=0.0001, N=30):
    """
    Método de Newton-Raphson para encontrar raízes de funções.
    
    Parâmetros:
    f  - Função da qual queremos encontrar a raiz.
    g  - Derivada da função f.
    x0 - Estimativa inicial da raiz.
    E  - Tolerância para critério de parada (default: 0.0001).
    N  - Número máximo de iterações (default: 30).
    
    Retorna:
    Aproximação da raiz da função f.
    """
    for n in range(0, N):
        try:
            x_novo = x0 - f(x0) / g(x0)
        except ZeroDivisionError:
            print(f'Divisão por zero na iteração {n}. Derivada é zero em x = {x0}.')
            return None

        print(f'Iteração {n}: x = {x_novo:.15f}')
        
        if abs((x_novo - x0) / x0) < E:
            return x_novo
        
        x0 = x_novo
    
    print('Número máximo de iterações atingido.')
    return x_novo

def f1(x):
    return x**5 - 6

def g1(x):
    return 5 * x**4

def f2(x):
    return 2 * np.cos(x) - np.exp(x) / 2

def g2(x):
    return -2 * np.sin(x) - np.exp(x) / 2

# Função para selecionar a equação
def selecionar_equacao():
    print("Escolha a função para calcular a raiz:")
    print("1. x^5 - 6")
    print("2. 2 * cos(x) - exp(x) / 2")
    escolha = int(input("Digite o número da sua escolha (1 ou 2): "))
    if escolha == 1:
        return f1, g1, "x^5 - 6"
    elif escolha == 2:
        return f2, g2, "2 * cos(x) - exp(x) / 2"
    else:
        print("Escolha inválida. Tente novamente.")
        return selecionar_equacao()

# Capturar entradas do usuário
f, g, descricao = selecionar_equacao()
x0 = float(input("Digite o valor inicial (x0): "))
N = int(input("Digite o número máximo de iterações: "))
E = float(input("Digite o erro mínimo (tolerância): "))

print(f'Função: {descricao}')
print(f'Com estimativa inicial x0 = {x0}:')
raiz = newton_raphson(f, g, x0, E, N)
print(f'Raiz encontrada para {descricao}: x = {raiz:.15f}' if raiz else 'Raiz não encontrada.')
