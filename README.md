Este repositório contém um projeto de análise de dados utilizando Python, Streamlit e Plotly. O objetivo do projeto é carregar e visualizar dados de um arquivo Excel, além de responder a algumas perguntas específicas sobre os dados.

Ele foi usado no curso de git da Comunidade DS

## Estrutura do Repositório

- app.py: Arquivo principal que inicializa a aplicação Streamlit e carrega os dados.
- src: Diretório contendo os módulos de extração e análise de dados.
  - extraction.py: Contém a função `load_data` que carrega os dados do arquivo Excel.
  - answers.py: Contém funções para responder a perguntas específicas sobre os dados e gerar visualizações.
- data: Diretório contendo o arquivo de dados escolaridade-2022-2023.xlsx.
- requirements.txt: Lista de dependências necessárias para executar o projeto.
- ComandosGit.md: Documento com comandos básicos e avançados do Git para gerenciamento do repositório.

## Como Executar

1. Clone o repositório:
   ```sh
   git clone <URL_DO_REPOSITORIO>
   ```
2. Navegue até o diretório do projeto:
   ```sh
   cd <NOME_DO_DIRETORIO>
   ```
3. Crie um ambiente virtual e ative-o:
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # No Windows, use .venv\Scripts\activate
   ```
4. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```
5. Execute a aplicação:
   ```sh
   streamlit run app.py
   ```

## Funcionalidades

- Carregamento de dados de um arquivo Excel.
- Visualização de dados utilizando gráficos interativos com Plotly.
- Respostas a perguntas específicas sobre os dados, como contagem de tipos de vendedores e análise de preços.

## Comandos Git

O arquivo ComandosGit.md contém uma lista de comandos úteis para gerenciar o repositório Git, incluindo como iniciar um repositório, adicionar arquivos, fazer commits, visualizar histórico de commits e realizar rebase interativo.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorias e correções.

## Licença

Este projeto está licenciado sob a MIT License.