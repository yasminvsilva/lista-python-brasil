"""
Exercício 02 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um programa que peça um número e então mostre a mensagem:
O número informado foi [número].

"""

def escreva_um_numero(num):
    print(f"O número informado foi {num}.")

escreva_um_numero(num = int(input("Informe um número: ")))