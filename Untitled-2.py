# Disciplina : Linguagem e Lógica de Programação
# Professor  : Antonio Carlos Nicolodi
# Descrição  : Controle de saldo com compras em loop
# Autor(a)   : Nome do(a) aluno(a)
# Data       : 05/05/2026

saldo = 500.0 

while saldo >= 0:
    compra= float(input("digite o valor da compra:"))
    saldo = saldo - compra
    print(f"saldo atual: R$ {saldo:.2f}/N")

print(f"/saldo negativo atingido: R$ {saldo:.2f}")
    