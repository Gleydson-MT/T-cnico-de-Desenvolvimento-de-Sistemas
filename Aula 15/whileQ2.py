
print(f"Bem vindo ao atendimento online de HYT LTDA.")
while True:
    print(f"""
            
    1. Falar com atendente.
    2. Finalizar contrato.
    3. Abrir nova conta.
    4. Visualizar segunda via da fatura.
    0. Sair
    """)

    resposta = input("Digite a opção desejada: ")
    if resposta == "1":
        print(f"Aguarde um momento...")
    elif resposta == "2":
        print(input("Digite seu CPF: "))
        print(f"Brincadeira, é necessario ir em uma agência fisica. >8-)")
    elif resposta == "3":
        print(f"Seu atendimento será direcionado para um dos nossos atendentes...")
    elif resposta =="4":
        print(f"Um e-mail será enviado para você com mais informações.")
    elif resposta == "0":
        print(f"Encerrando seu atendimento, agradeçemos seu contato.")
        break
    else:
            print("RESPOSTA INVÁLIDA!")
    input("APERTE QUALQUER TECLA PARA CONTINUAR.")