import csv
from datetime import datetime
import json

def csvCreate(stock , enterprise):
    data = []
    data.append((1 , stock , enterprise))
    data.append([2 , stock, enterprise])
    dateNow = datetime.now()
    fileName = f"FGFinance{dateNow.strftime('%f')}{'.csv'}"
    f= open(fileName , "w" , newline="")
    writer = csv.writer(f , delimiter = ";")

    for linha in data:
        writer.writerow(linha)
    f.close()

    f=open(fileName , "r" , newline="")
    reader = csv.reader(f)

    for row in reader:
        print(row)

    f.close()
def jsonCreate(dados):
    for (key , value) in dados.items():
        print(key , value)
    data= {k : v for (k , v) in dados.items()}
    dateNow = datetime.now()
    fileName = f"FGFinance{dateNow.strftime('%f')}{'.json'}"
    #escrever formato JSON

    f= open(fileName , "w")
    json.dump(data , f, sort_keys=True , indent=4)
    f.close()
    #ler formato json

    f = open(fileName , "r")
    data = json.load(f)
    f.close
    print (data)
