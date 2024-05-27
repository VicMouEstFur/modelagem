Explicação do Código Passo a Passo
Vamos detalhar cada parte do código, explicando de forma simples o que cada bloco faz e como ele contribui para o funcionamento do programa.

Importação de Módulos
python
Copiar código
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import math
tkinter: Este é o módulo padrão do Python para criar interfaces gráficas. tk é a versão básica, enquanto ttk fornece widgets (elementos de interface) estilizados.
messagebox: Usado para mostrar mensagens de erro ou informação ao usuário.
math: Este módulo fornece funções matemáticas, como cos (cosseno) e exp (exponencial).
Definição das Funções Matemáticas
python
Copiar código
def f1(x):
    return x**5 - 6

def f2(x):
    return 2 * math.cos(x) - (math.exp(x) / 2)
f1(x): Define a função matemática 
𝑓
(
𝑥
)
=
𝑥
5
−
6
f(x)=x 
5
 −6.
f2(x): Define a função matemática 
𝑓
(
𝑥
)
=
2
cos
⁡
(
𝑥
)
−
𝑒
𝑥
2
f(x)=2cos(x)− 
2
e 
x
 
​
 .
Função do Método da Falsa Posição
python
Copiar código
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
Parâmetros: a e b são os extremos do intervalo, max_iterations é o número máximo de iterações, epsilon é a precisão desejada, e func é a função a ser usada (f1 ou f2).
Verificação Inicial: Se func(a) * func(b) >= 0, os valores não cercam uma raiz e a função retorna uma mensagem de erro.
Loop de Iteração: Calcula uma aproximação da raiz usando o método da falsa posição, até atingir o número máximo de iterações ou a precisão desejada.
Armazenamento de Resultados: Cada iteração é armazenada em uma lista para exibição posterior.
Retorno: A função retorna a raiz aproximada e a lista de iterações.
Função de Cálculo
python
Copiar código
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
Entrada do Usuário: Obtém os valores de a, b, max_iterations, e epsilon das entradas do usuário. Se algum valor for inválido, exibe uma mensagem de erro.
Seleção da Função: Verifica qual função (f1 ou f2) foi selecionada pelo usuário.
Cálculo: Chama a função false_position com os parâmetros fornecidos e atualiza a interface com os resultados.
Atualização da Tabela: Limpa a tabela de resultados anteriores e insere os novos resultados.
Criação da Interface Gráfica
python
Copiar código
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
Janela Principal: Cria a janela principal da aplicação (app).
Frame de Entrada: Cria um frame para organizar os widgets de entrada.
Entradas de Texto: Cria caixas de entrada para a, b, max_iterations, e epsilon.
Botões de Opção: Permite ao usuário selecionar qual função usar (f1 ou f2).
Botão Calcular: Cria um botão para iniciar o cálculo quando clicado.
Label de Resultado: Cria um label para mostrar o resultado do cálculo.
Tabela de Resultados: Cria uma tabela para mostrar as iterações e resultados.
Loop Principal: Inicia o loop principal da interface gráfica, mantendo a janela aberta.
Resumo
Este código cria uma aplicação gráfica que permite ao usuário resolver uma equação usando o método da falsa posição. O usuário insere os parâmetros necessários, escolhe a função, e o programa calcula a raiz aproximada, mostrando as iterações em uma tabela.
