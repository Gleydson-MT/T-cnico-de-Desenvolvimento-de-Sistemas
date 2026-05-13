# agenda = {

#     "Julia": "8599664433",
#     "Marcos": "8598764532",
#     "Lopes": "8588745423"
# }
# nome = input("Digite o nome da pessoa que você deseja visualizar o telefone: ")

# if nome in agenda:  
#     print(agenda[nome])
# else:
#     print("Nome não encontrado!")

agenda = {

    "Julia": "8599664433",
    "Marcos": "8598764532",
    "Lopes": "8588745423"
}


for i in range(5):
    nome = (input("Digite o nome do novo contato: "))
    telefone = (input("Digite o número do novo contato: "))
    agenda[nome] = telefone

print(agenda)

while True:
    consulta = input("Deseja consultar a agenda? (S/N): ")

    if consulta.lower == "n":
        break
    else:
        c = input("Escreva o nome da lista que deseja consultar: ")
        if c != nome:
            print("CONTATO NÃO ESTÁ NA LISTA")
        else:
            print(agenda[nome])