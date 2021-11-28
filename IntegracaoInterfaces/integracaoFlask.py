from flask import Flask , render_template , request
from flask_material import Material
import os

import executeValuation

import readIndicators

""" executeValuation(24 , 0.03, 0.065, 1.2, 0.1) """

indicators = readIndicators.Indicators()
graphicDatas = readIndicators.readData("IBOV.SA")
labelsData = graphicDatas.datas 
valuesData= graphicDatas.dados

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

@app.route('/valuation')
def valuation():
    return render_template('valuation.html',dolar = indicators)


@app.route('/showvaluation' , methods = ['post' , 'get'])
def showvaluation():
    dados  = request.form
    initialValues = executeValuation.initialValues(24 , 0.03, 0.065, 1.2, 0.1)
    return render_template('showvaluation.html', dolar=indicators, valuation = initialValues , dados = dados)

@app.route('/userRegister')
def userRegister():
    return render_template('userRegister.html',dolar = indicators)

@app.route('/dashboard', methods = ['post' , 'get'])
def dashboard():
    ticker = "PETR4.SA"
    graphicDatasGenerico = readIndicators.readData(ticker)
    graphicDatasIBOV = readIndicators.readData("IBOV.SA")
    return render_template('dashboard.html',graphicDatasIBOV=graphicDatasIBOV, graphicDatasGenerico=graphicDatasGenerico, ticker=ticker, dolar = indicators)

@app.route('/login')
def login():
    return render_template('login.html' )

@app.route('/simulation')
def simulation():
    aux = []
    return render_template('simulation.html', labelsData=labelsData, valuesData = valuesData ,dolar = indicators , auxs = aux)


app.run(debug=True)

