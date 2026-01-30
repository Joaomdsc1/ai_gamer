import random
from enum import Enum

class Naipe(Enum):
    PAUS = '♣'
    COPAS = '♥'
    OUROS = '♦'
    ESPADAS = '♠'

class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe
    
    def __repr__(self):
        return f"{self.valor}{self.naipe.value}"
    
    def valor_blackjack(self):
        """Retorna o valor da carta no Blackjack"""
        if self.valor in ['J', 'Q', 'K']:
            return 10
        elif self.valor == 'A':
            return 11  # Será ajustado na lógica do jogo
        else:
            return int(self.valor)

class Baralho:
    def __init__(self, numero_baralhos=6, limite_reset=0.25):
        """
        Args:
            numero_baralhos: Quantos baralhos usar (padrão: 6, comum em cassinos)
            limite_reset: Porcentagem mínima para reset (padrão: 0.25 = 25%)
        """
        self.cartas = []
        self.numero_baralhos = numero_baralhos
        self.limite_reset = limite_reset  # Ex: 0.25 = 25% mínimo
        self.cartas_totais = 52 * numero_baralhos
        self.reset()
    
    def reset(self):
        """Recria e embaralha o baralho do zero"""
        self.cartas = []
        valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        
        for _ in range(self.numero_baralhos):
            for naipe in Naipe:
                for valor in valores:
                    self.cartas.append(Carta(valor, naipe))
        
        self.embaralhar()
        print(f"✅ Baralho resetado! {len(self.cartas)} cartas disponíveis.")
    
    def embaralhar(self):
        """Embaralha as cartas"""
        random.shuffle(self.cartas)
    
    def comprar(self):
        """Compra uma carta do topo do baralho"""
        if len(self.cartas) == 0:
            raise Exception("Baralho vazio! Chame reset() primeiro.")
        return self.cartas.pop()
    
    def verificar_reset(self):
        """
        Verifica se precisa resetar o baralho (após uma mão).
        Retorna True se resetou, False caso contrário.
        """
        cartas_restantes = len(self.cartas)
        limite_minimo = self.cartas_totais * self.limite_reset
        
        if cartas_restantes < limite_minimo:
            porcentagem = (cartas_restantes / self.cartas_totais) * 100
            print(f"⚠️  Baralho com apenas {cartas_restantes} cartas ({porcentagem:.1f}%) - Resetando...")
            self.reset()
            return True
        return False
    
    def cartas_restantes(self):
        """Retorna quantas cartas ainda estão no baralho"""
        return len(self.cartas)
    
    def porcentagem_restante(self):
        """Retorna a porcentagem de cartas restantes"""
        return (len(self.cartas) / self.cartas_totais) * 100
    
    def __len__(self):
        return len(self.cartas)


# ====== EXEMPLO DE USO NO SEU BOT ======

class BlackjackGame:
    def __init__(self):
        self.baralho = Baralho(numero_baralhos=6, limite_reset=0.25)
        self.mao_jogador = []
        self.mao_dealer = []
    
    def jogar_mao(self):
        """Executa uma mão completa de Blackjack"""
        print(f"\n{'='*40}")
        print("NOVA MÃO")
        print(f"{'='*40}")
        
        # 1. Distribuir cartas iniciais
        self.mao_jogador = [self.baralho.comprar(), self.baralho.comprar()]
        self.mao_dealer = [self.baralho.comprar(), self.baralho.comprar()]
        
        print(f"Cartas jogador: {self.mao_jogador}")
        print(f"Cartas dealer: [{self.mao_dealer[0]}, ?]")
        print(f"Cartas restantes no baralho: {self.baralho.cartas_restantes()}")
        
        # 2. Aqui viria a lógica do jogo (hit, stand, etc.)
        # ...
        
        # 3. Após terminar a mão, verificar se precisa resetar
        print(f"\n--- FIM DA MÃO ---")
        resetou = self.baralho.verificar_reset()
        if not resetou:
            print(f"Baralho ainda tem {self.baralho.cartas_restantes()} cartas ({self.baralho.porcentagem_restante():.1f}%)")
        
        return resetou
    
    def simular_multiplas_maos(self, num_maos=10):
        """Simula várias mãos para demonstrar o reset automático"""
        for i in range(num_maos):
            print(f"\n🎰 Mão #{i+1}")
            self.jogar_mao()
            
            # Simular uso de algumas cartas (entre 6-12 por mão)
            cartas_por_mao = random.randint(6, 12)
            for _ in range(cartas_por_mao):
                if len(self.baralho) > 0:
                    self.baralho.comprar()


# ====== TESTE ======

if __name__ == "__main__":
    # Teste simples
    print("=== TESTE DO BARALHO ===")
    jogo = BlackjackGame()
    
    # Verificar estado inicial
    print(f"\nEstado inicial:")
    print(f"Total de cartas: {jogo.baralho.cartas_totais}")
    print(f"Cartas no baralho: {len(jogo.baralho)}")
    print(f"Limite de reset: {jogo.baralho.limite_reset*100}%")
    
    # Jogar algumas mãos
    jogo.simular_multiplas_maos(3)
    
    # Teste manual
    print("\n\n=== TESTE MANUAL ===")
    baralho_teste = Baralho(numero_baralhos=1, limite_reset=0.5)  # Reset em 50%
    
    # Comprar cartas até chegar perto do limite
    print(f"\nComprando cartas...")
    while len(baralho_teste) > 30:  # 52 * 0.5 = 26, então vamos até 30
        baralho_teste.comprar()
    
    print(f"Cartas restantes: {len(baralho_teste)} ({baralho_teste.porcentagem_restante():.1f}%)")
    
    # Chamar verificar_reset (como faria após uma mão)
    print("\nVerificando reset após mão...")
    baralho_teste.verificar_reset()  # Deve resetar pois está abaixo de 50%