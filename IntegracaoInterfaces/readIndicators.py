
#Implementar classe para buscar os indicadores
import csv
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
    
    def teste(ticker):
        datas = []
        dados = []
        volume = []
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey=DNTIMB6HGSZAYR01'
        
        r = requests.get(url)
        
        data = r.json()['Time Series (Daily)']
        
        # dados_empresa = ['1. open', '2. high', '3. low', '4. close', '5. volume'] 
        dataFiltro = '2021-11'
        data_filter = { k: v for (k ,v) in data.items() if dataFiltro in k}
        
        for (key , value) in data_filter.items():
            datas.insert(0 , key)
            dados.insert(0 , value['4. close'])
            volume.insert(0 , value['5. volume'] )
        return (datas , dados , volume) 

class exteriorTicker:

    def queryTicker():
        CSV_URL = "https://www.alphavantage.co/query?function=LISTING_STATUS&apikey=DNTIMB6HGSZAYR01"
        with requests.Session() as s:
            download = s.get(CSV_URL)
            decoded_content = download.content.decode('utf-8')
            cr = csv.reader(decoded_content.splitlines(), delimiter=',')
            my_list = list(cr)
            for row in my_list:
                print(row)    


class IndicatorsExterior:

    #fiscalDateEnding data fiscal todas as apis
    #Açoes em circulaçao: "SharesOutstanding"(overview)
    #https://www.alphavantage.co/query?function=OVERVIEW&symbol=IBM&apikey=demo
    #
    #ebit , ebitda = "ebit", "ebitda" (income-statement)
    #
    #passivoFE = 
    #workingCapital= currentNetReceivables - currentAccountsPayable(balane-sheet)
    #https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=IBM&apikey=demo
    #cashAndEquivalent.append(data['changeInCashAndCashEquivalents'])
    #caixa: cashAndCashEquivalentsAtCarryingValue + propertyPlantEquipment (balance-sheet)
    # - dividendPayout (cash-flow)
    
    def cash_flow(ticker):            
        debtCash = []
        
        url = f"https://www.alphavantage.co/query?function=CASH_FLOW&symbol={ticker}&apikey=DNTIMB6HGSZAYR01"
        r = requests.get(url)
        datas = r.json()['annualReports']
        for data in datas:                
            debtCash.append(int(data['cashflowFromFinancing']) + int(data['dividendPayout']))
        return debtCash    
        

    def balance_sheet(ticker):
        workingCapital = []      
        cashAndEquivalent = []                 
        url = f"https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={ticker}&apikey=DNTIMB6HGSZAYR01"
        x = requests.get(url)
        datas2 = x.json()['annualReports']
        for data in datas2:
            workingCapital.append(int(data['currentNetReceivables']) - int(data['currentAccountsPayable'])) 
            cashAndEquivalent.append(int(data['cashAndShortTermInvestments']) + int(data['propertyPlantEquipment']))               
        return (workingCapital , cashAndEquivalent)

    def income_statement(ticker):    
        ebit = []      
        ebitda = []                 
        url = f"https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={ticker}&apikey=DNTIMB6HGSZAYR01"
        y = requests.get(url)
        datas3 = y.json()["annualReports"]
        for data in datas3:
            ebit.append(int(data['ebit'])) 
            ebitda.append(int(data['ebitda']))
        return(ebit , ebitda)

    def overview( ticker):          
        url = f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={ticker}&apikey=DNTIMB6HGSZAYR01"
        z = requests.get(url)
        quantityStock = z.json()['SharesOutstanding']
        return int(quantityStock) 
