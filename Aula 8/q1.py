num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))

if num1 %2 == 0:
    print("O primero, é um número par.")
else:
    print(f"O primeiro é um número impar.")
if num2 %2 != 0:
    print("O {num2}, é um número impar.")
else:
    print(f"O segundo é um número par.")