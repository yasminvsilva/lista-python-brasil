"""
Exercício 15 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e
5% para o sindicato, faça um programa que nos dê:

- Salário bruto;
- Quanto pagou de IR;
- Quanto pagou ao INSS;
- Quanto pagou ao sindicato;
- Salário líquido.

Calcule os descontos e o salário líquido.
Mostrar os resultados com duas casas decimais.

"""

def calcular_assalto_no_salario(pgto_hora, horas_trabalhadas):
    salario_bruto = pgto_hora * horas_trabalhadas
    imposto_renda = salario_bruto * 0.11
    inss = salario_bruto * 0.08
    sindicato = salario_bruto * 0.05
    salario_liquido = salario_bruto - imposto_renda - inss - sindicato

    print(f"""
+ Salário Bruto: R$ {salario_bruto:.2f}
- IR (11%): R$ {imposto_renda:.2f}
- INSS (8%): R$ {inss:.2f}
- Sindicato (5%): R$ {sindicato:.2f}
= Salário Líquido: R$ {salario_liquido:.2f} """)

calcular_assalto_no_salario(float(input("Digite quanto você ganha por hora: ")),
                            int(input("Digite quantas horas você trabalha por mês: ")))