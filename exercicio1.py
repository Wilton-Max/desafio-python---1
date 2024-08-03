#Faça um programa em que o usuário digita dois valores e o resultado da soma é exibido na tela

def somar_valores():
    valor1 = int(input("Informe o primeiro valor: "))
    valor2 = int(input("Informe o segundo valor: "))

    soma = valor1 + valor2

    print(f"A soma de {valor1} e {valor2} é: {soma}")

somar_valores()