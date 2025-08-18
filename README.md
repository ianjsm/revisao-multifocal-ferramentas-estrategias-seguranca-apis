# Título projeto
Revisão Multifocal sobre ferramentas de teste e estratégias de segurança de APIs em microsserviços
# Resumo
A comunicação em arquiteturas de microsserviços tem se tornado cada vez mais comum, exigindo atenção aos testes de segurança para garantir a qualidade das APIs. Este estudo, através de uma revisão multifocal, investigou ferramentas e estratégias de segurança aplicadas ao desenvolvimento de APIs. Foram analisados 50 artigos da literatura branca e 270 da cinza. As ferramentas mais citadas foram RESTest (6), OWASP ZAP (6) e Postman (4). Entre as estratégias, destacaram-se Spring Security (93), JWT (81) e API Gateway (37). Os principais testes envolvem validação de entrada (20), detecção de vulnerabilidades (19) e autenticação/autorização (14), com foco em mitigar ameaças como SQL Injection (11), falhas de configuração (10) e OWASP Top Ten (8).

# Objetivo do artefato
Este artefato tem como objetivo disponibilizar os dados coletados durante a revisão multifocal e fornecer um script para reproduzir de forma automatizada as análises e os gráficos apresentados no artigo. O artefato inclui as planilhas com os dados brutos extraídos, um arquivo de dados consolidado (dados_consolidados.xlsx) e um script em Python (analise.py) que gera todas as figuras do estudo. O artefato permite que os revisores executem a análise, validem a consistência dos dados e reproduzam os resultados que fundamentam as reivindicações do artigo.

# Estrutura do readme.md
- Título do projeto, resumo do projeto e objetivo dos artefatos
- Estrutura do repositório
- Selos considerados
- Informações básicas sobre o ambiente
- Dependências
- Preocupações com segurança
- Instalação
- Teste mínimo
- Execução dos experimentos
- Licença

# Selos Considerados

Os selos considerados são: SeloD, SeloF, SeloS e SeloR.

# Informações básicas

Este artefato requer um ambiente Python (versão 3.9 ou superior) para a execução do script de análise. Os dados brutos e consolidados estão no formato .xlsx. Não há necessidade de hardware específico, apenas um computador capaz de executar scripts Python.

- Software: Python 3.9+, pip (gerenciador de pacotes Python).
- Sistema Operacional: Windows.

# Dependências

O projeto depende de bibliotecas Python para manipulação de dados e geração de gráficos. Todas as dependências necessárias, com suas versões exatas, estão listadas no arquivo requirements.txt. A instalação dessas dependências é automatizada e descrita na seção Instalação.

# Preocupações com segurança

O artefato não apresenta riscos de segurança. O script analise.py realiza apenas operações locais de leitura de arquivos (.xlsx), processamento de dados e gravação de imagens (.png), sem se conectar à internet, modificar arquivos do sistema ou instalar softwares de terceiros.

# Instalação

Siga os passos abaixo para configurar o ambiente e instalar as dependências.
1. Verificar se o Python já está instalado
    Abra o terminal e digite:
   ```bash
   python --version
   ```
   - Se a versão instalada for o Python 3.9 ou superior, você pode prosseguir.
   - Caso não esteja instalado ou seja uma versão inferior à mencionada acima, baixe uma versão adequada em: "https://www.python.org/downloads/"

3. Clonar o repositório
    No terminal, execute:
   ```bash
   git clone https://github.com/ianjsm/revisao-multifocal-ferramentas-estrategias-seguranca-apis.git
   cd revisao-multifocal-ferramentas-estrategias-seguranca-apis
   ```

4. Instalar as dependências
    Ainda no terminal, execute:
   ```bash
   pip install -r requirements.txt
   ```
   
Ao final deste processo, o ambiente estará pronto para a execução.

# Teste mínimo

Um teste mínimo consiste em executar o script de análise para verificar se o ambiente e as dependências foram instalados corretamente.

1. Após a instalação (passo anterior), execute o seguinte comando no terminal, a partir da pasta raiz do projeto:
    python analise.py
2. Resultado esperado: O script deve executar sem erros e exibir mensagens de progresso no terminal, finalizando com "Script finalizado". Uma nova pasta chamada "graficos_gerados" será criada, contendo os arquivos de imagem dos gráficos.

# Experimentos

As análises e reivindicações do artigo podem ser reproduzidas de forma totalmente automatizada executando um único script.

## Reivindicação #1 — Transparência dos dados
Os dados brutos que serviram de base para a análise estão disponíveis para inspeção manual nas seguintes pastas: Literatura Branca/, Literatura Cinza/ e Snowballing/. O arquivo dados_consolidados.xlsx na raiz do projeto contém os dados já organizados que são utilizados pelo script.

## Reivindicação #2 — Análise gráfica dos resultados
Procedimento:
1. Certifique-se de que a instalação foi concluída com sucesso.
2. Execute o script principal a partir do diretório raiz do projeto:
    python analise.py

Resultado esperado:
- O script irá processar os dados do arquivo dados_consolidados.xlsx.
- Todos os gráficos apresentados no artigo (RQ1, RQ2, RQ3, RQ4) serão gerados e salvos como arquivos .png na pasta graficos_gerados/.
- A execução do script confirma e reproduz os resultados visuais apresentados no artigo.

# LICENSE

Este artefato está licenciado sob a MIT License.
