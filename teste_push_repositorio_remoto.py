
""" from datetime import date, datetime

dateNow = datetime.now()
fileName = f"FGFinance{dateNow.strftime('%f')}{'.json'}"
print(fileName) """

import csv

import requests

""" 
fileName = "F:\\Users\\Gilvan\\Downloads\\fx_intraday_5min_EUR_USD.csv"


f=open(fileName , "r" , newline="")
reader = csv.reader(f)

for row in reader:
    print(row)

f.close()
 """

url = f"https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=IBM&apikey=DNTIMB6HGSZAYR01"
y = requests.get(url)
datas3 = y.json()['annualReports']
for data in datas3:
    print(type(data['ebit'])) 