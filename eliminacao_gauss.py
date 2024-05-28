import tkinter as tk
from tkinter import ttk
import numpy as np

def gauss_elimination(a, b):
    n = len(b)
    elimination_steps = []
    for k in range(n):
        for i in range(k + 1, n):
            if a[i][k] == 0: continue
            factor = a[i][k] / a[k][k]
            elimination_steps.append(f"Linha {i+1} - ({round(factor, 6)}) * Linha {k+1}")
            for j in range(k, n):
                a[i][j] -= factor * a[k][j]
            b[i] -= factor * b[k]

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        sum_ax = 0
        for j in range(i + 1, n):
            sum_ax += a[i][j] * x[j]
        x[i] = (b[i] - sum_ax) / a[i][i]
    return x, elimination_steps

def solve_system():
    n = int(entry_n.get())
    a = []
    for i in range(n):
        row = [float(entries[i][j].get()) for j in range(n)]
        a.append(row)
    b = [float(entry_b[i].get()) for i in range(n)]
    a = np.array(a)
    b = np.array(b)

    solution, elimination_steps = gauss_elimination(a, b)
    result = ", ".join([f"x{i+1} = {round(solution[i], 6)}" for i in range(n)])

    solution_entry.config(state=tk.NORMAL)
    solution_entry.delete(0, tk.END)
    solution_entry.insert(0, result)
    solution_entry.config(state=tk.DISABLED)

    steps_text.config(state=tk.NORMAL)
    steps_text.delete("1.0", tk.END)
    steps_text.insert(tk.END, "\n".join(elimination_steps))
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

tk.Label(root, text="Tamanho da matriz").grid(row=0, column=0, padx=10, pady=10)
entry_n = tk.Entry(root, width=5)
entry_n.grid(row=0, column=1, padx=10, pady=10)

tk.Button(root, text="Gerar sistema", command=create_matrix_entries).grid(row=0, column=2, padx=10, pady=10)
tk.Button(root, text="Resolver Sistema", command=solve_system).grid(row=1, column=0, columnspan=3, pady=10)

frame_matrix = tk.Frame(root)
frame_matrix.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

solution_entry = tk.Entry(root, font=("Arial", 14), width=50, state=tk.DISABLED)
solution_entry.grid(row=3, column=0, columnspan=3, pady=10)

steps_text = tk.Text(root, font=("Arial", 12), width=50, height=10, state=tk.DISABLED)
steps_text.grid(row=4, column=0, columnspan=3, pady=10)

root.mainloop()
