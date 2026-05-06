# Disciplina : Linguagem e Lógica de Programação
# Professor  : Antonio Carlos Nicolodi
# Descrição  : Controle de saldo com compras em loop
# Autor(a)   : Nome do(a) aluno(a)
# Data       : 05/05/2026

saldo = 500.0

while saldo >= 0:
    compra = float(input("Digite o valor da compra: "))
    saldo = saldo - compra
    print(f"Saldo atual: R$ {saldo:.2f}\n")

print(f"\nSaldo negativo atingido: R$ {saldo:.2f}")
