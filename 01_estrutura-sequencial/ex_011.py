"""
Exercício 11 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um programa que peça 2 números inteiros e um número real.
Calcule e mostre:

1) o produto do dobro do primeiro com metade do segundo;
2) a soma do triplo do primeiro com o terceiro;
3) o terceiro elevado ao cubo.

Apresente os resultados com duas casas decimais.

"""

def calcular_formulas(n1, n2, n3):
    operacao1 = (n1 * 2) + (n2 / 2)
    operacao2 = (n1 * 3) + n3
    operacao3 = n3 ** 3

    print(f"\nO produto do dobro de {n1} com metade de {n2} é: {operacao1:.2f}.")
    print(f"A soma do triplo de {n1} com {n3} é: {operacao2:.2f}.")
    print(f"{n3} elevado ao cubo é: {operacao3:.2f}.")

calcular_formulas(int(input("Digite um número inteiro: ")),
                  int(input("Digite outro número inteiro: ")),
                  float(input("Digite um número real: ")))
