

class initialValues:
    
    """ ebit = [490.93, 338.93, 580.95, 887.69, 1081.55]
    ebitda = [605.26 , 464.73, 714.56, 1030.75, 1245.24]
    ncl = [0 , -372.1, -259.4, 268.2, 380.4]
    cash =  599.1 +  409.1 -  130.7 - 182.0 - 325.2
    quantityStock = 190591464 """
   
    
    def __init__(self, dados) :
        self.growthPerpet = 0.03
        self.growth = dados['growth'] / 100
        self.reinvest = dados['reinvest'] 
        self.costCapital = 0.1
        irRate = dados['IR']
        self.ebit = dados['ebit']
        self.ebitda = dados['ebitda']
        ncl = dados['ncg']
        ncg = [(ncl[i] - ncl[i - 1]) for i in range(1 , 5) ]
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
        stockPrice = round(equityValue * pow(10 , 6)/ self.quantityStock  , 3)
        
        return {'fclPerpet' : fclPerpet ,'fclTerminal':fclTerminal, 'flcFuture':flcFuturo,
        'fDesc' : fDesc, 'enterpriseValue':enterpriseValue, 'equityValue' : equityValue,
        'stockPrice':stockPrice}


