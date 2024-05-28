import numpy as np
import tkinter as tk
from tkinter import ttk, messagebox

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
    iteracoes = []
    x_novo = x0  # Inicializar x_novo para evitar erros de variável não vinculada
    for n in range(0, N):
        try:
            x_novo = x0 - f(x0) / g(x0)
        except ZeroDivisionError:
            messagebox.showerror("Erro", f'Divisão por zero na iteração {n}. Derivada é zero em x = {x0}.')
            return None, iteracoes

        iteracoes.append(f'Iteração {n}: x = {x_novo:.15f}')

        if abs((x_novo - x0) / x0) < E:
            return x_novo, iteracoes

        x0 = x_novo

    messagebox.showinfo("Aviso", 'Número máximo de iterações atingido.')
    return x_novo, iteracoes

def f1(x):
    return x**5 - 6

def g1(x):
    return 5 * x**4

def f2(x):
    return 2 * np.cos(x) - np.exp(x) / 2

def g2(x):
    return -2 * np.sin(x) - np.exp(x) / 2

def calcular_raiz():
    try:
        x0 = float(entry_x0.get())
        N = int(entry_N.get())
        E = float(entry_E.get())

        escolha = equacao_var.get()
        if escolha == 1:
            f, g, descricao = f1, g1, "x^5 - 6"
        elif escolha == 2:
            f, g, descricao = f2, g2, "2 * cos(x) - exp(x) / 2"
        else:
            messagebox.showerror("Erro", "Seleção de equação inválida.")
            return

        raiz, iteracoes = newton_raphson(f, g, x0, E, N)
        resultado_texto = f'Função: {descricao}\n'
        resultado_texto += f'Raiz encontrada: x = {raiz:.15f}\n\n'
        resultado_texto += '\n'.join(iteracoes)

        text_resultado.delete(1.0, tk.END)
        text_resultado.insert(tk.END, resultado_texto)

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")

# Configurar interface gráfica
root = tk.Tk()
root.title("Método de Newton-Raphson")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky="nsew")

equacao_var = tk.IntVar(value=1)
ttk.Radiobutton(frame, text="x^5 - 6", variable=equacao_var, value=1).grid(row=0, column=0, sticky="w")
ttk.Radiobutton(frame, text="2 * cos(x) - exp(x) / 2", variable=equacao_var, value=2).grid(row=0, column=1, sticky="w")

ttk.Label(frame, text="Valor inicial (x0):").grid(row=1, column=0, sticky="w")
entry_x0 = ttk.Entry(frame)
entry_x0.grid(row=1, column=1, sticky="ew")

ttk.Label(frame, text="Número máximo de iterações:").grid(row=2, column=0, sticky="w")
entry_N = ttk.Entry(frame)
entry_N.grid(row=2, column=1, sticky="ew")

ttk.Label(frame, text="Erro mínimo (tolerância):").grid(row=3, column=0, sticky="w")
entry_E = ttk.Entry(frame)
entry_E.grid(row=3, column=1, sticky="ew")

ttk.Button(frame, text="Calcular Raiz", command=calcular_raiz).grid(row=4, column=0, columnspan=2)

text_resultado = tk.Text(frame, width=60, height=20)
text_resultado.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
