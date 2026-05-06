saldo = 500.0

while saldo >= 0:
    try:
        compra = float(input("digite o valor da compra:"))
        saldo = saldo - compra
        print(f"saldo atual: R$ {saldo:.2f}\n")
    except ValueError:
        print("valor invalido!! Digite apenas números, Ex: 49.90")
        continue

print(f"\nSaldo negativo atingido: R$ {saldo:.2f}")

600