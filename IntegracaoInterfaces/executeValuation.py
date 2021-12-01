import readIndicators

class initialValues:
    
    ebit = [490.93, 338.93, 580.95, 887.69, 1081.55]
    ebitda = [605.26 , 464.73, 714.56, 1030.75, 1245.24]
    ncl = [0 , -372.1, -259.4, 268.2, 380.4]
    cash =  599.1 +  409.1 -  130.7 - 182.0 - 325.2
    quantityStock = 190591464
    flcFuturo = []

    def __init__(self, irRate, growthPerpet, growth, reinvest, costCapital) :
        self.growthPerpet = growthPerpet
        self.growth = growth
        self.reinvest = reinvest
        self.costCapital = costCapital
        self.ir = [round((self.ebit[n] * irRate/100 * -1) , 3) for n in range(len(self.ebit))]
        self.depAm = [(round((self.ebitda[n] - self.ebit[n]) , 3)) for n in range(len(self.ebit))]
        self.nopat = [round(self.ebit[n] + self.ir[n] , 3)  for n in range(len(self.ebit))]
        self.capex= [round(self.depAm[n] * self.reinvest * -1 , 3)  for n in range(len(self.depAm))]
        self.fco = [round(self.nopat[n] + self.depAm[n] , 3)  for n in range(len(self.nopat))]
        self.fcl = [round(self.fco[n] + self.capex[n] - self.ncl[n], 3)  for n in range(len(self.capex))]
        



    def flows(self):
        self.flcFuturo.append(510)
        for n in range(1 , 5):
            self.flcFuturo.append(round(self.flcFuturo[n-1] * (1 + self.growth ) , 3))
        fclPerpet = (round(self.flcFuturo[len(self.flcFuturo) - 1] * (1 + self.growthPerpet) , 3))
        fclTerminal = self.flcFuturo[len(self.flcFuturo) - 1] /(self.costCapital - self.growthPerpet )
        fDesc =[round(self.flcFuturo[n] / pow(1 + self.costCapital , n + 1)  ,3) for n in  range(len(self.flcFuturo))] 
        fDesc[len(fDesc) - 1] = round(self.flcFuturo[len(self.flcFuturo) - 1] + fclTerminal / pow(1 + self.costCapital , n + 1)  ,3)
        enterpriseValue = sum(fDesc)
        equityValue = enterpriseValue + self.cash
        stockPrice = round(equityValue / self.quantityStock * pow(10 , 6) , 3)
        return {'fclPerpet' : fclPerpet ,'fclTerminal':fclTerminal, 'flcFuture':self.flcFuturo,
        'fDesc' : fDesc, 'enterpriseValue':enterpriseValue, 'equityValue' : equityValue,
        'stockPrice':stockPrice}

class ValuesExterior:
    
    quantityStock = readIndicators.IndicatorsExterior.overview("IBM")
    #(ebit , ebitda) = readIndicators.IndicatorsExterior.income_statement("IBM")
    (working , cashEquivalent) = readIndicators.IndicatorsExterior.balance_sheet("IBM")
    debt = readIndicators.IndicatorsExterior.cash_flow("IBM")
    ncl = [(a - b) for a ,b in zip(cashEquivalent , debt) ]
    
    def __init__(self, irRate,  growth, reinvest, costCapital) :
        self.growthPerpet = 3 / 100
        self.growth = growth
        self.reinvest = reinvest
        self.costCapital = costCapital
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

