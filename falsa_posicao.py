import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import math

def f1(x):
    return x**5 - 6

def f2(x):
    return 2 * math.cos(x) - (math.exp(x) / 2)

def false_position(a, b, max_iterations, epsilon, func):
    if func(a) * func(b) >= 0:
        return "Os valores iniciais não cercam uma raiz.", []

    iter_count = 0
    iterations = []

    xi = a
    while iter_count < max_iterations:
        xi_old = xi
        xi = (a * func(b) - b * func(a)) / (func(b) - func(a))
        fxi = func(xi)
        error = abs(xi - xi_old)

        iterations.append((iter_count, a, b, xi, fxi, error))

        if error < epsilon:
            break

        if func(a) * fxi < 0:
            b = xi
        else:
            a = xi

        iter_count += 1

    return f"A raiz aproximada é: {xi:.6f}", iterations

def calculate():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        max_iterations = int(entry_max_iterations.get())
        epsilon = float(entry_epsilon.get())
    except ValueError:
        messagebox.showerror("Erro de entrada", "Por favor, insira valores válidos.")
        return

    selected_function = func_var.get()
    if selected_function == "f1":
        func = f1
    elif selected_function == "f2":
        func = f2
    else:
        messagebox.showerror("Erro de função", "Por favor, selecione uma função válida.")
        return

    result, iterations = false_position(a, b, max_iterations, epsilon, func)
    result_label.config(text=result)

    for i in tree.get_children():
        tree.delete(i)

    for iteration in iterations:
        tree.insert("", "end", values=[
            iteration[0],
            f"{iteration[1]:.6g}",
            f"{iteration[2]:.6g}",
            f"{iteration[3]:.6g}",
            f"{iteration[4]:.6g}",
            f"{iteration[5]:.6g}"
        ])

app = tk.Tk()
app.title("Método da Falsa Posição")

frame_input = tk.Frame(app)
frame_input.pack(pady=10)

tk.Label(frame_input, text="a:").grid(row=0, column=0, padx=5, pady=5)
entry_a = tk.Entry(frame_input)
entry_a.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_input, text="b:").grid(row=1, column=0, padx=5, pady=5)
entry_b = tk.Entry(frame_input)
entry_b.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Iterações Máximas:").grid(row=2, column=0, padx=5, pady=5)
entry_max_iterations = tk.Entry(frame_input)
entry_max_iterations.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Epsilon:").grid(row=3, column=0, padx=5, pady=5)
entry_epsilon = tk.Entry(frame_input)
entry_epsilon.grid(row=3, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Função:").grid(row=4, column=0, padx=5, pady=5)
func_var = tk.StringVar(value="f1")
ttk.Radiobutton(frame_input, text="f(x) = x^5 - 6", variable=func_var, value="f1").grid(row=4, column=1, padx=5, pady=5)
ttk.Radiobutton(frame_input, text="f(x) = 2*cos(x) - (e^x)/2", variable=func_var, value="f2").grid(row=5, column=1, padx=5, pady=5)

button_calculate = tk.Button(frame_input, text="Calcular", command=calculate)
button_calculate.grid(row=6, column=0, columnspan=2, pady=10)

result_label = tk.Label(app, text="")
result_label.pack(pady=10)

columns = ["Iteração", "a", "b", "xi", "f(xi)", "Erro"]
tree = ttk.Treeview(app, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.pack(pady=10)

app.mainloop()
