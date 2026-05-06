saldo = 500.0

#o laço "while" vai substituir o "enquanto" do portugol

while saldo >= 0:
   print("saldo atual: R$ (saldo:.2f)")

   compra = float(input("valor da compra: R$"))

   saldo = saldo - compra

print(F"saldo insuficiente da conta! seu saldo final ficou em (saldo:2.f)")
