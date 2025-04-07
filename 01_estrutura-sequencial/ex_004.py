"""
Exercício 04 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um programa que peça 4 notas bimestrais e mostre a média.

"""

def calcular_media():
    soma = 0

    for i in range(4):
        nota = float(input(f"Digite a {i + 1}ª nota: "))
        soma += nota

    media = soma / 4
    print(f"\nMédia anual: {media}")

calcular_media()