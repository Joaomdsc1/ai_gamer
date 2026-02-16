# # # somar os itens de um array utilizando recursão

lista = [1,2,3,4,10]
soma = 0
def somar_lista(lista, soma):
    x = lista.pop(-1)
    soma += x
    return soma
i = 0
while i < len(lista):
    soma = somar_lista(lista, soma)

print(soma)