
""" from datetime import date, datetime

dateNow = datetime.now()
fileName = f"FGFinance{dateNow.strftime('%f')}{'.json'}"
print(fileName) """

import csv


fileName = "F:\\Users\\Gilvan\\Downloads\\fx_intraday_5min_EUR_USD.csv"


f=open(fileName , "r" , newline="")
reader = csv.reader(f)

for row in reader:
    print(row)

f.close()
