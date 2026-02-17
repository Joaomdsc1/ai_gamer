# # # Função para contar os itens de uma lista

lista = [1, 4, 6, 7]

def contagem(lista):
    contador = 0
    for item in lista:
        contador += 1
    return contador

def maior(lista):
    valor = lista[0]
    for i in range(len(lista)):
        if valor < lista[i]:
            valor = lista[i]
        else:
            continue
    return valor


print(contagem(lista))
print(maior(lista))