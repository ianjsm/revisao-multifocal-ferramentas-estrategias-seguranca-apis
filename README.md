# Título projeto 
Revisão Multifocal sobre ferramentas de teste e estratégias de segurança de APIs em microsserviços 

# Resumo
A comunicação em arquiteturas de microsserviços tem se tornado cada vez mais comum, exigindo atenção aos testes de segurança para garantir a qualidade das APIs. Este estudo, através de uma revisão multifocal, investigou ferramentas e estratégias de segurança aplicadas ao desenvolvimento de APIs. Foram analisados 50 artigos da literatura branca e 270 da cinza. As ferramentas mais citadas foram RESTest (6), OWASP ZAP (6) e Postman (4). Entre as estratégias, destacaram-se Spring Security (93), JWT (81) e API Gateway (37). Os principais testes envolvem validação de entrada (20), detecção de vulnerabilidades (19) e autenticação/autorização (14), com foco em mitigar ameaças como SQL Injection (11), falhas de configuração (10) e OWASP Top Ten (8).
# Objetivo do artefato
Este artefato tem como objetivo disponibilizar os dados coletados, organizados e analisados durante o desenvolvimento da revisão multifocal. O artefato inclui planilhas estruturadas contendo os resultados dos processos de data extraction e avaliação de qualidade aplicados a estudos oriundos da literatura branca, literatura cinza e snowballing. Além disso, inclui um conjunto de gráficos em formato Excel que sintetizam visualmente os principais achados do estudo. O artefato permite que os revisores e demais interessados acessem e compreendam a base empírica que fundamenta as reivindicações do artigo, bem como avaliem a consistência e a completude do processo de análise realizado.
Este artefato tem como objetivo disponibilizar os dados coletados durante a revisão multifocal e fornecer um script para reproduzir de forma automatizada as análises e os gráficos apresentados no artigo. O artefato inclui as planilhas com os dados brutos extraídos, um arquivo de dados consolidado (dados_consolidados.xlsx) e um script em Python (analise.py) que gera todas as figuras do estudo. O artefato permite que os revisores executem a análise, validem a consistência dos dados e reproduzam os resultados que fundamentam as reivindicações do artigo.

# Estrutura do readme.md
- Título do projeto, resumo do projeto e objetivo dos artefatos
@@ -23,58 +23,58 @@ Os selos considerados são: SeloD, SeloF, SeloS e SeloR.

# Informações básicas

Os arquivos do artefato estão no formato .xlsx e podem ser acessados e analisados com qualquer software de planilhas, como Microsoft Excel ou Google Planilhas. Não há necessidade de hardware específico. Recomendado mínimo: 2GB de RAM e acesso à internet para uso da ferramenta Google Planilhas, se necessário.
Este artefato requer um ambiente Python (versão 3.9 ou superior) para a execução do script de análise. Os dados brutos e consolidados estão no formato .xlsx. Não há necessidade de hardware específico, apenas um computador capaz de executar scripts Python.

Software: Python 3.9+, pip (gerenciador de pacotes Python).

Sistema Operacional: Windows.

# Dependências

Os artefatos não possuem dependências externas além de um software capaz de abrir arquivos .xlsx. As análises podem ser realizadas utilizando as ferramentas mencionadas acima, sem necessidade de instalação de bibliotecas ou scripts.
O projeto depende de bibliotecas Python para manipulação de dados e geração de gráficos. Todas as dependências necessárias, com suas versões exatas, estão listadas no arquivo requirements.txt.

A instalação dessas dependências é automatizada e descrita na seção Instalação.

# Preocupações com segurança

Os artefatos não apresentam riscos de segurança. Todos os arquivos fornecidos estão no formato .xlsx, sem uso de scripts ou conteúdo executável.
O artefato não apresenta riscos de segurança. O script analise.py realiza apenas operações locais de leitura de arquivos (.xlsx), processamento de dados e gravação de imagens (.png), sem se conectar à internet, modificar arquivos do sistema ou instalar softwares de terceiros.

