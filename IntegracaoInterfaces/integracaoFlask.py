from flask import Flask , render_template , request
from flask_material import Material
import os
import executeValuation
import exportFile 

import executeValuation

import readIndicators

""" executeValuation(24 , 0.03, 0.065, 1.2, 0.1) """

indicators = readIndicators.Indicators()

def initialState(ticker):
    return readIndicators.readData.teste(ticker)

def funcValuation():
    return executeValuation.initialValues(24 , 0.03, 0.065, 1.2, 0.1)

def valuesExterior():
    return executeValuation.ValuesExterior(18, 0.1, 1.2, 0.1)

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
        datasToSend = valuesExterior()
        return render_template('valuation.html',dolar = indicators , datasToSend = datasToSend)
    else:
        return render_template('valuation.html',dolar = indicators)



@app.route('/showvaluation' , methods = ['post' , 'get'])
def showvaluation():
    dados  = request.form
    initialValues = funcValuation()
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

@app.route('/login')
def login():
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

