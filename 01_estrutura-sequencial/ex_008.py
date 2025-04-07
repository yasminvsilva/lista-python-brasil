"""
Exercício 08 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

Mostrar salário com duas casas decimais.

"""

def calcular_salario(valor_hora, horas_trabalhadas):
    salario = valor_hora * horas_trabalhadas
    print(f"\nSeu salário desse mês é R$ {salario:.2f}.")

calcular_salario(float(input("Digite quanto você ganha por hora: ")),
                 int(input("Digite o número de horas que você trabalha no mês: ")))