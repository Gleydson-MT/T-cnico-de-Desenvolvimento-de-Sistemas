while True:
    num = int(input("Digite o primeiro número: "))
    operacao = input("Informe a operação (+, -, *, /): ")
    num2 = int(input("Digite o segundo número: "))
    resultado = 0
    
    if operacao == "+":
        resultado = num + num2
    elif operacao == "-":
        resultado = num - num2
    elif operacao == "*":
        resultado = num * num2
    elif operacao == "/":
        if num2 == "0":
            resultado == "TENTATIVA DE DIVISÃO POR 0"
        else:
            resultado = num / num2
    else:
        print(f"Operação inválida!")
    print(f"O resultado é ({num} {operacao} {num2} = {resultado}).")
    resposta = input("Deseja continuar? (Sim) ou (Não).: ")
    if resposta == "Sim":
        continue
    else:
        print(f"Encerrando calculadora.")
        break


