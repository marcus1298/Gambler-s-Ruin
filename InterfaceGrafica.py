import random
import tkinter as tk
from tkinter import ttk

def simulacao_gambler_ruin(dinheiro_inicial, probabilidade_ganhar, multiplicador_alvo):
    dinheiro = dinheiro_inicial
    passos = 0

    while dinheiro > 0 and dinheiro < dinheiro_inicial * multiplicador_alvo and passos < 10000:

        if random.uniform(0, 1) < probabilidade_ganhar:
            dinheiro *= 2
        else:
            dinheiro -= 2
        passos += 1

    return dinheiro >= dinheiro_inicial * multiplicador_alvo, passos

def simular():
    dinheiro_inicial = int(entry_dinheiro_inicial.get())
    probabilidade_ganhar = float(entry_probabilidade.get())
    multiplicador_alvo = int(entry_multiplicador_alvo.get())
    num_simulacoes = int(entry_num_simulacoes.get())

    contagem_sucesso = 0
    total_passos = 0

    for _ in range(num_simulacoes):
        sucesso, passos = simulacao_gambler_ruin(dinheiro_inicial, probabilidade_ganhar, multiplicador_alvo)
        if sucesso:
            contagem_sucesso += 1
        total_passos += passos

    probabilidade_sucesso = contagem_sucesso / num_simulacoes
    media_passos = total_passos / num_simulacoes

    resultado_label.config(text=f"Probabilidade de Sucesso: {probabilidade_sucesso:.2%}\nMédia de Passos: {media_passos:.2f}")

# Criar a interface gráfica
root = tk.Tk()
root.title("Simulação Gambler's Ruin")

# Elementos da interface
label_dinheiro_inicial = ttk.Label(root, text="Dinheiro Inicial:")
label_dinheiro_inicial.grid(row=0, column=0, sticky="w")
entry_dinheiro_inicial = ttk.Entry(root)
entry_dinheiro_inicial.grid(row=0, column=1)

label_probabilidade = ttk.Label(root, text="Probabilidade de Ganhar:")
label_probabilidade.grid(row=1, column=0, sticky="w")
entry_probabilidade = ttk.Entry(root)
entry_probabilidade.grid(row=1, column=1)

label_multiplicador_alvo = ttk.Label(root, text="Multiplicador Alvo:")
label_multiplicador_alvo.grid(row=2, column=0, sticky="w")
entry_multiplicador_alvo = ttk.Entry(root)
entry_multiplicador_alvo.grid(row=2, column=1)

label_num_simulacoes = ttk.Label(root, text="Número de Simulações:")
label_num_simulacoes.grid(row=3, column=0, sticky="w")
entry_num_simulacoes = ttk.Entry(root)
entry_num_simulacoes.grid(row=3, column=1)

btn_simular = ttk.Button(root, text="Simular", command=simular)
btn_simular.grid(row=4, column=0, columnspan=2, pady=10)

resultado_label = ttk.Label(root, text="")
resultado_label.grid(row=5, column=0, columnspan=2)

# Iniciar o loop da interface gráfica
root.mainloop()
