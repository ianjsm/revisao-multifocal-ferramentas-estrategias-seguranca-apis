import pandas as pd
import matplotlib.pyplot as plt
import os

print("Iniciando o script de análise e geração de gráficos...")

# --- Configuração ---
arquivo_excel = 'dados_consolidados.xlsx'
pasta_saida = 'graficos_gerados/'

if not os.path.exists(pasta_saida):
    os.makedirs(pasta_saida)

# --- Geração dos Gráficos (Lendo de cada aba) ---

# ===================================================================
# GRÁFICO 1: A partir da aba 'RQ1_Ferramentas'
# ===================================================================
try:
    print("Gerando gráfico para RQ1_Ferramentas...")
    df_rq1_f = pd.read_excel(arquivo_excel, sheet_name='RQ1_Ferramentas').set_index('Ferramenta')
    df_rq1_f.fillna(0, inplace=True) # Converte valores vazios/NaN para 0

    # 2. Cria o gráfico de barras EMPILHADAS
    ax = df_rq1_f.plot(kind='bar', stacked=True, figsize=(12, 8), width=0.8)

    for container in ax.containers:
        # Filtra para não mostrar o rótulo se o valor for 0
        ax.bar_label(container, fmt='%.0f', label_type='center', fontsize=10, color='white', weight='bold')

    plt.title('Ferramentas Citadas na Literatura (RQ1)')
    plt.ylabel('Número de Citações')
    plt.xlabel('')
    # 1. Nomes das colunas na VERTICAL
    plt.xticks(rotation=90)
    ax.margins(y=0.1)
    plt.tight_layout()

    caminho_salvar = os.path.join(pasta_saida, 'figura_RQ1_ferramentas.png')
    plt.savefig(caminho_salvar)
    plt.close()
    print(f"Gráfico salvo em '{caminho_salvar}'")

except Exception as e:
    print(f"ERRO ao gerar gráfico para RQ1_Ferramentas: {e}")

# ===================================================================
# GRÁFICO 2: A partir da aba 'RQ1_Estrategias'
# ===================================================================
try:
    print("Gerando gráfico para RQ1_Estrategias...")
    df_rq1_e = pd.read_excel(arquivo_excel, sheet_name='RQ1_Estrategias').set_index('Estrategia')
    df_rq1_e.fillna(0, inplace=True)

    # 2. Cria o gráfico de barras EMPILHADAS
    ax = df_rq1_e.plot(kind='bar', stacked=True, figsize=(12, 8), width=0.8)
    
    for container in ax.containers:
        ax.bar_label(container, fmt='%.0f', label_type='center', fontsize=10, color='white', weight='bold')

    plt.title('Estratégias Citadas na Literatura (RQ1)')
    plt.ylabel('Número de Citações')
    plt.xlabel('')
    # 1. Nomes das colunas na VERTICAL
    plt.xticks(rotation=90)
    ax.margins(y=0.1)
    plt.tight_layout()

    caminho_salvar = os.path.join(pasta_saida, 'figura_RQ1_estrategias.png')
    plt.savefig(caminho_salvar)
    plt.close()
    print(f"Gráfico salvo em '{caminho_salvar}'")

except Exception as e:
    print(f"ERRO ao gerar gráfico para RQ1_Estrategias: {e}")

# ===================================================================
# GRÁFICO 3: A partir da aba 'RQ3'
# ===================================================================
try:
    print("Gerando gráfico para RQ3...")
    df_rq3 = pd.read_excel(arquivo_excel, sheet_name='RQ3').set_index('Categoria')
    df_rq3.fillna(0, inplace=True)

    # 2. Cria o gráfico de barras EMPILHADAS
    ax = df_rq3.plot(kind='bar', stacked=True, figsize=(12, 8), width=0.8)

    for container in ax.containers:
        ax.bar_label(container, fmt='%.0f', label_type='center', fontsize=10, color='white', weight='bold')

    plt.title('Categorias de Análise (RQ3)')
    plt.ylabel('Número de Citações')
    plt.xlabel('')
    # 1. Nomes das colunas na VERTICAL
    plt.xticks(rotation=90)
    ax.margins(y=0.1)
    plt.tight_layout()

    caminho_salvar = os.path.join(pasta_saida, 'figura_RQ3.png')
    plt.savefig(caminho_salvar)
    plt.close()
    print(f"Gráfico salvo em '{caminho_salvar}'")

except Exception as e:
    print(f"ERRO ao gerar gráfico para RQ3: {e}")

# ===================================================================
# GRÁFICO 4: A partir da aba 'RQ4'
# ===================================================================
try:
    print("Gerando gráfico para RQ4...")
    df_rq4 = pd.read_excel(arquivo_excel, sheet_name='RQ4').set_index('Vulnerabilidade')
    df_rq4.fillna(0, inplace=True)

    # 2. Cria o gráfico de barras EMPILHADAS
    ax = df_rq4.plot(kind='bar', stacked=True, figsize=(12, 8), width=0.8)
    
    for container in ax.containers:
        ax.bar_label(container, fmt='%.0f', label_type='center', fontsize=10, color='white', weight='bold')

    plt.title('Vulnerabilidades Exploradas (RQ4)')
    plt.ylabel('Número de Citações')
    plt.xlabel('')
    # 1. Nomes das colunas na VERTICAL
    plt.xticks(rotation=90)
    ax.margins(y=0.1)
    plt.tight_layout()

    caminho_salvar = os.path.join(pasta_saida, 'figura_RQ4.png')
    plt.savefig(caminho_salvar)
    plt.close()
    print(f"Gráfico salvo em '{caminho_salvar}'")

except Exception as e:
    print(f"ERRO ao gerar gráfico para RQ4: {e}")

print(f"\nScript finalizado. Gráficos gerados na pasta '{pasta_saida}'.")