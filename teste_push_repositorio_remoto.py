
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

url = "https://www.alphavantage.co/query?function=CASH_FLOW&symbol=IBM&apikey=DNTIMB6HGSZAYR01"
r = requests.get(url)
datas = r.json()['annualReports']
for data in datas:
    print(data)