O intuito deste projeto é desenvolver um bot que tome as melhores decisões possíveis em uma partida de blackjack


O primeiro passo para chegar ao objetivo do projeto, será desenvolver um programa que avalie a melhor decisão tendo como base as cartas que estão na mesa. Após consolidar este passo, será implementada a tomada de decisão por parte do programa.


Descrição curta e objetiva de cada arquivo.

README.md

    Descrição do projeto
    Regras do jogo usadas
    Como rodar simulações
    Exemplos de uso

config.py

    Todas as configurações globais
    Regras da mesa
    Parâmetros de simulação
    Nada de lógica

main.py

    Ponto de entrada do projeto
    Chama simulações específicas
    Imprime resultados finais

core/ — motor do jogo (regras puras)
core/deck.py

    Criação do baralho
    Shuffle
    Compra de cartas
    Controle de % restante
    Reembaralhamento por RESHUFFLE_PCT

core/hand.py

    Representação da mão
    Cálculo do valor total
    Lógica de Ás (soft vs hard)
    Bust / blackjack

core/dealer.py

    Regras fixas do dealer
    Lógica de compra até parar
    Respeita soft 17 configurado

core/game.py

    Orquestra uma mão completa
    Distribuição inicial
    Execução do turno do jogador (ação forçada)
    Execução do dealer
    Determina win / lose / push

simulation/ — Monte Carlo
simulation/simulate.py

    Roda N simulações para uma ação fixa
    Força HIT ou STAND
    Retorna resultados brutos

simulation/results.py

    Agrega resultados
    Calcula porcentagens
    Calcula EV
    Estrutura dados para análise

analysis/ — comparação de decisões
analysis/ev_calculator.py

    Compara HIT vs STAND
    Dado um estado fixo
    Decide qual ação tem maior EV
    Base da estratégia básica

tests/ — validação
tests/test_hand.py

    Testes de soft/hard
    Testes com múltiplos Áses
    Bust e blackjack

tests/test_deck.py

    Quantidade correta de cartas
    Shuffle funcional
    Reembaralhamento por %

Regra geral

    core não sabe de simulação
    simulation não muda regras
    analysis não executa jogo
    config não executa nada