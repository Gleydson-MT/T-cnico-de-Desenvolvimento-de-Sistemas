# 4. Crie um programa que pede o nome dos funcionários de um departamente até que seja fornecido um funcionário com o nome "SAIR". Exiba quantos funcionários foram cadastrados.

while True:
    nome_func = input("Digite o nome do funcionário: ")

    if nome_func == "SAIR":
        print("SAINDO DO CADASTRO DE FUNCIONÁRIOS")
        break

    qnt_funcionarios += 1

print(f"Funcionários Cadastrados: {qnt_funcionarios}")