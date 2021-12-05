
from flask import Flask , render_template , request
from flask_material import Material


import connectionDataBase.connectionBD as BD


from valuation.exteriorStocksValues import cashFlow, debt, balance, overview
from valuation.executeValuation import initialValues


import getFiles.exportFile  as exportFile
import re
import indicators.readIndicators as readIndicators

indicators = readIndicators.Indicators()

def initialState(ticker):
    return readIndicators.readData.teste(ticker)

def funcValuation(dados):
    ebit = [float(v) for (k ,v) in dados.items() if re.search("\\bebit.\\b", k)]
    ebitda = [float(v) for (k ,v) in  dados.items() if "ebitda" in k ]
    ncg = [float(v) for (k ,v) in dados.items() if "cg" in k]
    stocks = int(dados['stocks'])
    IR = int(dados['IR'])
    growth = int(dados['growth'])
    reinvest = float(dados['reinvest'])
    cash = float(dados['cash'])
    sendDados = {'ebit':ebit, 'ebitda' : ebitda, 
    'ncg' :ncg, 'stocks' : stocks, 'IR' : IR,
    'growth' :growth, 'reinvest' : reinvest,
    'cash' : cash}
    return initialValues(sendDados)

def cashValues(dados):    
    return cashFlow(dados)

def debtValue(dados , cashvalue):
    cashout = debt(dados)
    cashin = [cashvalue[i] - cashout[i] for i in range(5)]
    return cashin

def balanceValue(dados):
    return balance(dados)

def overValue(dados):
    return overview(dados)

app = Flask(__name__)

app.config['TITLE'] = 'FINANCAS'

Material(app)

@app.route('/')
def index():
    products = ['Baguete', 'Ciabata', 'Pretzel']
    return render_template('index.html' , products=products, dolar = indicators)


@app.route('/about' , methods = ['GET' , 'POST'])
def about():        
    return render_template('about.html',dolar = indicators)


@app.route('/valuation' , methods = ['post' , 'get'])
def valuation():
    requestHtml = request.args
    print(requestHtml)
    if requestHtml:        
        cashflow = cashValues("IBM") #ebit e ebitda
        print(cashflow)
        #caixa equivalente e o capital de giro
        balanceVal = balanceValue("IBM")
        print(balanceVal)
        #retorna o caixa da empresa
        cash = debtValue("IBM" , balanceVal['cash'])
        print(debt)
        #quantidade de açoes       
        over = overValue("IBM")
        print(over) 
        return render_template('valuation.html',dolar = indicators,
        over = over , ebit = cashflow['ebit'], 
        ebitda = cashflow['ebitda'], cash = cash )
    else:
        return render_template('valuation.html',dolar = indicators)


@app.route('/showvaluation' , methods = ['post' , 'get'])
def showvaluation():
    dados  = request.form
    if request.method == "POST":
        initialValues = funcValuation(dados)
        flows = initialValues.flows()   
    
    return render_template('showvaluation.html', dolar=indicators, initialValues = initialValues , dados = dados, flows = flows)


@app.route('/userRegister')
def userRegister():
    return render_template('userRegister.html',dolar = indicators)

@app.route('/dashboard', methods = ['post' , 'get'])
def dashboard():
    (labels , values , volume ) = initialState("PETR4.SA")
    
    return render_template('dashboard.html',  dolar = indicators,
    labelsData=labels,valuesData = values, volume = volume )

@app.route('/login' , methods = ['post' , 'get'])
def login():
    if request.method == "POST":
        datas_DB = request.form
        BD.create(datas_DB['nome'] , datas_DB['email'])
    return render_template('login.html' )

@app.route('/simulation' , methods=['post' , 'get'])
def simulation():    
    requestHtml = request.args  
    if requestHtml:
        (labels , values , volume) = initialState(requestHtml['ticker'])
    else:
       (labels , values, volume) = initialState("IBOV.SA") 
    
    
    return render_template('simulation.html', labelsData=labels, valuesData = values ,dolar = indicators )

@app.route('/exportFiles' , methods = ['post' , 'get'])
def exportFiles():
    dados  = request.form
    
    if (dados['method'] == "json"):
        exportFile.jsonCreate(dados)
    elif (dados['method'] == "csv"):
       exportFile.csvCreate(dados['stockPrice'] , dados['enterpriseValue'])     
    else:
        print("Sem dados")
      
    return render_template('exportFiles.html', dolar=indicators)


app.run(debug=True)

