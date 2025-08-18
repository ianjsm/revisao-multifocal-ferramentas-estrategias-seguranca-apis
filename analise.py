import pandas as pd
import matplotlib.pyplot as plt
import os

print("Iniciando o script de análise e geração de gráficos...")

# --- Configuração ---
arquivo_excel = 'dados_consolidados.xlsx'
pasta_saida = 'graficos_gerados/'
# Definindo as cores padrão para os gráficos
# A ordem assume que a primeira coluna no seu Excel é 'Lit. Branca' e a segunda 'Lit. Cinza'
cores_grafico = ['#f3b735', '#3a919d'] 

if not os.path.exists(pasta_saida):
    os.makedirs(pasta_saida)
    print(f"Pasta de saída criada em: '{pasta_saida}'")

# ===================================================================
# GRÁFICO 1: A partir da aba 'RQ1_Ferramentas'
# ===================================================================
try:
    print("Gerando gráfico para RQ1_Ferramentas...")
    df_rq1_f = pd.read_excel(arquivo_excel, sheet_name='RQ1_Ferramentas').set_index('Ferramenta')
    df_rq1_f.fillna(0, inplace=True)

    # Cria o gráfico de barras empilhadas com as cores e tamanho definidos
    ax = df_rq1_f.plot(kind='bar', stacked=True, figsize=(20, 7), width=0.7, color=cores_grafico, legend=False)

    # --- Estilização do Gráfico (Padrão para todos) ---
    # Adiciona os rótulos de dados em cima de cada barra/segmento
    for container in ax.containers:
        # Cria os rótulos, mas deixa uma string vazia para valores zero
        labels = [int(v) if v > 0 else '' for v in container.datavalues]
        ax.bar_label(
            container,
            labels=labels,
            label_type='edge', # Posição na ponta da barra
            fontsize=9,
            color='black',
            padding=3 # Pequeno espaço entre a barra e o texto
        )

    # Remove todos os eixos e bordas para um visual limpo
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax.tick_params(axis='x', length=0) # Remove as marquinhas do eixo X

    # Ajusta o limite do eixo Y para dar espaço aos rótulos no topo
    max_height = df_rq1_f.sum(axis=1).max()
    ax.set_ylim(0, max_height * 1.2)
    
    # Configura os rótulos do eixo X
    plt.xlabel('')
    plt.xticks(rotation=90, fontsize=11)
    
    # Adiciona e posiciona a legenda na parte inferior
    handles, labels = ax.get_legend_handles_labels()
    fig = plt.gcf()
    fig.legend(handles, labels, loc='lower center', bbox_to_anchor=(0.5, 0), ncol=len(df_rq1_f.columns), frameon=False, fontsize=11)
    
    plt.tight_layout(rect=[0, 0.1, 1, 1]) # Ajusta o layout para caber a legenda

    caminho_salvar = os.path.join(pasta_saida, 'figura_RQ1_ferramentas.png')
    plt.savefig(caminho_salvar, bbox_inches='tight', pad_inches=0.1)
    plt.close()
    print(f"Gráfico salvo em '{caminho_salvar}'")

except Exception as e:
    print(f"ERRO ao gerar gráfico para RQ1_Ferramentas: {e}")

