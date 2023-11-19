import random

def gambler_ruin_simulation(initial_money, win_probability, target_multiplier, num_simulations):
    total_successes = 0

    for _ in range(num_simulations):
        current_money = initial_money

        while current_money > 0 and current_money < initial_money * target_multiplier:
            # Simula a aposta
            if random.uniform(0, 1) < win_probability:
                current_money += 1
            else:
                current_money -= 1

        # Verifica se o jogador atingiu o objetivo
        if current_money >= initial_money * target_multiplier:
            total_successes += 1

    probability_of_success = total_successes / num_simulations
    return probability_of_success

# Parâmetros
initial_money = 100
win_probability = 18 / 38  # Probabilidade de ganhar na roleta
target_multiplier = 2
num_simulations = 10000

# Simulação
probability_of_success = gambler_ruin_simulation(initial_money, win_probability, target_multiplier, num_simulations)

# Imprimir resultado
print(f"Probabilidade de Sucesso: {probability_of_success:.2%}")