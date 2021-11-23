import os
import json
import requests


#https://www.alphavantage.co/documentation/#dailyadj
#https://web.digitalinnovation.one/track/everis-new-talents-2-java/confirmation

#API B3
#https://developers.b3.com.br/apis-br

os.system("cls")

#dados_empresa_user = input("Escolha uma opcao:  " )
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBOV.SA&apikey=DNTIMB6HGSZAYR01'
#data = requests.get(url=url, headers=navegador)
r = requests.get(url)
data = r.json()['Time Series (Daily)']
print("\n")
# dados_empresa = ['1. open', '2. high', '3. low', '4. close', '5. volume'] 


dataFiltro = '2021-11'
data_filter = { k: v for (k ,v) in data.items() if dataFiltro in k}
open_filter = [value for value in data_filter.values()]
for (key , value) in data_filter.items():
    print(value)
""" 
navegador = {
    "User-Agent":"Chrome"
}
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=PETR4.SA&slice=year1month2&apikey=DNTIMB6HGSZAYR01'

r = requests.get(url=url, headers=navegador)
datas = r.json()
#data_filter = []
print(datas)
 for value in datas:
    print(value['fiscalDateEnding'])
    #print (len(value.keys()))  """


