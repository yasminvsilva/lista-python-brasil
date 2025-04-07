"""
Exercício 10 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um programa que peça a temperatura em graus Celsius,
transforme e mostre em graus Fahrenheit.

Mostrar apenas valor inteiro da temperatura.

"""

def transformar_para_fahrenheit(celsius):
    fahrenheit = int((celsius * 1.8) + 32)
    print(f"{celsius}°C em Fahrenheit é {fahrenheit} F.")

transformar_para_fahrenheit(float(input("Digite a temperatura (°C): ")))