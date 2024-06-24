import os
import random
import time
import csv
from colorama import Fore, Style, init

# Inicialização do Colorama para a coloração do terminal
init(autoreset=True)

# Dicionário de emojis por tipo
tipo_emojis = {
    'fogo': '🔥',
    'água': '💧',
    'grama': '🌿',
    'pedra': '🪨',
    'ar': '🌬️',
    'elétrico': '⚡',
    'gelo': '❄️',
    'terra': '🌍',
    'dragão': '🐉',
    'psíquico': '🔮',
    'sombrio': '🌑'
}

# Carrega Pokemons do arquivo CSV
def carregar_pokemons():
    pokemons = []
    with open('pokemons.csv', 'r') as file:
        reader = csv.DictReader(file)
        for linha in reader:
            nome = linha['nome']
            tipo = linha['tipo']
            emoji = tipo_emojis.get(tipo, '')
            pokemons.append({'nome': nome, 'tipo': tipo, 'emoji': emoji})
    return pokemons

# Seleciona Pokemons aleatoriamente
def selecionar_pokemons(pokemons, quantidade = 4):
    return random.sample(pokemons, quantidade)

# Define as regras de vantagem entre os tipos
vantagens = {
    'fogo': ['grama', 'gelo'],
    'água': ['fogo', 'terra'],
    'grama': ['água', 'terra'],
    'pedra': ['ar', 'fogo', 'gelo'],
    'ar': ['grama'],
    'elétrico': ['água', 'ar'],
    'gelo': ['grama', 'terra', 'ar'],
    'terra': ['pedra', 'elétrico', 'fogo'],
    'dragão': ['grama', 'terra', 'ar'],
    'psíquico': ['lutador', 'veneno'],
    'sombrio': ['psíquico', 'fantasma']
}

# Função de batalha
def batalha(pokemon1, pokemon2):
    print(f"Batalha: {pokemon1['nome']} ({pokemon1['tipo']} {pokemon1['emoji']}) vs {pokemon2['nome']} ({pokemon2['tipo']} {pokemon2['emoji']})")

    if pokemon2['tipo'] in vantagens[pokemon1['tipo']]:
        print(f"{Fore.GREEN}{pokemon1['nome']} vence!{Style.RESET_ALL}\n")
        return (3, 0)
    elif pokemon1['tipo'] in vantagens[pokemon2['tipo']]:
        print(f"{Fore.GREEN}{pokemon2['nome']} vence!{Style.RESET_ALL}\n")
        return (0, 3)
    else:
        print(f"{Fore.YELLOW}Empate!{Style.RESET_ALL}\n")
        return (1, 1)

# Contador regressivo
def contador_regressivo():
    for i in range(10, -1, -1):
        print(i, end=' ', flush=True)
        time.sleep(1)
    print()

# Limpa a tela
def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Salva o resultado no arquivo
def salvar_resultado(nome1, nome2, vencedor):
    with open("resultado_jogo.txt", "a") as file:
        file.write(f"Jogador 1: {nome1}\n")
        file.write(f"Jogador 2: {nome2}\n")
        file.write(f"Vencedor: {vencedor}\n")
        file.write("-" * 40 + "\n")

# Função para ver os resultados
def ver_resultados():
    if os.path.exists("resultado_jogo.txt"):
        with open("resultado_jogo.txt", "r") as file:
            print(file.read())
    else:
        print("Nenhum resultado disponível.")

# Função para mostrar o menu
def mostrar_menu():
    print("1. Jogar")
    print("2. Ver resultados")
    print("3. Sair")
    escolha = input("Escolha uma opção: ")
    print("\n")
    print(f"{Fore.RED}{'*'*40}\n{'*' * 5} {' *** '.center(28)} {'*' * 5}\n{'*'*40}{Style.RESET_ALL}")
    return escolha

# Função principal
def Batalha():
    pokemons = carregar_pokemons()
    
    while True:
        limpar_tela()
        print(f"{Fore.RED}{'*'*40}\n{'*' * 5} {'BATALHA POKEMON'.center(28)} {'*' * 5}\n{'*'*40}{Style.RESET_ALL}")
        escolha = mostrar_menu()

        if escolha == '1':
            limpar_tela()
            print(f"{'*'*40}\n{'*' * 5}{'REGISTRO DE TREINADORES'.center(28)} {'*' * 5}\n{'*'*40}")
            nome1 = input("Digite o nome do Jogador 1: ")
            nome2 = input("Digite o nome do Jogador 2: ")

            jogador1 = selecionar_pokemons(pokemons)
            jogador2 = selecionar_pokemons(pokemons)

            pontos_j1 = 0
            pontos_j2 = 0

            limpar_tela()
            print(f"{nome1} e {nome2} estão escolhendo seu time...")
            contador_regressivo()

            limpar_tela()
            print(f"{'*'*35}\nTime do jogador {nome1}: \n{'*'*35}")
            for p in jogador1:
                print(f"{p['nome']} ( {p['tipo']} {p['emoji']} )")

            print("\n")

            print(f"{'*'*35}\nTime do jogador {nome2}: \n{'*'*35}")
            for p in jogador2:
                print(f"{p['nome']} ( {p['tipo']} {p['emoji']} )")

            for pokemon1, pokemon2 in zip(jogador1, jogador2):
                print("Próximo turno começando em:")
                contador_regressivo()
                limpar_tela()

                pontos_rodada_j1, pontos_rodada_j2 = batalha(pokemon1, pokemon2)
                pontos_j1 += pontos_rodada_j1
                pontos_j2 += pontos_rodada_j2
                print(f"Pontos atuais: {nome1} - {pontos_j1}, {nome2} - {pontos_j2}\n")

            limpar_tela()
            print(f"Pontuação Final:\n{nome1}: {pontos_j1} pontos\n{nome2}: {pontos_j2} pontos")

            if pontos_j1 > pontos_j2:
                resultado_final = f"{Fore.GREEN}{nome1} vence o jogo!{Style.RESET_ALL}"
                salvar_resultado(nome1, nome2, nome1)
            elif pontos_j2 > pontos_j1:
                resultado_final = f"{Fore.GREEN}{nome2} vence o jogo!{Style.RESET_ALL}"
                salvar_resultado(nome1, nome2, nome2)
            else:
                resultado_final = f"{Fore.RED}O jogo termina em empate!{Style.RESET_ALL}"
                salvar_resultado(nome1, nome2, "Empate")

            print(resultado_final)
            print(" ")
            input("Pressione Enter para continuar...")

        elif escolha == '2':
            limpar_tela()
            ver_resultados()
            input("Pressione Enter para continuar...")

        elif escolha == '3':
            print(f"O sistema foi finalizado pelo usuário ...")
            break

        else:
            print("Opção inválida! Tente novamente.")
            input("Pressione Enter para continuar...")

# Início do jogo
Batalha()