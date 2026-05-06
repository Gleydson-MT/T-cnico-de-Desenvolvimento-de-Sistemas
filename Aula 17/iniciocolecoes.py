#Crie um programa que recebe uma palavra. Imprima a úlitma letra dessa palavra.

palavra = "Santander"
#Usar o len() para descobrir o tamanho de uma coleção.
print(palavra[8])

#Crie um programa que recebe uma palavra. Imforme se a palavra começa com vogal ou consoante.

palavra_dois = "Dezembro"
#in == "Entre"
if palavra_dois[0].lower() in "aeiou":
    print(f"{palavra_dois}, começa com uma vogal.")
elif palavra_dois[0].isdigit(): # ou palavra_dois[0] in "0123456789":
    print("Começa com número.")
else:
    print(f"Essa palavra começa com uma consoante.")

#Crie um programa que recebe uma palavra. Imprima todas os caracteres dessa palavra, linha por linha.

palavra_tres = "Melhor"

for i in range(len(palavra_tres)):
    print(palavra_tres[i])

texto = "Armagedom, bom filme"

qtd_letra = 0

for letra in texto:
    if letra in "aeiou":
        qtd_letra += 1
print(qtd_letra)
