import requests

class ValuesExterior:
    
    def __init__(self,dados) :
        self.growthPerpet = 0.03
        self.growth = dados['growth'] / 100
        self.reinvest = dados['reinvest'] 
        self.costCapital = 0.1
        irRate = dados['IR']
        self.ebit = dados['ebit']
        self.ebitda = dados['ebitda']
        self.ncl = dados['ncg']
        ncg = [(self.ncl[i] - self.ncl[i - 1]) for i in range(1 , 5) ]
        ncg.insert(0 , 0)
        self.quantityStock = dados['stocks']
        self.cash =  dados['cash']
        self.ir = [round((self.ebit[n] * irRate/100 * -1) , 3) for n in range(len(self.ebit))]
        self.depAm = [(round((self.ebitda[n] - self.ebit[n]) , 3)) for n in range(len(self.ebit))]
        self.nopat = [round(self.ebit[n] + self.ir[n] , 3)  for n in range(len(self.ebit))]
        self.capex= [round(self.depAm[n] * self.reinvest * -1 , 3)  for n in range(len(self.depAm))]
        self.fco = [round(self.nopat[n] + self.depAm[n] , 3)  for n in range(len(self.nopat))]
        self.fcl = [round(self.fco[n] + self.capex[n] - ncg[n], 3)  for n in range(len(self.capex))]
        
    def flows(self): 
        flcFuturo = []
        fDesc = []        

        fluxo = [(self.fcl[i - 1] / self.fcl[i]) for i in range(1 , 5)]   
        multFluxo =  sum(fluxo) / (len(self.fcl) - 1 )
        flcFuturo.append(self.fcl[4] * multFluxo) 
        for n in range(1 , 5):
            flcFuturo.append(round(flcFuturo[n-1] * (1 + self.growth ) , 3))
        fclPerpet = (round(flcFuturo[len(flcFuturo) - 1] * (1 + self.growthPerpet) , 3))
        fclTerminal = flcFuturo[len(flcFuturo) - 1] /(self.costCapital - self.growthPerpet )
        fDesc =[round(flcFuturo[n] / pow(1 + self.costCapital , n + 1)  ,3) for n in  range(len(flcFuturo))] 
        fDesc[len(fDesc) - 1] = round(flcFuturo[len(flcFuturo) - 1] + fclTerminal / pow(1 + self.costCapital , n + 1)  ,3)
        enterpriseValue = sum(fDesc)
        equityValue = enterpriseValue + self.cash
        stockPrice = round(equityValue / self.quantityStock  , 3)
        self.fclPerpet = fclPerpet
        self.fclTerminal = fclTerminal
        self.flcFuturo = flcFuturo
        self.fDesc = fDesc
        self.enterprise = enterpriseValue
        self.equity = equityValue
        self.stockPrice = stockPrice
        

class datasCompaniesExt:  

    def __init__(self , ticker):
        self.ticker = ticker

    def cashFlow(self):
        ebit = []
        ebitda = []
        url3 = f"https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={self.ticker}&apikey=DNTIMB6HGSZAYR01"
        x = requests.get(url3 )
        datas = x.json()
        datas3 = datas['annualReports']
        
        for data in datas3:
            ebit.append(float(data['ebit'])) 
            ebitda.append(float(data['ebitda'])) 
        
        self.ebit = ebit
        self.ebitda = ebitda 


    def debt (self):
        debtCash = []        
        url = f"https://www.alphavantage.co/query?function=CASH_FLOW&symbol={self.ticker}&apikey=DNTIMB6HGSZAYR01"
        a = requests.get(url)
        datas = a.json()['annualReports']
        for data in datas:                
            debtCash.append(float(data['cashflowFromFinancing']) + int(data['dividendPayout']))
        a.close()
        del datas
        self.debtCash  = debtCash
            

    def balance (self):
        workingCapital = []
        cashAndEquivalent = []
        url2 = f"https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={self.ticker}&apikey=DNTIMB6HGSZAYR01"
        x = requests.get(url2)
        datas2 = x.json()['annualReports']
        for data in datas2:
            workingCapital.append(float(data['currentNetReceivables']) - int(data['currentAccountsPayable'])) 
            cashAndEquivalent.append(float(data['cashAndShortTermInvestments']) + int(data['propertyPlantEquipment']))               
        x.close()
        del datas2
        self.workingCapital = workingCapital
        self.cashAndEquivalent = cashAndEquivalent


        

    def overview(self):        
        url = f"https://www.alphavantage.co/query?function=OVERVIEW&symbol={self.ticker}&apikey=DNTIMB6HGSZAYR01"
        z = requests.get(url)
        dados = z.json()['SharesOutstanding']
        quantityStock = int(dados)
        
        self.quantityStock = quantityStock 