# ===================================================================
# GRÁFICO 2: A partir da aba 'RQ1_Estrategias' renomeada para 'RQ2'
# ===================================================================
try:
    # Nota: A imagem enviada se chama RQ2-ESTRATÉGIAS, assumindo que a aba é 'RQ1_Estrategias'
    print("Gerando gráfico para RQ2_Estrategias...")
    df_rq2_e = pd.read_excel(arquivo_excel, sheet_name='RQ2_Estrategias').set_index('Estrategia')
    df_rq2_e.fillna(0, inplace=True)

    ax = df_rq2_e.plot(kind='bar', stacked=True, figsize=(16, 7), width=0.7, color=cores_grafico, legend=False)

    # --- Estilização do Gráfico ---
    for container in ax.containers:
        labels = [int(v) if v > 0 else '' for v in container.datavalues]
        ax.bar_label(container, labels=labels, label_type='edge', fontsize=9, color='black', padding=3)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax.tick_params(axis='x', length=0)

    max_height = df_rq2_e.sum(axis=1).max()
    ax.set_ylim(0, max_height * 1.2)
    
    plt.xlabel('')
    plt.xticks(rotation=90, fontsize=11)
    
    handles, labels = ax.get_legend_handles_labels()
    fig = plt.gcf()
    fig.legend(handles, labels, loc='lower center', bbox_to_anchor=(0.5, 0), ncol=len(df_rq2_e.columns), frameon=False, fontsize=11)
    
    plt.tight_layout(rect=[0, 0.1, 1, 1])

    caminho_salvar = os.path.join(pasta_saida, 'figura_RQ2_estrategias.png')
    plt.savefig(caminho_salvar, bbox_inches='tight', pad_inches=0.1)
    plt.close()
    print(f"Gráfico salvo em '{caminho_salvar}'")

except Exception as e:
    print(f"ERRO ao gerar gráfico para RQ2_Estrategias: {e}")

# ===================================================================
# GRÁFICO 3: A partir da aba 'RQ3'
# ===================================================================
try:
    print("Gerando gráfico para RQ3...")
    df_rq3 = pd.read_excel(arquivo_excel, sheet_name='RQ3').set_index('Categoria')
    df_rq3.fillna(0, inplace=True)

    ax = df_rq3.plot(kind='bar', stacked=True, figsize=(12, 7), width=0.7, color=cores_grafico, legend=False)

    # --- Estilização do Gráfico ---
    for container in ax.containers:
        labels = [int(v) if v > 0 else '' for v in container.datavalues]
        ax.bar_label(container, labels=labels, label_type='edge', fontsize=9, color='black', padding=3)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax.tick_params(axis='x', length=0)

    max_height = df_rq3.sum(axis=1).max()
    ax.set_ylim(0, max_height * 1.2)
    
    plt.xlabel('')
    plt.xticks(rotation=90, fontsize=11)
    
    handles, labels = ax.get_legend_handles_labels()
    fig = plt.gcf()
    fig.legend(handles, labels, loc='lower center', bbox_to_anchor=(0.5, 0), ncol=len(df_rq3.columns), frameon=False, fontsize=11)
    
    plt.tight_layout(rect=[0, 0.1, 1, 1])

    caminho_salvar = os.path.join(pasta_saida, 'figura_RQ3.png')
    plt.savefig(caminho_salvar, bbox_inches='tight', pad_inches=0.1)
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

    ax = df_rq4.plot(kind='bar', stacked=True, figsize=(12, 7), width=0.7, color=cores_grafico, legend=False)

    # --- Estilização do Gráfico ---
    for container in ax.containers:
        labels = [int(v) if v > 0 else '' for v in container.datavalues]
        ax.bar_label(container, labels=labels, label_type='edge', fontsize=9, color='black', padding=3)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax.tick_params(axis='x', length=0)

    max_height = df_rq4.sum(axis=1).max()
    ax.set_ylim(0, max_height * 1.2)
    
    plt.xlabel('')
    plt.xticks(rotation=90, fontsize=11)
    
    handles, labels = ax.get_legend_handles_labels()
    fig = plt.gcf()
    fig.legend(handles, labels, loc='lower center', bbox_to_anchor=(0.5, 0), ncol=len(df_rq4.columns), frameon=False, fontsize=11)
    
    plt.tight_layout(rect=[0, 0.1, 1, 1])

    caminho_salvar = os.path.join(pasta_saida, 'figura_RQ4.png')
    plt.savefig(caminho_salvar, bbox_inches='tight', pad_inches=0.1)
    plt.close()
    print(f"Gráfico salvo em '{caminho_salvar}'")

except Exception as e:
    print(f"ERRO ao gerar gráfico para RQ4: {e}")

print(f"\nScript finalizado. Gráficos gerados na pasta '{pasta_saida}'.")