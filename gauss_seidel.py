import tkinter as tk
from tkinter import ttk
import numpy as np

class GaussSeidelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Método de Gauss-Seidel")

        self.create_widgets()

    def create_widgets(self):
        # Tamanho da matriz
        ttk.Label(self.root, text="Tamanho da Matriz:").grid(row=0, column=0, padx=10, pady=10)
        self.matrix_size_entry = ttk.Entry(self.root)
        self.matrix_size_entry.grid(row=0, column=1, padx=10, pady=10)

        # Botão para configurar entradas da matriz
        self.setup_matrix_button = ttk.Button(self.root, text="Configurar Matriz", command=self.setup_matrix_entries)
        self.setup_matrix_button.grid(row=0, column=2, padx=10, pady=10)

        # Frame para entradas de matriz e constantes
        self.matrix_frame = ttk.Frame(self.root)
        self.matrix_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Opções para critério de parada
        ttk.Label(self.root, text="Número máximo de iterações:").grid(row=2, column=0, padx=10, pady=10)
        self.iteration_entry = ttk.Entry(self.root)
        self.iteration_entry.grid(row=2, column=1, padx=10, pady=10)

        ttk.Label(self.root, text="Erro máximo:").grid(row=3, column=0, padx=10, pady=10)
        self.error_entry = ttk.Entry(self.root)
        self.error_entry.grid(row=3, column=1, padx=10, pady=10)

        # Botão de resolver
        self.solve_button = ttk.Button(self.root, text="Resolver", command=self.solve)
        self.solve_button.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

        # Tabela de iterações
        self.iteration_table = ttk.Treeview(self.root, columns=("Iteração", "x1", "x2", "x3", "Erro"), show='headings')
        self.iteration_table.heading("Iteração", text="Iteração")
        self.iteration_table.heading("x1", text="x1")
        self.iteration_table.heading("x2", text="x2")
        self.iteration_table.heading("x3", text="x3")
        self.iteration_table.heading("Erro", text="Erro")
        self.iteration_table.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

    def setup_matrix_entries(self):
        # Limpar entradas anteriores, se houver
        for widget in self.matrix_frame.winfo_children():
            widget.destroy()

        try:
            self.L = int(self.matrix_size_entry.get())
        except ValueError:
            self.insert_output("Por favor, insira um inteiro válido para o tamanho da matriz.")
            return

        self.matrix_entries = []
        self.constant_entries = []

        # Criar entradas para a matriz
        ttk.Label(self.matrix_frame, text="Matriz A:").grid(row=0, column=0, columnspan=self.L, padx=5, pady=5)
        for i in range(self.L):
            row_entries = []
            for j in range(self.L):
                entry = ttk.Entry(self.matrix_frame, width=5)
                entry.grid(row=i+1, column=j, padx=5, pady=5)
                row_entries.append(entry)
            self.matrix_entries.append(row_entries)

        # Criar entradas para as constantes
        ttk.Label(self.matrix_frame, text="Matriz b:").grid(row=0, column=self.L, padx=5, pady=5)
        for i in range(self.L):
            entry = ttk.Entry(self.matrix_frame, width=5)
            entry.grid(row=i+1, column=self.L, padx=5, pady=5)
            self.constant_entries.append(entry)

        # Atualizar colunas da tabela de iterações
        self.update_table_columns()

    def update_table_columns(self):
        # Atualizar as colunas da tabela com base no tamanho da matriz
        columns = ["Iteração"] + [f"x{i+1}" for i in range(self.L)] + ["Erro"]
        self.iteration_table["columns"] = columns
        for col in columns:
            self.iteration_table.heading(col, text=col)
        self.iteration_table.column("#0", width=0, stretch=tk.NO)
        for col in columns:
            self.iteration_table.column(col, anchor=tk.CENTER)

    def insert_output(self, message):
        self.iteration_table.insert("", "end", values=(message, "", "", "", ""))

    def clear_output(self):
        for item in self.iteration_table.get_children():
            self.iteration_table.delete(item)

    def get_matrix(self):
        try:
            f = np.array([[float(entry.get()) for entry in row] for row in self.matrix_entries])
            f1 = np.array([[float(entry.get())] for entry in self.constant_entries])
        except ValueError:
            self.insert_output("Por favor, insira números válidos para os elementos da matriz e constantes.")
            return None, None
        return f, f1

    def solve(self):
        self.clear_output()
        f, f1 = self.get_matrix()
        if f is None or f1 is None:
            return

        try:
            maxitera = int(self.iteration_entry.get())
            err = float(self.error_entry.get())
        except ValueError:
            self.insert_output("Por favor, insira valores válidos para iterações e erro.")
            return

        self.gauss_seidel(f, f1, maxitera=maxitera, err=err)

    def gauss_seidel(self, f, f1, maxitera, err):
        L = f.shape[0]
        xk = np.zeros((L, 1))
        xkc = xk.copy()
        itera = 0
        erro = float('inf')

        while itera < maxitera and erro > err:
            itera += 1
            xkc = xk.copy()
            for i in range(L):
                soma1 = 0
                for j in range(L):
                    if i != j:
                        soma1 += f[i, j] * xk[j]
                xk[i] = (f1[i] - soma1) / f[i, i]

            erro = np.max(np.abs(xk - xkc)) / np.max(np.abs(xk))
            x_values = [f"{xk[i, 0]:.6f}" for i in range(L)]
            self.iteration_table.insert("", "end", values=(itera, *x_values, f"{erro:.6f}"))

if __name__ == "__main__":
    root = tk.Tk()
    app = GaussSeidelApp(root)
    root.mainloop()
