"""
Exercício 04 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um programa que verifique se uma letra digitada é vogal ou consoante.

"""

def vogal_ou_consoante(letra):
    vogais = ['a', 'e', 'i', 'o', 'u']

    if letra.isalpha():
        if letra in vogais:
            print("É vogal!")
        else:
            print("É consoante!")
    else:
        print("Inválido!")

vogal_ou_consoante(input("Informe uma letra: ").lower())