# Instalação

1. Acesse o repositório do artefato.
2. Baixe o conteúdo por meio do botão "Code" > "Download ZIP".
3. Extraia (se necessário) e abra os arquivos .xlsx utilizando Microsoft Excel ou Google Planilhas.

# Teste mínimo
Siga os passos abaixo para configurar o ambiente e instalar as dependências.
1. Clone o repositório para sua máquina local:
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
2. Instale as dependências listadas no requirements.txt usando o pip:
    pip install -r requirements.txt

1. Baixe e extraia o repositório.
2. Acesse a pasta Gráficos.
3. Abra o arquivo graficos.xlsx com um software de planilhas.
4. Verifique se os gráficos estão corretamente carregados e visíveis.
Ao final deste processo, o ambiente estará pronto para a execução.

# Experimentos
# Teste mínimo

As análises que embasaram as principais reivindicações do artigo podem ser reproduzidas a partir dos dados contidos nos arquivos .xlsx presentes nas pastas Literatura Branca, Literatura Cinza, Snowballing e Gráficos.
Um teste mínimo consiste em executar o script de análise para verificar se o ambiente e as dependências foram instalados corretamente.

## Reivindicação #1 — Extração e avaliação dos dados dos estudos
Arquivos envolvidos:
- Literatura Branca/Lit. Branca - Data Extraction.xlsx
- Literatura Cinza/Lit. Cinza - Data Extraction.xlsx
- Literatura Branca/Lit. Branca - QA.xlsx
- Literatura Cinza/Lit. Cinza - QA.xlsx
- Snowballing/Snowballing - QA e Data Extraction.xlsx
1. Após a instalação (passo anterior), execute o seguinte comando no terminal, a partir da pasta raiz do projeto:
    python analise.py
2. Resultado esperado: O script deve executar sem erros e exibir mensagens de progresso no terminal, finalizando com "Script finalizado". Uma nova pasta chamada graficos_gerados/ será criada, contendo os arquivos de imagem dos gráficos.

Procedimento:
- Abrir os arquivos nas ferramentas de planilha.
- Verificar os dados extraídos dos estudos e as avaliações de qualidade realizadas.
# Experimentos

Resultado esperado:
- Confirmação da extração dos dados e avaliação da qualidade dos estudos seguindo o processo e os critérios definidos no artigo.
As análises e reivindicações do artigo podem ser reproduzidas de forma totalmente automatizada executando um único script.

## Reivindicação #2 — Análise gráfica dos resultados
Arquivo envolvido:
- Gráficos/Gráficos.xlsx
## Reivindicação #1 — Transparência dos Dados
Os dados brutos que serviram de base para a análise estão disponíveis para inspeção manual nas seguintes pastas: Literatura Branca/, Literatura Cinza/ e Snowballing/. O arquivo dados_consolidados.xlsx na raiz do projeto contém os dados já organizados que são utilizados pelo script.

## Reivindicação #2 — Análise Gráfica dos Resultados (Reprodução Automatizada)
Procedimento:
- Abrir o arquivo e revisar os gráficos gerados a partir das análises anteriores.
- Validar a correspondência entre os gráficos e os resultados descritos no artigo.
1. Certifique-se de que a instalação foi concluída com sucesso.
2. Execute o script principal a partir do diretório raiz do projeto:
    python analise.py

Resultado esperado:
- Confirmação visual dos resultados apresentados no artigo.
- O script irá processar os dados do arquivo dados_consolidados.xlsx.
- Todos os gráficos apresentados no artigo (RQ1-Ferramentas, RQ1-Estratégias, RQ3, RQ4) serão gerados e salvos como arquivos .png na pasta graficos_gerados/.
- A execução do script confirma e reproduz os resultados visuais apresentados no artigo.

# LICENSE
Este artefato está licenciado sob a MIT License.
