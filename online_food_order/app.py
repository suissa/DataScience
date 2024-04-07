import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo CSV
df = pd.read_csv('onlinefoods.csv')  # Substitua 'caminho_para_seu_arquivo.csv' pelo caminho real do seu arquivo

# Contar os valores na coluna 'Gender'
gender_counts = df['Gender'].value_counts()

# Calcular a porcentagem de cada gênero
gender_percentage = (gender_counts / gender_counts.sum() * 100).round(2)

# Exibir a contagem e a porcentagem de cada gênero
print("Contagem de Gênero:")
print(gender_counts)
print("\nPorcentagem de Gênero:")
print(gender_percentage)

# Criar um gráfico de barras para as porcentagens de gênero
gender_percentage.plot(kind='bar', color=['blue', 'pink'])

# Configurar o título e os rótulos dos eixos
plt.title('Porcentagem de Gênero')
plt.xlabel('Gênero')
plt.ylabel('Porcentagem (%)')
plt.xticks(rotation=0)  # Mantém os rótulos dos eixos x horizontais

# Mostrar o gráfico
plt.show()