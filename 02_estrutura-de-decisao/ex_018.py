"""
Exercício 01 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um programa que peça dois números e imprima o maior deles.

"""

def maior_de_dois_numeros(n1, n2):
    if n1 > n2:
        print(f"\n{n1} é maior!")
    else:
        print(f"\n{n2} é maior!")

maior_de_dois_numeros(int(input("Digite um número: ")),
                      int(input("Digite outro número: ")))