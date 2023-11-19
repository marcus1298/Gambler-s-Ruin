import random

def simulacao_gambler_ruin(dinheiro_inicial, probabilidade_ganhar, multiplicador_alvo):
    dinheiro = dinheiro_inicial
    passos = 0

    while dinheiro > 0 and dinheiro < dinheiro_inicial * multiplicador_alvo:
        # Simula um lançamento de moeda para determinar se o jogador ganha ou perde
        if random.uniform(0, 1) < probabilidade_ganhar:
            dinheiro *= 2  # Jogador ganha e dobra o dinheiro
        else:
            dinheiro -= 2  # Jogador perde $1
        passos += 1

    return dinheiro >= dinheiro_inicial * multiplicador_alvo, passos

# Parâmetros
dinheiro_inicial = 100
probabilidade_ganhar = 18 / 38  # Probabilidade de ganhar na roleta
multiplicador_alvo = 2

# Simulação
num_simulacoes = 10000
contagem_sucesso = 0
total_passos = 0

for _ in range(num_simulacoes):
    sucesso, passos = simulacao_gambler_ruin(dinheiro_inicial, probabilidade_ganhar, multiplicador_alvo)
    if sucesso:
        contagem_sucesso += 1
    total_passos += passos

# Calcula as probabilidades
probabilidade_sucesso = contagem_sucesso / num_simulacoes
media_passos = total_passos / num_simulacoes

# Imprime os resultados
print(f"Dinheiro Inicial: {dinheiro_inicial}")
print(f"Probabilidade de Ganhar: {probabilidade_ganhar}")
print(f"Multiplicador Alvo: {multiplicador_alvo}")
print(f"Probabilidade de Sucesso: {probabilidade_sucesso}")
print(f"Média de Passos: {media_passos}")
