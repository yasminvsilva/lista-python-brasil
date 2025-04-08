"""
Exercício 13 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Tendo como dado de entrada a altura (h) de uma pessoa, construa
um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

Para homens: (72.7 * h) - 58
Para mulheres: (62.1 * h) - 44.7

Mostrar a área com 1 casa decimal.

"""

def calcular_peso_ideal(altura):
    peso_ideal_homem = (72.7 * altura) - 58
    peso_ideal_mulher = (62.1 * altura) - 44.7

    print(f"\nSeu peso ideal é {peso_ideal_homem:.1f}, se você for homem.")
    print(f"Seu peso ideal é {peso_ideal_mulher:.1f}, se você for mulher.")

calcular_peso_ideal(float(input("Digite a sua altura: ")))