"""
Exercício 12 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo
que calcule seu peso ideal, usando a seguinte fórmula: (72.7 * altura) - 58

Mostrar a área com 1 casa decimal.

"""

def calcular_peso_ideal(altura):
    peso_ideal = (72.7 * altura) - 58
    print(f"Seu peso ideal é: {peso_ideal:.1f}.")

calcular_peso_ideal(float(input("Digite a sua altura: ")))