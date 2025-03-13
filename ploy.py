import pandas as pd
import matplotlib.pyplot as plt

# 1. Ler a planilha
df = pd.read_excel("2.xlsx")

# 2. Selecionar colunas numéricas
numeric_cols = df.select_dtypes(include='number').columns

# 3. Criar subplots (um para cada coluna)
fig, axes = plt.subplots(nrows=len(numeric_cols), figsize=(10, 5 * len(numeric_cols)))

# Se houver só 1 coluna numérica, axes vira um único objeto ao invés de lista
if len(numeric_cols) == 1:
    axes = [axes]

for i, col in enumerate(numeric_cols):
    axes[i].plot(df.index, df[col], marker='o', label=col)
    axes[i].set_title(f'Gráfico de {col}')
    axes[i].set_xlabel('Índice (linhas do DataFrame)')
    axes[i].set_ylabel(col)
    axes[i].legend()
    axes[i].grid(True)

plt.tight_layout()  # Ajusta espaçamento para evitar sobreposição
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# 1. Ler a planilha
df = pd.read_excel("2.xlsx")

# 2. Selecionar as colunas numéricas
numeric_cols = df.select_dtypes(include='number').columns
print("Colunas numéricas encontradas:", numeric_cols.tolist())

# 3. Criar a figura e o eixo (tamanho maior para caber tudo com clareza)
fig, ax = plt.subplots(figsize=(12, 6))

# 4. Plotar cada coluna numérica no mesmo gráfico
for col in numeric_cols:
    ax.plot(df.index, df[col], marker='o', linewidth=1.5, label=col)

# 5. Personalizar o título e os rótulos dos eixos
ax.set_title("Evolução de Todas as Categorias", fontsize=16, fontweight='bold')
ax.set_xlabel("Índice (linhas do DataFrame)", fontsize=12)
ax.set_ylabel("Valores", fontsize=12)

# 6. Ajustar os ticks do eixo X (exemplo: mostrar rótulos de 5 em 5 linhas)
ax.set_xticks(range(0, len(df), 5))

# 7. Ativar linhas de grade (major) e deixar visualmente mais claras
ax.grid(True, which='major', linestyle='--', alpha=0.7)

# 8. Adicionar uma legenda mais organizada, fora do gráfico
ax.legend(
    bbox_to_anchor=(1.05, 1),  # posição (fora, à direita)
    loc='upper left',
    fontsize=10,
    title="Categorias"
)

# 9. Ajustar o layout para acomodar a legenda sem cortar nada
plt.tight_layout()

# 10. Exibir o gráfico
plt.show()
cores = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'pink']
for i, col in enumerate(numeric_cols):
    ax.plot(df.index, df[col], marker='o', color=cores[i % len(cores)], label=col)


