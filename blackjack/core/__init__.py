from game import Game
from deck import Baralho
from time import sleep

def main():
    print("=== BlackJack ===\n")
    baralho = Baralho()
    jogo = Game(baralho)
    jogar = True
    vitorias_jogador = 0
    vitorias_mesa = 0

    while jogar == True:
        if len(baralho) < 0.5 * 52:
            print("Reiniciando o Baralho")
            baralho.baralho = Baralho().baralho
            baralho.shuffle()
            
        print("Distribuindo cartas...")
        dealer, jogador = jogo.distribuir_cartas()

        print("=== Situação inicial ===")
        print(f"Mão do Dealer: {dealer[1]['carta']}")
        print(f"\nSua mão: {jogador[0]['carta']} e {jogador[1]['carta']}")
        pontos_jogador = jogo.pontuacao_atual(jogador)
        print(f"Pontuação atual: {pontos_jogador}")

        while True:
            if pontos_jogador == 21:
                break
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
        
        if pontos_dealer > 21:
            print("\nA mesa estourou")

        vencedor = jogo.vencedor(pontos_jogador, pontos_dealer)
        if vencedor == "Empate":
            print("A mão empatou")
        else:
            print(f"\nO vencedor foi o {vencedor}\n")

        if vencedor == "Jogador":
            vitorias_jogador += 1
        elif vencedor == "Dealer":
            vitorias_mesa += 1
        else:
            continue
        
        if vitorias_jogador > vitorias_mesa:
            print(f"O placar agora é de {vitorias_jogador} a {vitorias_mesa} para o JOGADOR")
        elif vitorias_mesa > vitorias_jogador:
            print(f"O placar agora é de {vitorias_mesa} a {vitorias_jogador} para a MESA")
        else:
            print(f"Estamos empatados em {vitorias_mesa} a {vitorias_jogador}")

        print("\nO baralho ainda tem ", len(baralho), " cartas.")

        replay = input("\nJogar novamente? (s ou n)\n")
        if replay == 's':
            continue
        else:
            jogar = False


if __name__ == "__main__":
    main()