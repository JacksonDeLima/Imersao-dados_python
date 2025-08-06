import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

# Dicionário para traduzir as colunas para português brasileiro
colunas_traduzidas = {
    'work_year': 'ano_de_trabalho',
    'experience_level': 'nivel_de_experiencia',
    'employment_type': 'tipo_de_emprego',
    'job_title': 'cargo',
    'salary': 'salario',
    'salary_currency': 'moeda_do_salario',
    'salary_in_usd': 'salario_em_usd',
    'employee_residence': 'residencia_do_funcionario',
    'remote_ratio': 'proporcao_remoto',
    'company_location': 'localizacao_da_empresa',
    'company_size': 'tamanho_da_empresa'
}

# Renomeando as colunas do DataFrame
df = df.rename(columns=colunas_traduzidas)

print(df.head())

print("============================================")

print(df.info())

print("============================================")

print(df.describe())

print("============================================")

print(df.shape)

print("============================================")

linhas,  colunas = df.shape[0], df.shape[1]

print(f"Linhas: {linhas}, Colunas: {colunas}")

print("============================================")

print(df.columns)

print("============================================")


print(df["nivel_de_experiencia"].value_counts())

print("============================================")

print(df["tipo_de_emprego"].value_counts())

print("============================================")

print(df["proporcao_remoto"].value_counts())

print("============================================")

print(df["tamanho_da_empresa"].value_counts())

print("============================================")

print(df.describe(include='object'))