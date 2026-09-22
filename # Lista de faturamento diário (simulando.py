# Lista de faturamento diário (simulando uma coluna de dados)
faturamento = [1500, 2300, 800, 4500, 1200, 3100, 500]

# 1. Calcular o faturamento total usando a função sum()
# A função sum() soma todos os valores da lista
total = sum(faturamento)

# 2. Calcular a média de faturamento
# len() retorna a quantidade de elementos na lista
quantidade = len(faturamento)

# A média é o total dividido pela quantidade de dias
media = total / quantidade

# 3. Exibir o relatório de desempenho
print("Relatório de Performance:")
print(f"Faturamento Total: R$ {total:.2f}")  # Mostra o total com 2 casas decimais
print(f"Média Diária: R$ {media:.2f}")       # Mostra a média com 2 casas decimais
print("-" * 30)  # Linha separadora

# 4. Usar um laço FOR para analisar cada dia
# O FOR percorre cada valor dentro da lista faturamento
for valor in faturamento:
    
    # Verifica se o valor é maior que a média
    if valor > media:
        # Se for maior, é considerado um destaque positivo
        print(f"Destaque Positivo: R$ {valor} (Acima da média)")
    else:
        # Caso contrário, é um dia normal
        print(f"Dia Normal: R$ {valor}")