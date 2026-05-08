#2. Fila de atendimento
#Uma clínica tem uma fila com so nomes: ["Carlos", "Beatriz", "Fábio", "Juliana", "Rafael"]. Adicione "Tatiane" ao final da fila e remova "Fábio" porque ele desistiu. Exiba a fila atualizada e o total de pessoas.

fila = ["Carlos", "Beatriz", "Fábio", "Juliana", "Rafael"]
posicao = 1
fila.append("Tatiane")
if "Fábio" in fila:
    fila.remove("Fábio")
else:
    print("PACIENTE NÃO ENCONTRADO")

for p in fila:
    print(f"{posicao}. {p}")
    posicao += 1

print(f"Total de pacientes:{len(fila)}")