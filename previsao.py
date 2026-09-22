import pandas as pd
import matplotlib.pyplot as plt

# Criando uma base de dados linear simples
dados = {
    'Minutos': [10, 20, 30, 40, 50],
    'Calorias': [100, 200, 300, 400, 500]
}

df = pd.DataFrame(dados)

# Visualizando a relação linear
print("Tabela de Progressão Linear:")
print(df)

# Se 10 minutos = 100 calorias, qual a função matemática aqui?
# Resposta: Calorias = Minutos * 10
previsao_60_min = 60 * 10
print(f"\nPrevisão: Em 60 minutos, você queimará {previsao_60_min} calorias.")

# Visualizando a relação com um gráfico
plt.scatter(df['Minutos'], df['Calorias'], color='blue')
plt.plot(df['Minutos'], df['Calorias'], color='lightblue')
plt.title('Relação entre Minutos e Calorias')
plt.xlabel('Minutos')
plt.ylabel('Calorias')
plt.grid()
plt.show()