"""
Exercício 03 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um programa que verifique se uma letra digitada é "F" ou "M". Retorne:

- F - Feminino;
- M - Masculino;
- Sexo Inválido.

"""

def f_ou_m(sexo):
    if sexo == 'f':
        print("F - Feminino.")
    elif sexo == 'm':
        print("M- Masculino.")
    else:
        print("Sexo inválido.")

f_ou_m(input("Digite o seu sexo (F/M): ").lower())