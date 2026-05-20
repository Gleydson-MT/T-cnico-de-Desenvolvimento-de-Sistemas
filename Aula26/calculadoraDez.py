#Calculadora de 10%. Crie uma função que recebe o valor de uma conta, use o valor dessa conta para calcular a gorgeta(10%) e o valor final da conta (total + gorgeta) e imprima na tela uma nota que o usuário terá que pagar.


def caculadora_de_dez_por_cento(valor_conta):
    gorjeta = valor_conta * 0.1
    valor_final = valor_conta + gorjeta

    print(f""""

============== NOTA FISCAL ==============         

VALOR DA CONTA: R$ {valor_conta:,.2f}
GORJETA (10%): R$ {gorjeta:,.2f}


TOTAL A PAGAR: R$: {valor_final:,.2f}  
          """)
    

#Calculadora de gorjeta. Crie uma função que receba as informações valor da conta e porcentagem da gorjeta, a função deverá retornar o valor total a ser pago pelo cliente, imprima na tela.

def calcular_gorgeta_personalizada(valor_conta, pct_gorgeta):
    gorgeta = valor_conta * pct_gorgeta

    valor_total = valor_conta + gorgeta

    return valor_total

#Crie uma função de calculadora. Essa função deve receber as informações num1, num2 e operação, essa função devera retornar o resultado da operação escolhida. Imprima o resultado de 5 operações com essa ferramenta. P.S.: Lembre de verificar divisões por 0 e forneça o resultado adequado.

def calcular_operacoes(num1, operacao, num2):
    resultado = 0

    if operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado = num1 - num2
    elif operacao == "*":
        resultado = num1 * num2
    elif operacao == "/":
        if num2 == 0:
            resultado = "TENTATIVA DE DIVISÃO POR 0"
        else:
            resultado = num1 / num2
    else:
        resultado = "OPERAÇÃO INVÁLIDA"

    return resultado

print(calcular_operacoes(10, "/", 2))