import requests
import json

def api_call(s_currency, d_currency):
    input_list = [s_currency, d_currency]
    response = requests.get('https://open.er-api.com/v6/latest/' + str(input_list[0]))
    data_1 = response.json()
    data_2 = data_1.get('rates')
    return data_2.get(str(d_currency))



s_currency = 'USD'
d_currency = 'GBP'
print(api_call(s_currency, d_currency))