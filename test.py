# # # hashmap

caderno = dict()

caderno['maça'] = 0.50
caderno['pera'] = 0.70
print(caderno)
caderno['abacaxi'] = 10.50
caderno['maça'] = 1.50
print(caderno)

def verifica(nome):
    if caderno.get(nome):
        print("Ta tendo !!")
    else:
        print('Tem mas acabou //:')

verifica('maça')
verifica('uva')