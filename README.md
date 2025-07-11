# Título projeto
Revisão Multifocal sobre ferramentas de teste e estratégias de segurança de APIs em microsserviços
# Resumo
A comunicação em arquiteturas de microsserviços tem se tornado cada vez mais comum, exigindo atenção aos testes de segurança para garantir a qualidade das APIs. Este estudo, através de uma revisão multifocal, investigou ferramentas e estratégias de segurança aplicadas ao desenvolvimento de APIs. Foram analisados 50 artigos da literatura branca e 270 da cinza. As ferramentas mais citadas foram RESTest (6), OWASP ZAP (6) e Postman (4). Entre as estratégias, destacaram-se Spring Security (93), JWT (81) e API Gateway (37). Os principais testes envolvem validação de entrada (20), detecção de vulnerabilidades (19) e autenticação/autorização (14), com foco em mitigar ameaças como SQL Injection (11), falhas de configuração (10) e OWASP Top Ten (8).
# Objetivo do artefato
Este artefato tem como objetivo disponibilizar os dados coletados, organizados e analisados durante o desenvolvimento da revisão multifocal. O artefato inclui planilhas estruturadas contendo os resultados dos processos de data extraction e avaliação de qualidade aplicados a estudos oriundos da literatura branca, literatura cinza e snowballing. Além disso, inclui um conjunto de gráficos em formato Excel que sintetizam visualmente os principais achados do estudo. O artefato permite que os revisores e demais interessados acessem e compreendam a base empírica que fundamenta as reivindicações do artigo, bem como avaliem a consistência e a completude do processo de análise realizado.

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

Os arquivos do artefato estão no formato .xlsx e podem ser acessados e analisados com qualquer software de planilhas, como Microsoft Excel ou Google Planilhas. Não há necessidade de hardware específico. Recomendado mínimo: 2GB de RAM e acesso à internet para uso de ferramentas online, se necessário.

# Dependências

Os artefatos não possuem dependências externas além de um software capaz de abrir arquivos .xlsx. As análises podem ser realizadas utilizando as ferramentas mencionadas acima, sem necessidade de instalação de bibliotecas ou scripts.

# Preocupações com segurança

Os artefatos não apresentam riscos de segurança. Todos os arquivos fornecidos estão no formato .xlsx, sem uso de scripts ou conteúdo executável.

# Instalação

1. Acesse o repositório do artefato.
2. Baixe o conteúdo por meio do botão "Code" > "Download ZIP".
3. Extraia (se necessário) e abra os arquivos .xlsx utilizando Microsoft Excel ou Google Planilhas.

# Teste mínimo

1. Baixe e extraia o repositório.
2. Acesse a pasta Graficos.
3. Abra o arquivo graficos.xlsx com um software de planilhas.
4. Verifique se os gráficos estão corretamente carregados e visíveis.

# Experimentos

As análises que embasaram as principais reivindicações do artigo podem ser reproduzidas a partir dos dados contidos nos arquivos .xlsx presentes nas pastas Literatura Branca, Literatura Cinza, Snowballing e Gráficos.

## Reivindicação #1 — Extração e avaliação dos dados dos estudos
Arquivos envolvidos:
- Literatura Branca/Lit. Branca - Data Extraction.xlsx
- Literatura Cinza/Lit. Cinza - Data Extraction.xlsx
- Literatura Branca/Lit. Branca - QA.xlsx
- Literatura Cinza/Lit. Cinza - QA.xlsx
- Snowballing/Snowballing - QA e Data Extraction.xlsx

Procedimento:
- Abrir os arquivos nas ferramentas de planilha.
- Verificar os dados extraídos dos estudos e as avaliações de qualidade realizadas.

Resultado esperado:
- Confirmação da extração dos dados e avaliação da qualidade dos estudos seguindo o processo e os critérios definidos no artigo.

## Reivindicação #2 — Análise gráfica dos resultados
Arquivo envolvido:
- Gráficos/Gráficos.xlsx

Procedimento:
- Abrir o arquivo e revisar os gráficos gerados a partir das análises anteriores.
- Validar a correspondência entre os gráficos e os resultados descritos no artigo.

Resultado esperado:
- Confirmação visual dos resultados apresentados no artigo.

# LICENSE

Este artefato está licenciado sob a MIT License.
