import tkinter as tk
from tkinter import ttk
import numpy as np

def gauss_elimination(a, b):
    n = len(b)
    steps = []

    # Fase de eliminação
    for k in range(n):
        steps.append(f"Eliminação na coluna {k+1}:")
        for i in range(k + 1, n):
            if a[k][k] == 0:
                steps.append("Erro: pivô zero encontrado. Trocar linhas ou utilizar pivoteamento.")
                return [], []
            factor = a[i][k] / a[k][k]
            steps.append(f"Multiplicador de fila para eliminar x{k+1} da equação {i+1}: m{i+1}{k+1} = {factor:.6f}")
            for j in range(k, n):
                a[i][j] -= factor * a[k][j]
            b[i] -= factor * b[k]
            steps.append(f"Nova linha {i+1}: {a[i]}, {b[i]:.6f}")

    steps.append("Matriz após a eliminação: ")
    steps.append(np.array_str(a))
    steps.append("Vetor b após a eliminação: ")
    steps.append(np.array_str(b))

    # Fase de substituição regressiva
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        sum_ax = sum(a[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (b[i] - sum_ax) / a[i][i]
        steps.append(f"Solução de x{i+1}: (b{i+1} - soma_ax) / a[{i+1},{i+1}] = ({b[i]:.6f} - {sum_ax:.6f}) / {a[i][i]:.6f} = {x[i]:.6f}")

    return x, steps

def solve_system():
    n = int(entry_n.get())
    a = []
    for i in range(n):
        row = [float(entries[i][j].get()) for j in range(n)]
        a.append(row)
    b = [float(entry_b[i].get()) for i in range(n)]
    a = np.array(a)
    b = np.array(b)

    solution, steps = gauss_elimination(a, b)
    result = ", ".join([f"x{i+1} = {round(solution[i], 6)}" for i in range(len(solution))])

    solution_entry.config(state=tk.NORMAL)
    solution_entry.delete(0, tk.END)
    solution_entry.insert(0, result)
    solution_entry.config(state=tk.DISABLED)

    steps_text.config(state=tk.NORMAL)
    steps_text.delete(1.0, tk.END)
    for step in steps:
        steps_text.insert(tk.END, step + "\n")
    steps_text.config(state=tk.DISABLED)

def create_matrix_entries():
    n = int(entry_n.get())
    for widget in frame_matrix.winfo_children():
        widget.destroy()
    global entries, entry_b
    entries = []
    entry_b = []

    for i in range(n):
        row_entries = []
        for j in range(n):
            entry = tk.Entry(frame_matrix, width=5)
            entry.grid(row=i+1, column=j, padx=5, pady=5)
            row_entries.append(entry)
        entries.append(row_entries)

        entry_b_single = tk.Entry(frame_matrix, width=5)
        entry_b_single.grid(row=i+1, column=n+1, padx=5, pady=5)
        entry_b.append(entry_b_single)

    tk.Label(frame_matrix, text="Coeficientes (A)").grid(row=0, column=0, columnspan=n)
    tk.Label(frame_matrix, text="Termos Independentes (B)").grid(row=0, column=n+1)

root = tk.Tk()
root.title("Eliminação de Gauss - Interface Simplificada")

# Interface simplificada
tk.Label(root, text="Tamanho da matriz").grid(row=0, column=0, padx=10, pady=10)
entry_n = tk.Entry(root, width=5)
entry_n.grid(row=0, column=1, padx=10, pady=10)

tk.Button(root, text="Gerar sistema", command=create_matrix_entries).grid(row=0, column=2, padx=10, pady=10)
tk.Button(root, text="Resolver Sistema", command=solve_system).grid(row=1, column=0, columnspan=3, pady=10)

frame_matrix = tk.Frame(root)
frame_matrix.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

solution_entry = tk.Entry(root, font=("Arial", 14), width=50, state=tk.DISABLED)
solution_entry.grid(row=3, column=0, columnspan=3, pady=10)

steps_text = tk.Text(root, height=10, width=70, state=tk.DISABLED)
steps_text.grid(row=4, column=0, columnspan=3, pady=10)

root.mainloop()
