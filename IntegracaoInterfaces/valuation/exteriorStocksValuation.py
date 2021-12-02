import requests

class ValuesExterior:
    
    """ quantityStock = overview("IBM")  
    fluxo = ex.CashFlow.cashFlow("'IBM")   
    ebit = fluxo['ebit']
    ebitda = fluxo['ebitda']
    balance = ex.balance("IBM")
    working = balance['working']
    cashEquivalent = balance['cash']
    debt = ex.debt("IBM") """

    def __init__(self, irRate,  growth, reinvest, costCapital) :
        self.growthPerpet = 3 / 100
        self.growth = growth
        self.reinvest = reinvest
        self.costCapital = costCapital
        ncl = [self.cashEquivalent[i] - self.debt[i] for i in range(len(self.debt)) ]
        self.ir = [round((self.ebit[n] * irRate/100 * -1) , 3) for n in range(len(self.ebit))]
        self.depAm = [(round((self.ebitda[n] - self.ebit[n]) , 3)) for n in range(len(self.ebit))]
        self.nopat = [round(self.ebit[n] + self.ir[n] , 3)  for n in range(len(self.ebit))]
        self.capex= [round(self.depAm[n] * self.reinvest * -1 , 3)  for n in range(len(self.depAm))]
        self.fco = [round(self.nopat[n] + self.depAm[n] , 3)  for n in range(len(self.nopat))]
        self.fcl = [round(self.fco[n] + self.capex[n] - self.ncl[n], 3)  for n in range(len(self.capex))]
        
    def flows(self):        
        for n in range(1 , 5):
            self.flcFuturo.append(round(self.flcFuturo[n-1] * (1 + self.growth ) , 3))
        fclPerpet = (round(self.flcFuturo[len(self.flcFuturo) - 1] * (1 + self.growthPerpet) , 3))
        fclTerminal = self.flcFuturo[len(self.flcFuturo) - 1] /(self.costCapital - self.growthPerpet )
        fDesc =[round(self.flcFuturo[n] / pow(1 + self.costCapital , n + 1)  ,3) for n in  range(len(self.flcFuturo))] 
        fDesc[len(fDesc) - 1] = round(self.flcFuturo[len(self.flcFuturo) - 1] + fclTerminal / pow(1 + self.costCapital , n + 1)  ,3)
        enterpriseValue = sum(fDesc)
        equityValue = enterpriseValue + self.cash
        stockPrice = round(equityValue / self.quantityStock , 3)
        return {'fclPerpet' : fclPerpet ,'fclTerminal':fclTerminal, 'flcFuture':self.flcFuturo,
        'fDesc' : fDesc, 'enterpriseValue':enterpriseValue, 'equityValue' : equityValue,
        'stockPrice':stockPrice}


def cashFlow(ticker):
    ebit = []
    ebitda = []
    url3 = f"https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={ticker}&apikey=DNTIMB6HGSZAYR01"
    x = requests.get(url3 )
    datas = x.json()
    datas3 = datas['annualReports']
    
    for data in datas3:
        ebit.append(int(data['ebit'])) 
        ebitda.append(int(data['ebitda'])) 
    
    return {'ebit': ebit,
        'ebitda' : ebitda}  


def debt (ticker):
    debtCash = []        
    url = f"https://www.alphavantage.co/query?function=CASH_FLOW&symbol={ticker}&apikey=DNTIMB6HGSZAYR01"
    a = requests.get(url)
    datas = a.json()['annualReports']
    for data in datas:                
        debtCash.append(int(data['cashflowFromFinancing']) + int(data['dividendPayout']))
    a.close()
    del datas
    return debtCash 
        

def balance (ticker):
    workingCapital = []
    cashAndEquivalent = []
    url2 = f"https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={ticker}&apikey=DNTIMB6HGSZAYR01"
    x = requests.get(url2)
    datas2 = x.json()['annualReports']
    for data in datas2:
        workingCapital.append(int(data['currentNetReceivables']) - int(data['currentAccountsPayable'])) 
        cashAndEquivalent.append(int(data['cashAndShortTermInvestments']) + int(data['propertyPlantEquipment']))               
    x.close()
    del datas2
    return {
        'working' : workingCapital,
        'cash' : cashAndEquivalent
    }


    

def overview(ticker):        
    url = f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={ticker}&apikey=DNTIMB6HGSZAYR01"
    z = requests.get(url)
    dados = z.json()['SharesOutstanding']
    quantityStock = int(dados)
    
    return quantityStock    
