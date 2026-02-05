from game import Game
from deck import Baralho

def main():
    print("=== BlackJack ===\n")
    baralho = Baralho()
    jogo = Game()

    print("Distribuindo cartas...")
    dealer, jogador = jogo.distribuir_cartas()

    print("=== Situação inicial ===")
    print(f"Mão do Dealer: {dealer[1]['carta']}")
    print(f"\nSua mão: {jogador[0]['carta']} e {jogador[1]['carta']}")
    pontos_jogador = jogo.pontuacao_atual(jogador)
    print(f"Pontuação atual: {pontos_jogador}")

    while True:
        comando = input("Quer mais uma carta? (s ou n) ")
        if comando == 's':
            jogador = jogo.comprar(jogador)
            print(f"Nova carta: {jogador[-1]['carta']}")
            pontos_jogador = jogo.pontuacao_atual(jogador)
            print(f"Pontuação atual: {pontos_jogador}")
            if pontos_jogador == 21:
                print("Jogador fez 21")
                break
            elif pontos_jogador > 21:
                print("Jogador estourou")
                break
            else:
                continue
        else:
            break
    

if __name__ == "__main__":
    main()