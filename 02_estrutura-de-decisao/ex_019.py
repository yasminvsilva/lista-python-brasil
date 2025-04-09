"""
Exercício 02 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um programa que peça um valor e mostre na tela se o valor é
positivo ou negativo. Caso seja igual a 0, retorne None.

"""

def positivo_ou_negativo(num):
    if num < 0:
        print("É negativo!")
    elif num > 0:
        print("É positivo!")
    else:
        print("É zero! Não é positivo nem negativo!")

positivo_ou_negativo(int(input("Digite um número: ")))