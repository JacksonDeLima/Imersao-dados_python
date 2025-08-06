# Análise e Limpeza de Dados de Salários em TI (Imersão Dados Alura)

Este projeto faz parte da Imersão Dados da Alura e foca na preparação e limpeza de um conjunto de dados sobre salários na área de tecnologia. O script `aula02.py` demonstra diversas técnicas essenciais de manipulação de dados utilizando a biblioteca `pandas` em Python.

## 📜 Descrição

O script carrega um dataset de salários, realiza a tradução das colunas e de valores categóricos para o português, e explora diferentes métodos para tratar dados ausentes (`NaN`). O objetivo é preparar os dados para futuras análises e visualizações.

## ✨ Funcionalidades

O script `aula02.py` executa as seguintes tarefas:

- **Carregamento de Dados**: Lê um arquivo CSV diretamente de um repositório no GitHub.
- **Tradução de Colunas**: Renomeia as colunas do DataFrame do inglês para o português para facilitar a compreensão.
- **Mapeamento de Valores**: Converte valores codificados (ex: 'EN', 'MI', 'SE') em categorias mais descritivas (ex: 'Junior', 'Pleno', 'Sênior'). As colunas tratadas são:
  - `nivel_de_experiencia`
  - `tipo_de_emprego`
  - `tamanho_da_empresa`
  - `proporcao_remoto`
- **Verificação de Dados Nulos**: Utiliza `isnull()`, `isnull().sum()` e `isnull().any()` para identificar a presença e a quantidade de dados ausentes no DataFrame.
- **Demonstração de Tratamento de Dados Ausentes**:
  - **Substituição pela Média/Mediana**: Cria um DataFrame de exemplo para preencher valores `NaN` com a média e a mediana da coluna.
  - **Preenchimento Sequencial (`ffill` e `bfill`)**: Demonstra como preencher dados ausentes com o valor anterior (`ffill`) ou o próximo (`bfill`).
  - **Substituição por Valor Fixo**: Mostra como preencher `NaN` com uma string constante (ex: "Não Informado").
- **Limpeza Final**: Cria uma versão final do DataFrame (`df_limpo`) removendo todas as linhas que contêm qualquer valor nulo.
- **Conversão de Tipos**: Converte o tipo de dado da coluna `ano_de_trabalho` para `int64` para otimizar o uso de memória e garantir a consistência.

## 📊 Dataset

O conjunto de dados utilizado é o `salaries.csv`, disponível no repositório data-jobs de Guilherme Onrails. Ele contém informações sobre salários em diversas áreas de dados ao redor do mundo.

## 🚀 Como Executar

### Pré-requisitos

- Python 3.x
- Bibliotecas `pandas` e `numpy`

### Instalação

1. Clone este repositório ou baixe o arquivo `aula02.py`.
2. Instale as dependências necessárias:
   ```bash
   pip install pandas numpy
   ```

### Execução

Para rodar o script, execute o seguinte comando no seu terminal, dentro da pasta do projeto:

```bash
python aula02.py
```

O script irá imprimir no console os DataFrames em diferentes etapas do processo de limpeza e transformação, demonstrando os resultados de cada operação.