import pandas as pd
import requests

# Criar um contador de adições, para não perder de vista o trabalho realizado.

url = 'http://api.portaldatransparencia.gov.br'

api = '/api-de-dados/despesas/recursos-recebidos'

header = {'chave-api-dados':''} # para se ter uma chave de acesso, é necessário se cadastrar no Portal Transparência, na seção de API

# PARAMETROS
# mes_inicio = '01/2014'
# mes_fim = '12/2014'
# mes_inicio = '01/2015'
# mes_fim = '12/2015'
# mes_inicio = '01/2016'
# mes_fim = '12/2016'
# mes_inicio = '01/2017'
# mes_fim = '12/2017'
# mes_inicio = '01/2018'
# mes_fim = '12/2018'
# mes_inicio = '01/2019'
# mes_fim = '12/2019'
# mes_inicio = '01/2020'
# mes_fim = '12/2020'
mes_inicio = '01/2021'
mes_fim = '10/2021'

# Período mais antigo: 01/2014
i = 1
x = 0
# ITAJUBÁ 153030
#para = {'mesAnoInicio':mes_inicio, 'mesAnoFim':mes_fim, "pagina":i, 'unidadeGestora':'153030'}

# ITABIRA 158161
para = {'mesAnoInicio':mes_inicio, 'mesAnoFim':mes_fim, "pagina":i, 'unidadeGestora':'158161'}

pages_list = []

response_obj = requests.get(url + api, headers=header, params=para)
print(f'{response_obj}: comunicação ok!')

response_json = response_obj.json()
for j, item in enumerate(response_json, start=1):
    x += 1
    pages_list.append(item)
    print(f'Registro adicionado na lista de dados! Total de registros {x}...')
#teste = requests.get(url + api)

# Para as páginas seguintes
i = 2 # contador de páginas
while response_json:
    # para = {'mesAnoInicio':mes_inicio, 'mesAnoFim':mes_fim, "pagina":i, 'unidadeGestora':'153030'}
    para = {'mesAnoInicio':mes_inicio, 'mesAnoFim':mes_fim, "pagina":i, 'unidadeGestora':'158161'}
    response_obj = requests.get(url + api, headers=header, params=para)
    response_json = response_obj.json()
    for j, item in enumerate(response_json, start=1):
        x += 1
        pages_list.append(item)
        print(f'Registro adicionado na lista de dados! Total de registros {x}...')
    # pages_list.append(response_json)
    i += 1
    
#print(type(response_json))
print()
print(f'Dados lidos com sucesso. Começando a gerar a tabela...')
#print(len(pages_list))

df = pd.DataFrame.from_dict(pages_list, orient='columns')

print()
print(f'Tabela gerada com sucesso. Começando a exportar para o arquivo em Execel...')

# ITAJUBÁ
df.to_excel(f'Despesas_Unifei_{mes_inicio.replace("/", "_")}_{mes_fim.replace("/", "_")}.xlsx')

# ITABIRA
df.to_excel(f'Despesas_Unifei_{mes_inicio.replace("/", "_")}_{mes_fim.replace("/", "_")}_ITABIRA.xlsx')

print()
print(f'Arquivo em Excel exportado com sucesso!')
print()
# for i, j in enumerate(teste.json()):
#     print(i, j)
