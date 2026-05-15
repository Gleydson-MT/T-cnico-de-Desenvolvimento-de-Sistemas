# coletar informações 
# colocar na lista

lista = []


#(1.Passo) Cadastrar — ler os dados do usuário, montar o dicionário e adicionar à lista.

# Atributos: nome do pet, espécie, raça, idade, nome do tutor

# Listar todos — exibir todos os registros de forma numerada
# Ver detalhes — mostrar todos os campos de um registro específico escolhido pelo número
# Sair — encerrar o programa



while True:
    print("""
------------------GERENCIAMENTO DE CADASTRO------------------
Menu de Opções:
          1 - Cadastra Pet
          2 - Listar todos
          3 - Ver detalhes
          4 - Pesquisa por espécie

          0 - Sair

""")
    

    op = input("Digite o número da opção desejada: ")

    if op == "1":
        print("CADASTRO DE PET")

        nome_do_pet = input("Digite o nome do pet: ")
        especie = input("Digite a espécie: ")
        raca = input("Digite a raça do animal: ")
        while True:
            idade = input("Digite a idade do animal: ")
            if not idade.isdigit():
                print("IDADE ÍNVALIDA")
            else:
                break
        nome_do_tutor = input("Nome do tutor: ")

        novo_cadastro = {
            "Nome do Pet": nome_do_pet,
            "Espécie": especie,
            "Raça": raca,
            "Idade": idade,
            "Nome do tutor": nome_do_tutor
        }
        lista.append(novo_cadastro)
    elif op == "2":
        print("=========LISTA DE PETS=========")
        contador = 1
        for pet in lista:
            print(f"{contador}- {pet["Nome do Pet"]}")
            contador += 1

    if op == "3":
        print("=========LISTA DE PETS=========")
        contador = 1
        for pet in lista:
            print(f"{contador} - {pet["Nome do Pet"]} - {pet["Nome do tutor"]}")
            contador += 1

        resposta = int(input("Digite o número da opção desejada para mais informações: (0=Cancelar): "))

        if resposta == "0":
            print("Cancelando operação......")
        else:
            opcao_escolhida = lista[resposta-1]

        print(f"""
FICHA DOS PETS CADASTRADOS:
              
        Nome: {opcao_escolhida["Nome do Pet"]}
        Espécie: {opcao_escolhida["Espécie"]}
        Raça: {opcao_escolhida["Raça"]}
        Idade: {opcao_escolhida["Idade"]}
        Nome do tutor: {opcao_escolhida["Nome do tutor"]}

""")
        

    elif op == "4":
        print("LISTA DE PETS POR ESPÉCIE")
        contador = 1

        escolha =(input("Digite a espécie para consultar os nomes: (0 Para cancelar.)"))
        for pet in lista:
            if escolha == pet["Espécie"]:
                print(f"{contador} - {pet["Nome do Pet"]} ")
                contador += 1 

    elif op == "0":
        print("ENCERRANDO O PROGRAMA")
        break

else:
    print("DIGITE UMA OPÇÃO VÁLIDA")

    input("DIGITE ENTER PARA CONTINUAR")