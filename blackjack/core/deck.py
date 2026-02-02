import random

class Baralho:
    def __init__(self):
        self.valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.naipes = ['♠', '♥', '♦', '♣']
        self.baralho = []
        self.criar_baralho()
        self.shuffle()


    def criar_baralho(self):
        for i in self.valores:
            for j in self.naipes:
                self.baralho.append(i+j)

    def shuffle(self):
        random.shuffle(self.baralho)

    
baralho = Baralho()
print(len(baralho.baralho))
print(baralho.baralho)