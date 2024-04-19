import os
import time
import random
from colorama import Fore, Style

# Criando o Dicionario de Emojis para cada tipo (fogo, agua, ar, ...)
tipo_emoji = {
    'fogo': '🔥',
    'água': '💧',
    'grama': '🌿',
    'pedra': '🪨',
    'ar': '🌬️',
    'elétrico': '⚡',
    'gelo': '❄️',
    'terra': '🌍'
}

# Criando o Dicionario 'efetivo' para saber a vantagem que um tipo tem sobre o outro
efetivo = {
    'fogo': ['grama', 'gelo'],
    'água': ['fogo', 'terra'],
    'grama': ['água', 'terra'],
    'pedra': ['ar', 'fogo', 'gelo'],
    'ar': ['grama'],
    'elétrico': ['água', 'ar'],
    'gelo': ['grama', 'terra', 'ar'],
    'terra': ['pedra', 'elétrico', 'fogo']
}


