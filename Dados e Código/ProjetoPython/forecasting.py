# Importações para rodar os modelos
import pandas as pd # dataframe opertations - pandas
from matplotlib import pyplot as plt # plotting data - matplotlib
from statsmodels.tsa.seasonal import seasonal_decompose # time series - statsmodels # Seasonality decomposition
from statsmodels.tsa.holtwinters import SimpleExpSmoothing # holt winters - single exponential smoothing
from statsmodels.tsa.holtwinters import ExponentialSmoothing # double and triple exponential smoothing
from sklearn.metrics import mean_absolute_error, mean_squared_error
from math import sqrt

# importação de dados
df = pd.read_excel('dados.xlsx', sheet_name='leitura2', parse_dates=True, index_col='data')
#df = pd.read_excel('dados.xlsx', sheet_name='leitura3', parse_dates=True, index_col='data)

print(df.head())
print(df.info(verbose=True))

# plt.plot(df['total_despesa'])
# plt.show()
# plt.savefig('total_despesa_v1.png')

# Método multiplicativo
decompose_result = seasonal_decompose(df['total_despesa'], model='multiplicative')
#print(type(decompose_result))
figure = decompose_result.plot()
print(type(figure))
figure.savefig('multiplicative.png')

decompose_result = seasonal_decompose(df['total_despesa'], model='additive')
#print(type(decompose_result))
figure = decompose_result.plot()
print(type(figure))
figure.savefig('additive.png')

# Set the frequency of the date time index as Monthly start as indicated by the data
df.index.freq = 'M'

# Set the value of Alpha and define m (Time Period)
m = 12
alpha = 1/(2*m)

# # Aplicação - SINGLE Exponential Smoothing
# df['HWES1'] = SimpleExpSmoothing(df['total_despesa']).fit(smoothing_level=alpha,optimized=False,use_brute=True).fittedvalues

# # plt.plot(df[['total_despesa', 'HWES1']])
# # plt.title('Holt Winters Single Exponential Smoothing')
# # plt.savefig('HWES1.png')

# fig, ax = plt.subplots()
# ax.plot(df[['total_despesa', 'HWES1']])
# plt.title('Holt Winters Single Exponential Smoothing')
# #plt.show()
# #plt.savefig('HWES1.png')

# # Aplicação - DOBLE Exponential Smoothing

# df['HWES2_ADD'] = ExponentialSmoothing(df['total_despesa'], trend='add').fit().fittedvalues
# df['HWES2_MUL'] = ExponentialSmoothing(df['total_despesa'], trend='mul').fit().fittedvalues

# fig, ax = plt.subplots()
# ax.plot(df[['total_despesa', 'HWES2_ADD', 'HWES2_MUL']])
# plt.title('Holt Winters DOUBLE Exponential Smoothing')
# # plt.show()

# # TRIPLE
# df['HWES3_ADD'] = ExponentialSmoothing(df['total_despesa'], trend='add', seasonal='add', seasonal_periods=12).fit().fittedvalues

# df['HWES3_MUL'] = ExponentialSmoothing(df['total_despesa'], trend='mul', seasonal='mul', seasonal_periods=12).fit().fittedvalues

# fig, ax = plt.subplots()
# ax.plot(df[['total_despesa', 'HWES3_ADD', 'HWES3_MUL']])
# plt.title('Holt Winters TRIPLE Exponential Smoothing')
# #plt.show()

# #airline[[‘Thousands of Passengers’,’HWES3_ADD’,’HWES3_MUL’]].plot(title=’Holt Winters Triple Exponential Smoothing: Additive and Multiplicative Seasonality’)

# PREVISÃO
# 85 pontos de dados como treinamento, de 2013 a 2020. 9 pontos de 2021 como teste, como apliação prática.
treinamento = df[:85]
# print(treinamento.shape)
teste = df[85:]
# print(teste.shape)

# MUL MUL
fitted_model = ExponentialSmoothing(treinamento['total_despesa'], trend='mul', seasonal='mul', seasonal_periods=12).fit()
test_predictions = fitted_model.forecast(9)

# print(len(test_predictions))

print("Mul Mul")
print(f'Mean Absolute Error = {mean_absolute_error(teste["total_despesa"], test_predictions)}')
print(f'Root Mean Squared Error = {sqrt(mean_squared_error(teste["total_despesa"], test_predictions))}')

fig, ax = plt.subplots()
ax.plot(treinamento['total_despesa'], label='Treinamento')
ax.plot(teste['total_despesa'], label='Teste')
ax.plot(test_predictions, label='Previsão')
ax.legend()
plt.title('Dados de treinameto, teste e previsão utilizando Holt-Winters.\nTendência e sazonalidade multiplicativas.')
# plt.show()
plt.savefig('previsao_mul_mul.png')


# ADD ADD
fitted_model = ExponentialSmoothing(treinamento['total_despesa'], trend='add', seasonal='add', seasonal_periods=12).fit()
test_predictions = fitted_model.forecast(9)

# print(len(test_predictions))
print()
print('Add Add')
print(f'Mean Absolute Error = {mean_absolute_error(teste["total_despesa"], test_predictions)}')
print(f'Root Mean Squared Error = {sqrt(mean_squared_error(teste["total_despesa"], test_predictions))}')

fig, ax = plt.subplots()
ax.plot(treinamento['total_despesa'], label='Treinamento')
ax.plot(teste['total_despesa'], label='Teste')
ax.plot(test_predictions, label='Previsão')
ax.legend()
plt.title('Dados de treinameto, teste e previsão utilizando Holt-Winters.\nTendência e sazonalidade aditivas.')
# plt.show()
plt.savefig('previsao_add_add.png')

# ADD MUL
fitted_model = ExponentialSmoothing(treinamento['total_despesa'], trend='add', seasonal='mul', seasonal_periods=12).fit()
test_predictions = fitted_model.forecast(9)

# print(len(test_predictions))
print()
print('Add Mul')
print(f'Mean Absolute Error = {mean_absolute_error(teste["total_despesa"], test_predictions)}')
print(f'Root Mean Squared Error = {sqrt(mean_squared_error(teste["total_despesa"], test_predictions))}')

fig, ax = plt.subplots()
ax.plot(treinamento['total_despesa'], label='Treinamento')
ax.plot(teste['total_despesa'], label='Teste')
ax.plot(test_predictions, label='Previsão')
ax.legend()
plt.title('Dados de treinameto, teste e previsão utilizando Holt-Winters.\nTendência aditiva e sazonalidade multiplicativa.')
# plt.show()
plt.savefig('previsao_add_mul.png')

# MUL ADD
fitted_model = ExponentialSmoothing(treinamento['total_despesa'], trend='mul', seasonal='add', seasonal_periods=12).fit()
test_predictions = fitted_model.forecast(9)

# print(len(test_predictions))
print()
print('Mul Add')
print(f'Mean Absolute Error = {mean_absolute_error(teste["total_despesa"], test_predictions)}')
print(f'Root Mean Squared Error = {sqrt(mean_squared_error(teste["total_despesa"], test_predictions))}')

fig, ax = plt.subplots()
ax.plot(treinamento['total_despesa'], label='Treinamento')
ax.plot(teste['total_despesa'], label='Teste')
ax.plot(test_predictions, label='Previsão')
ax.legend()
plt.title('Dados de treinameto, teste e previsão utilizando Holt-Winters.\nTendência aditiva e sazonalidade multiplicativa.')
# plt.show()
plt.savefig('previsao_mul_add.png')
