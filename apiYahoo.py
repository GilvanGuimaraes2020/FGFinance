
import os

import requests
os.system("cls")

#VwsEUE9zelaX9J1eZ6sAs7CN2V5rfzZT709ET9Mr
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



url = "https://yfapi.net/v6/finance/quote"

querystring = {"symbols":"PETR4.SA"}

headers = {
    'x-api-key': "VwsEUE9zelaX9J1eZ6sAs7CN2V5rfzZT709ET9Mr"
    }

responses = requests.request("GET", url, headers=headers, params=querystring).json()
print (responses)


