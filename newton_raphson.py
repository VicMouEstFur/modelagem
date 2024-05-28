import numpy as np


def newton_raphson(f, g, x0, E=0.0001, N=30):
  for n in range(0, N):
    x_novo = x0 - f(x0) / g(x0)
    print(f'Iteração {n}: x = {x_novo}')
    if abs((x_novo - x0)/x0)< E:
      return x_novo
    x0 = x_novo


def f1(x):
  return x**5 - 6


def g1(x):
  return 5 * x**4


print('x**5 - 6')
x1 = 3
print(f'x**5 - 6 com x0 = {x1}:')
raiz_f1 = newton_raphson(f1, g1, x1)
print(f'Raiz encontrada para f1: x = {raiz_f1}')


def f2(x):
  return 2 * np.cos(x) - np.exp(x) / 2


def g2(x):
  return -2 * np.sin(x) - np.exp(x) / 2


print(' ')
x2 = -2
print(f'2cosx-e^x/2 com x0 = {x2}:')
raiz_f2 = newton_raphson(f2, g2, x2)
print(f'Raiz encontrada para f2: x = {raiz_f2}')
