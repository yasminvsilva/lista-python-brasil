"""
Exercício 09 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um programa que peça a temperatura em graus Fahrenheit,
transforme e mostre a temperatura em graus Celsius.

Fórmula: C = 5 * ((F-32) / 9)
Mostrar apenas valor inteiro da temperatura.

"""

def transformar_para_celsius(fahrenheit):
    celsius = int(5 * ((fahrenheit - 32) / 9))
    print(f"{fahrenheit} F em graus celsius é {celsius}°C.")

transformar_para_celsius(float(input("Digite a temperatura (F): ")))