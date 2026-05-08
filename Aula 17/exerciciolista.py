#Crie um programa que pede o nome de 10 pessoas. Adicione cada nome em uma lista e imprima verticamente.
#Ex:
# Maria
# Joao
# Matheus
# ...

lista = []
for i in range(10):
    nome = input("Digite o nome que deseja adicionar: ")
    lista.append(nome)
numero = 1
for n in lista:
    print(f"{numero}. {n}")
    numero+=1
