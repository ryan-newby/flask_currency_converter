from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)


def api_call(s_currency, d_currency):
    input_list = [s_currency, d_currency]
    response = requests.get('https://open.er-api.com/v6/latest/' + str(input_list[0]))
    data_1 = response.json()
    data_2 = data_1.get('rates')
    return data_2.get(str(d_currency))


@app.route('/')
@app.route('/index/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        s_currency = request.form.get('source-currency')
        d_currency = request.form.get('destination-currency')
        out_response = api_call(s_currency, d_currency)
        return render_template('index.html', s_currency=s_currency, d_currency=d_currency, out_response=out_response)
