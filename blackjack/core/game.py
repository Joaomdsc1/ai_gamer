from deck import Baralho

class Game():
    
    def __init__(self, baralho: Baralho):
        self.baralho = baralho

    def distribuir_cartas(self):
        mao_dealer = []
        mao_jogador = []

        mao_jogador.append({
            "carta": self.baralho.baralho.pop(0),
            "visivel": True
        })
        
        mao_dealer.append({
            "carta": self.baralho.baralho.pop(0),
            "visivel": False
        })

        mao_jogador.append({
            "carta": self.baralho.baralho.pop(0),
            "visivel": True
        })
        
        mao_dealer.append({
            "carta": self.baralho.baralho.pop(0),
            "visivel": True
        })

        return mao_dealer, mao_jogador  

    def comprar(self, mao_jogador):
        mao_jogador.append({
            "carta": self.baralho.baralho.pop(0),
            "visivel": True
        })
        return mao_jogador
    
    def pontuacao_atual(self, mao):
        total = 0
        ases = 0

        for item in mao:
            valor = str(item["carta"])

            if valor and valor[-1] in ("♣", "♦", "♥", "♠"):
                valor = valor[:-1]
            
            if valor in ("J", "Q", "K"):
                total += 10
            elif valor == "A":
                total += 11
                ases += 1
            else:
                total += int(valor)
        
        while total > 21 and ases > 0:
            total -= 10
            ases -= 1
        
        return total
    
    def vencedor(self, ponto_jogador, ponto_dealer):
        if ponto_jogador > 21:
            return "Dealer"
        elif ponto_dealer > 21:
            return "Jogador"
        elif ponto_jogador > ponto_dealer:
            return "Jogador"
        elif ponto_dealer == ponto_jogador:
            return "Empate"
        else:
            return "Dealer"