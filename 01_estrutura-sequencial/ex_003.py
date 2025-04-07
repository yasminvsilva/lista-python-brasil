"""
Exercício 03 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um programa que peça dois números inteiros e imprima a soma.

"""

def imprima_a_soma_de_dois_numeros(n1, n2):
    print(f"\nA soma dos dois números informados é: {n1 + n2}")

imprima_a_soma_de_dois_numeros(int(input("Digite o primeiro número: ")),
                               int(input("Digite o segundo número: ")))