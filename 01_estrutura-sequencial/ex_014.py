"""
Exercício 14 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar
o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes
maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50
quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que
você faça um programa que leia a variável peso (peso de peixes) e calcule o
excesso. Gravar na variável excesso a quantidade de quilos além do limite e
na variável multa o valor da multa que João deverá pagar.

Imprima os dados do programa com as mensagens adequadas.
Mostrar o peso e multa com duas casas decimais.

"""

def calcular_peso_excedente_e_multa(peso):
    peso_excedente = peso - 50
    multa = peso_excedente * 4

    print(f"\nO peso excedente de peixes é de {peso_excedente:.2f} kg.")
    print(f"Por isso, a multa é de R$ {multa:.2f}.")

calcular_peso_excedente_e_multa(int(input("Digite a quantidade de peixe (kg): ")))