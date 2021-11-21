
#Implementar classe para buscar os indicadores
import json
import requests
import os

class Indicators:
    ibovespa = 0
    dolar = 100

    def __init__(self):
        navegador = {
        "User-agent" : "Chrome"    }
        url = f'https://api.hgbrasil.com/finance?key=cecacfc8'
        data = requests.get(url=url, headers=navegador)
        todo = json.loads(data.content)
        moedas = todo['results']['currencies']        
        taxa_juro = todo['results']['taxes']        
        bolsa_valores = todo['results']['stocks']
        self.ibovespa = bolsa_valores['IBOVESPA']
        self.dolar = moedas['USD']
        self.euro = moedas['EUR']
        self.selic = taxa_juro[0]['selic']

    def retornos(self):
        #return f"Dolar: R${round(self.dolar['buy'],2)}\tEuro: R${round(self.euro['buy'],2)}\tSelic: {round(self.selic,2)}%\tIbovespa: {round(self.ibovespa['variation'],2)}%"
        datasReturn = {'dolar' : self.dolar, 'euro':self.euro }
        return datasReturn
    

cabecalho = Indicators()
print(cabecalho.dolar['buy'])

