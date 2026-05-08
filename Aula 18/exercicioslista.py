#1. lista de compras
#Crie uma lista com 5 intens de supermercado. Exiba o primeiro item, o último e o total de itens da lista usando len().

# compras = ["Arroz", "Feijão", "Café", "Ovos", "Manteiga"]

# print(f"O primeiro da lista é: {compras[0]}, o ultimo da lista é :{compras[4]}, a lista tem: {len(compras)} itens.")

produtos = 0

for i in range(5):
    item = input("Digite o novo item: ")
    produtos.append(item)

print(produtos[0])
print(produtos[-1])
print(len(produtos))