from game import Game
from deck import Baralho
from time import sleep

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
    
    sleep(1)

    print(f"\nA mão do do dealer é {dealer[1]['carta']} e {dealer[0]['carta']}")
    pontos_dealer = jogo.pontuacao_atual(dealer)
    print(f"A pontuação do dealer é {pontos_dealer}")

    sleep(1)

    if pontos_jogador <= 21:
        while pontos_dealer < 17:
            dealer = jogo.comprar(dealer)
            print(f"Nova carta do Dealer é: {dealer[-1]['carta']}")
            pontos_dealer = jogo.pontuacao_atual(dealer)
            print(f"Pontuação do Dealer é: {pontos_dealer}")
            sleep(1)
    
    vencedor = jogo.vencedor(pontos_jogador, pontos_dealer)
    print(f"\nO vencedor foi o {vencedor}")

if __name__ == "__main__":
    main()