"""
Exercício 05 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um programa que converta metros para centímetros.

"""

def converter_metros_para_centimetros(metros):
    centimetros = metros * 100
    print(f"{metros} metros são {centimetros} centímetros.")

converter_metros_para_centimetros(float(input("Digite os metros: ")))