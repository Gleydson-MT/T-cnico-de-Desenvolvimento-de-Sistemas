# 5. Verificação de estoque
# Um mercadinho tem a lista estoque = ["arroz", "feijão", "macarrão", "leite", "óleo"]. Peça ao usuário um produto com input() e informe se ele está ou não disponível no estoque. Depois, exiba o estoque em ordem alfabética usando sorted().

estoque = ["arroz", "feijão", "macarrão", "leite", "óleo"]

item = input("Digite o item que você deseja retirar: ")

# achou = False

# # if e in estoque:
# #     if estoque == e:
# #         achou = True
# #         break

# # if achou == True:
# #     print("Produto em estoque.")



if item in estoque:
    print("Produto em estoque.")
else:
    print:(f"O item digitado não está em estoque.")

estoque.sort()