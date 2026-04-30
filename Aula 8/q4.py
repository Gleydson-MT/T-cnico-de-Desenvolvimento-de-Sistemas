idade = int(input("Digite sua idade para verificação: "))


if idade <= 17:
    print(f"Você é uma criança.")
    if idade >= 59:
        print(f"Você é um adulto.")
        if idade >= 60:
            print(f"Você é um Sênior.")
else:
    print(f"Você é um aliginigena, idade inválida.")