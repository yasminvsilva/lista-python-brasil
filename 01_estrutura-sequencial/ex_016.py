"""
Exercício 16 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um programa para uma loja de tintas.

O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe
ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

"""

def calcular_latas_e_preco_de_tinta(area):
    litros = area / 3
    latas = litros / 18

    if latas != int(latas):
        latas = int(latas) + 1
    else:
        latas = int(latas)

    preco = latas * 80

    print(f"Você deve comprar {round(latas, 2)} lata(s) de tinta no custo de R$ {preco:.2f}.")

calcular_latas_e_preco_de_tinta(float(input("Digite o tamanho da área (m²): ")))