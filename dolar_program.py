import requests

get_dollar = requests.get('https://pydolarvenezuela-api.vercel.app/api/v1/dollar/')
data_dollar = get_dollar.json()

print(f"{data_dollar['datetime']}")
data_dollar['datetime']['date'],
# print(f"Banco Central de Venezuela: {data_dollar['monitors']['bcv']['price']}")
# print(f"Última actualización: {data_dollar['monitors']['bcv']['last_update']}\n")

# print(f"Binance: {data_dollar['monitors']['binance']['price']}")
# print(f"Última actualización: {data_dollar['monitors']['binance']['last_update']}\n")

# print(f"Cripto dolar: {data_dollar['monitors']['cripto_dolar']['price']}")
# print(f"Última actualización: {data_dollar['monitors']['cripto_dolar']['last_update']}\n")

# print(f"Dolar Today: {data_dollar['monitors']['dolar_today']['price']}")
# print(f"Última actualización: {data_dollar['monitors']['dolar_today']['last_update']}\n")

# print(f"EnParaleloVnzl: {data_dollar['monitors']['enparalelovzla']['price']}")
# print(f"Última actualización: {data_dollar['monitors']['enparalelovzla']['last_update']}\n")