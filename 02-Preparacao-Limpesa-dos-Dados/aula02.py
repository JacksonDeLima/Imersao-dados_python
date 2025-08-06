import pandas as pd
import numpy as np


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

# Dicionários para traduzir os valores das colunas
traducao_nivel_experiencia = {
    'EN': 'Junior',
    'MI': 'Pleno',
    'SE': 'Sênior',
    'EX': 'Executivo'
}
traducao_tipo_emprego = {
    'FT': 'Tempo Integral',
    'PT': 'Meio Período',
    'CT': 'Contrato',
    'FL': 'Freelancer'
}
traducao_tamanho_empresa = {
    'S': 'Pequena',
    'M': 'Média',
    'L': 'Grande'
}
traducao_proporcao_remoto = {
    0: 'Presencial',
    50: 'Híbrido',
    100: 'Remoto'
}

df['nivel_de_experiencia'] = df['nivel_de_experiencia'].replace(traducao_nivel_experiencia)
df['tipo_de_emprego'] = df['tipo_de_emprego'].replace(traducao_tipo_emprego)
df['tamanho_da_empresa'] = df['tamanho_da_empresa'].replace(traducao_tamanho_empresa)
df['proporcao_remoto'] = df['proporcao_remoto'].replace(traducao_proporcao_remoto)


print (df.isnull())
print ("============================================")
print (df.head())
print ("============================================")
print (df.isnull().sum())
print ("============================================")
print(df['ano_de_trabalho'].unique())
print ("============================================")
print (df[df.isnull().any(axis=1)])
print ("============================================")

# Criando um DataFrame de exemplo para calcular a média e mediana
df_salarios = pd.DataFrame({
    "nome": ['Guilherme', 'Maria', 'João', 'Daniela'],
    "salario": [5000, np.nan, 7000, np.nan]
})
# Calaculando a média salarial e substituindo os valores NaN pela média e arredonda os valores para duas casas decimais
df_salarios['salario_media'] = df_salarios['salario'].fillna(df_salarios['salario'].mean().round(2))

# Calaculando a mediana salarial e substituindo os valores NaN pela mediana e arredonda os valores para duas casas decimais
df_salarios['salario_mediana'] = df_salarios['salario'].fillna(df_salarios['salario'].median().round(2))

print(df_salarios)
print ("============================================")
df_temperaturas = pd.DataFrame({
    "Dia": ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta'],
    "Temperatura": [22.5, 23.0, np.nan, 24.5, 25.0]                                 
    })

df_temperaturas["preenchido_ffill"] = df_temperaturas["Temperatura"].ffill()
df_temperaturas["preenchido_bfill"] = df_temperaturas["Temperatura"].bfill()

print(df_temperaturas)
print ("============================================")

df_cidades = pd.DataFrame({
    "nome": ['Ana', 'Bruno', 'Carlos', 'Daniele', 'Val'],
    "cidade": ['São Paulo', 'Rio de Janeiro', np.nan, 'Belo Horizonte', 'Curitiba'],
})

df_cidades['cidade_preenchida'] = df_cidades['cidade'].fillna("Não Informado")
    
print(df_cidades)
print ("============================================")

df_limpo = df.dropna()  # Remove linhas com qualquer valor NaN
df_limpo.isnull().sum()  # Verifica se ainda há valores NaN
print(df_limpo)
print ("============================================")
print(df_limpo.info())
print ("============================================")

df_limpo = df_limpo.assign(ano_de_trabalho = df_limpo['ano_de_trabalho'].astype('int64'))
print(df_limpo)

print ("============================================")