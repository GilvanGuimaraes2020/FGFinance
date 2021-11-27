from flask import Flask , render_template 
from flask_material import Material
import os

import readIndicators

indicators = readIndicators.Indicators()


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
    return render_template('valuation.html',dolar = indicators )

@app.route('/userRegister')
def userRegister():
    return render_template('userRegister.html',dolar = indicators )

@app.route('/dashboard', methods = ['post' , 'get'])
def dashboard():
    return render_template('dashboard.html',dolar = indicators )

@app.route('/login')
def login():
    return render_template('login.html' )

@app.route('/simulation')
def simulation():
   
    graphicDatas = readIndicators.readData("IBOV.SA")
    labelsData = graphicDatas.datas 
    valuesData= graphicDatas.dados
    aux = []

    return render_template('simulation.html', labelsData=labelsData, valuesData = valuesData ,dolar = indicators , auxs = aux)

"""
@app.route('/pessoas/<string:nome>/<string:cidade>')
def pessoa(nome , cidade):
    #return '<h1> Nome: {}, cidade: {} </h1>'.format(nome , cidade)
    return jsonify({'nome':nome , 'cidade':cidade}) """

app.run(debug=True)


