
import os

import requests
os.system("cls")

""" from pandas_datareader import data as web
import pandas as pd
#import yfinance as yf
import os
from datetime import date

os.system("cls")

startAnalisys = date(2021 , 11 , 1)

endAnalisys = date.today()

dados = web.DataReader('PETR4.SA', data_source='yahoo', start= startAnalisys, end = endAnalisys)



print(type(dados) ) """


url = "https://www.yahoofinanceapi.com/yahoo-finance-api-specification.json"
data = requests.get(url=url)
r = requests.get(url)
data = r.json()
print(data['paths'].keys())


