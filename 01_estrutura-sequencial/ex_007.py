"""
Exercício 07 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um programa que calcule a área de um quadrado,
em seguida mostre o dobro desta área para o usuário.

Mostrar a área com 2 casas decimais.

"""

def calcular_area_de_quadrado(lado):
    area = lado * lado
    dobro = area * 2

    print(f"A área do quadrado é: round({area}, 2)")
    print(f"O dobro da área do quadrado é: round({dobro}, 2)")

calcular_area_de_quadrado(float(input("Digite o lado do quadrado: ")))