import numpy as np
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

def newton_raphson(f, g, x0, E=0.0001, N=30, output_box=None):
    """
    Método de Newton-Raphson para encontrar raízes de funções.

    Parâmetros:
    f  - Função da qual queremos encontrar a raiz.
    g  - Derivada da função f.
    x0 - Estimativa inicial da raiz.
    E  - Tolerância para critério de parada (default: 0.0001).
    N  - Número máximo de iterações (default: 30).
    output_box - Caixa de texto para saída (opcional).

    Retorna:
    Aproximação da raiz da função f.
    """
    for n in range(0, N):
        try:
            x_novo = x0 - f(x0) / g(x0)
        except ZeroDivisionError:
            output_box.insert(tk.END, f'Divisão por zero na iteração {n}. Derivada é zero em x = {x0}.\n')
            return None

        output_box.insert(tk.END, f'Iteração {n}: x = {x_novo:.15f}\n')

        if abs((x_novo - x0) / x0) < E:
            return x_novo

        x0 = x_novo

    output_box.insert(tk.END, 'Número máximo de iterações atingido.\n')
    return x_novo

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
        N = int(entry_iter.get()) if entry_iter.get() else 30
        E = float(entry_tol.get()) if entry_tol.get() else 0.0001
    except ValueError:
        messagebox.showerror("Entrada Inválida", "Por favor, insira valores numéricos válidos.")
        return

    escolha = combo_funcao.get()
    if escolha == "x^5 - 6":
        f, g, descricao = f1, g1, "x^5 - 6"
    elif escolha == "2 * cos(x) - exp(x) / 2":
        f, g, descricao = f2, g2, "2 * cos(x) - exp(x) / 2"
    else:
        messagebox.showerror("Escolha Inválida", "Por favor, selecione uma função válida.")
        return

    output_box.delete('1.0', tk.END)
    output_box.insert(tk.END, f'Função: {descricao}\n')
    output_box.insert(tk.END, f'Com estimativa inicial x0 = {x0}:\n')
    raiz = newton_raphson(f, g, x0, E, N, output_box)
    if raiz is not None:
        output_box.insert(tk.END, f'Raiz encontrada para {descricao}: x = {raiz:.15f}\n')
    else:
        output_box.insert(tk.END, 'Raiz não encontrada.\n')

# Interface gráfica
root = tk.Tk()
root.title("Método de Newton-Raphson")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame, text="Selecione a função:").grid(column=1, row=1, sticky=tk.W)
combo_funcao = ttk.Combobox(frame, values=["x^5 - 6", "2 * cos(x) - exp(x) / 2"])
combo_funcao.grid(column=2, row=1, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Valor inicial (x0):").grid(column=1, row=2, sticky=tk.W)
entry_x0 = ttk.Entry(frame)
entry_x0.grid(column=2, row=2, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Número máximo de iterações (padrão: 30):").grid(column=1, row=3, sticky=tk.W)
entry_iter = ttk.Entry(frame)
entry_iter.grid(column=2, row=3, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Erro mínimo (tolerância) (padrão: 0.0001):").grid(column=1, row=4, sticky=tk.W)
entry_tol = ttk.Entry(frame)
entry_tol.grid(column=2, row=4, sticky=(tk.W, tk.E))

ttk.Button(frame, text="Calcular", command=calcular_raiz).grid(column=2, row=5, sticky=tk.W)

output_box = scrolledtext.ScrolledText(frame, width=50, height=15, wrap=tk.WORD)
output_box.grid(column=1, row=6, columnspan=2, sticky=(tk.W, tk.E))

for child in frame.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.mainloop()
