
#Implementar classe para buscar os indicadores
import json
import requests
import os

class Indicators:
    def __init__(self):
        navegador = {
        "User-agent" : "Chrome"    }
        url = f'https://api.hgbrasil.com/finance?key=cecacfc8'
        data = requests.get(url=url, headers=navegador)
        todo = json.loads(data.content)
        moedas = todo['results']['currencies']        
        taxa_juro = todo['results']['taxes']        
        bolsa_valores = todo['results']['stocks']
        
        #Taxas de Juros
        self.selic = taxa_juro[0]['selic']
        self.cdi = taxa_juro[0]['cdi']

        #Bolsas e Fundo Imobiliário
        self.ifix = bolsa_valores['IFIX']
        self.ibovespa = bolsa_valores['IBOVESPA']
        self.nasdaq = bolsa_valores['NASDAQ']
        self.dowjones = bolsa_valores['DOWJONES']
        self.cac = bolsa_valores['CAC']
        self.nikkei = bolsa_valores['NIKKEI']

        #Câmbio
        self.dolar = moedas['USD']
        self.euro = moedas['EUR']
        self.libra_esterlina = moedas['GBP']
        self.peso_argentino = moedas['ARS']
        self.dolar_canadense = moedas['CAD']
        self.dolar_australiano = moedas['AUD']
        self.yen_japones = moedas['JPY']
        self.renminbi_china = moedas['CNY']

        #Criptomoedas
        self.bitcoin = moedas['BTC']
        
        

class readData:
    datas = []
    dados = []
    def __init__(self, ticker):
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey=DNTIMB6HGSZAYR01'
        
        r = requests.get(url)
        data = r.json()['Time Series (Daily)']
        
        # dados_empresa = ['1. open', '2. high', '3. low', '4. close', '5. volume'] 
        dataFiltro = '2021-11'
        data_filter = { k: v for (k ,v) in data.items() if dataFiltro in k}
        
        for (key , value) in data_filter.items():
            self.datas.insert(0 , key)
            self.dados.insert(0 , value['4. close'])
       



