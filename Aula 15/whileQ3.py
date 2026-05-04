qnt_notas_validas = 0

soma_notas = 0

while True:
    nota = float(input("Digite uma nota entre 0 e 10: "))

    if nota < 0 or nota > 10:
        print("Nota inválida... Digite novamente...")
        continue

    qnt_notas_validas += 1
    soma_notas += nota

    if qnt_notas_validas >=4:
        break

media = soma_notas/qnt_notas_validas

print(f"Média: {media}")

if media >=7 and media <=10:
    print("APROVADO")

elif media >=4 and media <7:
    print("RECUPERAÇÃO")
elif media >=0 and media <4 :
    print("REPROVADO")

else:
    print("De alguma maneira a média é inválida")