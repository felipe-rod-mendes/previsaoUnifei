import requests

url = 'http://api.portaldatransparencia.gov.br'

api = '/api-de-dados/despesas/recursos-recebidos'

header = {'chave-api-dados':'7be5830b97f91762ad7a33b27db9f431'}

# Período mais antigo: 01/2014
para = {'mesAnoInicio':'01/2014', 'mesAnoFim':'01/2014', "pagina":1, 'unidadeGestora':'153030', 'chave-api-dados':'7be5830b97f91762ad7a33b27db9f431'}

pages_list = []

response_obj = requests.get(url + api, headers=header, params=para)
response_json = response_obj.json()

pages_list.append(response_json)
#teste = requests.get(url + api)

# Consegui me comunicar com a API, mas só retornou a primeira página
# gostaria de automatizar um loop para incrementar automaticamente o número de páginas e ir armazenando o valor em listas
i = 2 # contador de páginas
while response_json:
    para = {'mesAnoInicio':'01/2014', 'mesAnoFim':'01/2014', "pagina":i, 'unidadeGestora':'153030'}
    response_obj = requests.get(url + api, headers=header, params=para)
    response_json = response_obj.json()
    pages_list.append(response_json)
    i += 1
    
#print(type(response_json))
print(len(pages_list))

# for i, j in enumerate(teste.json()):
#     print(i, j)
