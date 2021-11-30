import csv
import os
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

def zipFile():
    path_zip = os.path.join(os.sep, "c:\\", "output.zip")
    path_dir = os.path.join(os.sep , "c:\\" , "src")

    zf = zip.ZipFile(path_zip , "w")
    for dirname , subdirs, files in os.walk(path_dir):
        zf.write(dirname)
        for filename in files:
            zf.write(os.path.join(dirname , filename))
    zf.close()

def descZip():
    dir = os.path.join(os.sep , "c:\\", "teste")
    if not os.path.isdir(dir):
        os.makedirs(dir)

    zf = zip.ZipFile("c:\\output.zip", "r")
    zf.extractall(dir)
    zf.close()