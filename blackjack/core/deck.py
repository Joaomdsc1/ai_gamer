import random

def criar_baralho():
    """Cria um baralho completo de 52 cartas"""
    naipes = ['♠', '♥', '♦', '♣']  # Paus, Copas, Ouros, Espadas
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    
    baralho = []
    for naipe in naipes:
        for valor in valores:
            baralho.append((valor, naipe))
    
    return baralho


baralho = criar_baralho()
random.shuffle(baralho)
print(f"Baralho criado com {len(baralho)} cartas")
print(f"Primeiras 5 cartas: {baralho[:5]}")