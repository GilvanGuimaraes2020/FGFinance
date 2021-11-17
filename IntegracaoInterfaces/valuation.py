#Utiliza dados financeiro da empresa para calcular seu valuation

import os

os.system("cls")

ebitda = [605.26 , 464.73, 714.56, 1030.75, 1245.24]

ebit = [490.93, 338.93, 580.95, 887.69, 1081.55]
""" for n in range(5):
    ebitda.append(float(input("Entre com o ebitda da empresa: ")))


for n in range(5):
    ebit.append(float(input("Entre com o ebit da empresa: ")))
 """

reinvest = 1.2

costCapital = 0.1
growth = 0.065
growthPerpet = 0.03
flcFuturo = []

irRate = float(input("Entre com a aliquota do IR: "))

ir = [round((ebit[n] * irRate/100 * -1) , 3) for n in range(len(ebit))]

depAm = [(round((ebitda[n] - ebit[n]) , 3)) for n in range(len(ebit))]
#Lucro operacional 
nopat = [round(ebit[n] + ir[n] , 3)  for n in range(len(ebit))]
#reinvestimento
capex= [round(depAm[n] * reinvest * -1 , 3)  for n in range(len(depAm))]
#Necessidade de Capital de Giro
ncl = [0 , -372.1, -259.4, 268.2, 380.4]
#Fluxo de capital operacional
fco = [round(nopat[n] + depAm[n] , 3)  for n in range(len(nopat))]
#Fluxo de capital liquido
fcl = [round(fco[n] + capex[n] - ncl[n], 3)  for n in range(len(capex))]
#   Iniciando fluxo de caixa futuro, seguindo exemplo do curso
#em virtude da descrepancia no ano de 2016 e 2017
flcFuturo.append(510)
print(fcl)
for n in range(1 , 5):
    flcFuturo.append(round(flcFuturo[n-1] * (1 + growth ) , 3))
#Fluxo na perpetuidade
fclPerpet = (round(flcFuturo[len(flcFuturo) - 1] * (1 + growthPerpet) , 3))
#Valor Terminal
fclTerminal = flcFuturo[len(flcFuturo) - 1] /(costCapital - growthPerpet )
#fUXO DE CAIXA DESCONTADO

fDesc =[round(flcFuturo[n] / pow(1 + costCapital , n + 1)  ,3) for n in  range(len(flcFuturo))] 
fDesc[len(fDesc) - 1] = round(flcFuturo[len(flcFuturo) - 1] + fclTerminal / pow(1 + costCapital , n + 1)  ,3)
enterpriseValue = sum(fDesc)
#Soma-se os caixas e subtrai as obrigaçoes da empresa
cash =  599.1 +  409.1 -  130.7 - 182.0 - 325.2 
qualityValue = enterpriseValue + cash
quantityStock = 190591464
stockPrice = round(qualityValue / quantityStock * pow(10 , 6) , 3)
print(depAm)
print(ir)
print(nopat)
print (capex)
print (ncl)
print (fco)
print (fcl)
print (fclTerminal)
print (fDesc)
print (enterpriseValue)
print(stockPrice)