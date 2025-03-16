import pandas as pd
import os

# utilizado para concatenar os objetos criados pelo consumo da API
folder = '' # indicar a pasta onde os arquivos gerados pela API foram armazenados.

# só para testar a leitura do df
#file = 'Despesas_Unifei_01_2014_12_2014.xlsx'

df_list = []
# funcionando
for file in os.listdir(folder):
    patch = f'{folder}/{file}'
    df = pd.read_excel(patch,
                    usecols=['anoMes',
                                'codigoPessoa',
                                'nomePessoa',
                                'tipoPessoa',
                                'municipioPessoa',
                                'siglaUFPessoa',
                                'codigoUG',
                                'nomeUG',
                                'codigoOrgao',
                                'nomeOrgao',
                                'codigoOrgaoSuperior',
                                'nomeOrgaoSuperior',
                                'valor'])
    df_list.append(df)
    print(f'Arquivo {file} lido e df concatenado.')

df_full = pd.concat(df_list, ignore_index=True)
print()
print('Concatenação completa!')

df_full.to_excel('teste_full.xlsx', index_label=False, index=False)
print()
print('Arquivo Excel gerado!')
