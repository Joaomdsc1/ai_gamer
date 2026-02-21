import random

class Baralho:
    def __init__(self, num_decks = 8):
        self.valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.naipes = ['♠', '♥', '♦', '♣']
        self.baralho = []
        self.num_decks = num_decks
        self.criar_baralho()
        self.shuffle()

    def criar_baralho(self):
        for _ in range(self.num_decks):
            for i in self.valores:
                for j in self.naipes:
                    self.baralho.append(i+j)

    def shuffle(self):
        random.shuffle(self.baralho)

    def __len__(self):
        return len(self.baralho)