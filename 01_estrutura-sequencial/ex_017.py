"""
Exercício 17 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um programa que peça o tamanho de um arquivo para download (em MB) e
a velocidade de um link de internet (em Mbps), calcule e informe o tempo
aproximado de download do arquivo usando este link (em minutos).

Arredonde o tempo em minutos.

"""

def calcular_tempo_de_download(tamanho, velocidade):
    tempo_segundos = (tamanho * 8) / velocidade
    tempo_minutos = tempo_segundos / 60

    print(f"\nO seu download será concluído em {round(tempo_minutos)} minutos.")

calcular_tempo_de_download(float(input("Digite o tamanho do arquivo (MB): ")),
                           float(input("Digite a velocidade do link (Mbps): ")))
