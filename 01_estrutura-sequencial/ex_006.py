"""
Exercício 06 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um programa que peça o raio de um círculo, calcule e
mostre sua área. Mostrar a área com 4 casas decimais.

Observação: Use o valor de 3.1415 para o valor da constante π.

"""

def calcular_area_de_circulo(raio):
    area = 3.1415 * (raio ** 2)
    print(f"A área do círculo de raio {raio} é: {round(area, 4)}")

calcular_area_de_circulo(float(input("Digite o raio do círculo: ")))