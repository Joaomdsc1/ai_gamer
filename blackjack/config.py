# ==============================
# BARALHO
# ==============================

NUM_DECKS = 1

# Percentual do baralho restante para reembaralhar
# 1.0 = reembaralha toda mão
# 0.25 = reembaralha quando restar 25%
RESHUFFLE_PCT = 1.0


# ==============================
# REGRAS DO JOGO
# ==============================

BLACKJACK_PAYOUT = 1.5  # 3:2

DEALER_HITS_SOFT_17 = False  # False = dealer para no soft 17

ALLOW_HIT = True
ALLOW_STAND = True

# Desabilitados neste estágio
ALLOW_DOUBLE = False
ALLOW_SPLIT = False
ALLOW_SURRENDER = False
ALLOW_INSURANCE = False


# ==============================
# SIMULAÇÃO
# ==============================

# Número de simulações por ação (HIT / STAND)
SIMULATIONS_PER_ACTION = 100_000

# Seed para reprodutibilidade (None = aleatório)
RANDOM_SEED = None


# ==============================
# DEBUG / LOG
# ==============================

VERBOSE = False
