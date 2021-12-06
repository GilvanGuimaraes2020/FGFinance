

from flask import Flask , render_template , request, session
from flask_material import Material

import connectionDataBase.connectionBD as BD
import connectionDataBase.validConection as VC
from valuation.exteriorStocksValues import datasCompaniesExt as dcExt , ValuesExterior as vext
from valuation.executeValuation import initialValues
from lists.classesBD import connBD as classBD
from setDados.setDatasValuation import extValuation as setValues
import getFiles.exportFile  as exportFile
import indicators.readIndicators as readIndicators

indicators = readIndicators.Indicators()

def initialState(ticker):
    return readIndicators.readData.teste(ticker)

def funcValuation(dados):
    sendDados = setValues(dados)
    return initialValues(sendDados)

def extValuation(dados):
    sendDados = setValues(dados)
    return vext(sendDados)

def resultCash(gainCash , debtCash):
    profit = gainCash[4] - debtCash[4] 
    return profit



app = Flask(__name__)

app.config['TITLE'] = 'FINANCAS'

Material(app)

@app.route('/')
def index():
   return render_template('index.html' , dolar = indicators)

@app.route('/login' , methods = ['post' , 'get'])
def login():
    error = None
    if request.method == "POST":
        allow_access = VC.validUser(request.form['usuario'], request.form['senha'])
        print (allow_access)
        if allow_access:
            session['username'] = request.form['usuario']
            return render_template('dashboard.html', dolar = indicators)
        else:
            allow_access = False
            error = 'Invalid username/password'
            return render_template('login.html' ,error = error)
    else:
        return render_template('login.html')
    

@app.route('/userRegister' , methods = ['post' , 'get'])
def userRegister():
    if request.method == 'POST':
        metodo = "salvar"
        datas_DB = request.form
        ids = 0
        user_to_bd = classBD('', '', '', '', '', '', '','', datas_DB['usuario'] ,datas_DB['email'], datas_DB['senha'])

        BD.saveDatas(user_to_bd ,metodo, "usuario" , ids)
        return render_template('login.html')
    else:
        return render_template('userRegister.html')


@app.route('/about' , methods = ['GET' , 'POST'])
def about():
    if session['username']:        
        return render_template('about.html',dolar = indicators)
    else:
        return render_template('login.html')

@app.route('/valuation' , methods = ['post' , 'get'])
def valuation():
    if session['username']:
        requestHtml = request.args
        
        if requestHtml:   
            ticker = requestHtml['ticker']
            dtsExt =  dcExt(ticker)    
            dtsExt.cashFlow() #ebit e ebitda
            dtsExt.overview() #quantidade de açoes 
            dtsExt.balance()#caixa equivalente e o capital de giro
            dtsExt.debt()               
            #retorna o caixa da empresa
            cash = resultCash(dtsExt.cashAndEquivalent , dtsExt.debtCash)
                
            
            return render_template('valuation.html',dolar = indicators,
            over = dtsExt.quantityStock , ebit = dtsExt.ebit, 
            ebitda = dtsExt.ebitda, cash = cash,
            working = dtsExt.workingCapital , 
            ticker = ticker)        
        else:
            return render_template('valuation.html',dolar = indicators)
    else:
        return render_template('login.html')

@app.route('/showvaluation' , methods = ['post' , 'get'])
def showvaluation():
    if session['username']:
        dados  = request.form

        if request.method == "POST":
            if dados['setExterior']:
                metodo = "salvar"
                ids = 0
                ivalues = extValuation(dados)
            elif dados['idValuation']:
                metodo = "atualizar"
                ids = [dados['idValuation'],dados['idebit'],dados['idebitda'], dados['idncl']]
                ivalues = extValuation(dados)
                
            else:
                metodo = "salvar"
                ivalues = funcValuation(dados)
                
            ivalues.flows()  
            value_to_bd = classBD(
                ivalues.ebit, ivalues.ebitda,
                ivalues.ncl , ivalues.quantityStock,
                ivalues.enterprise,ivalues.equity, dados['setExterior'],
                ivalues.stockPrice , '' ,''
            ) 
            BD.saveDatas(value_to_bd , metodo , "valuation", ids)  
            return render_template('showvaluation.html', dolar=indicators, ivalues = ivalues, dados = dados)
        else:
            return render_template('showvaluation.html', dolar=indicators)
    else:
        return render_template('login.html')



@app.route('/dashboard', methods = ['post' , 'get'])
def dashboard():
    if session['username']:
        (labels , values , volume ) = initialState("PETR4.SA")
        
        return render_template('dashboard.html',  dolar = indicators,
        labelsData=labels,valuesData = values, volume = volume )
    else:
        return render_template('login.html')


#pular 14, 22 , 29 , 0 a 8 val - 9 a 15 ebit - 16 a 22 ebitda - 23 a 29 ncl
@app.route('/listDatas' , methods=['post' , 'get'])
def listDatas():
    if session['username']:
        requesthtml = request.args
        if requesthtml: 
            returnBd = BD.action_on_bd(requesthtml)
            rbd = returnBd[0]
            if len(returnBd[0]) > 20:
                return render_template('updateValuation.html',dolar = indicators, rbd = rbd)
            
        rows = BD.consultDatas()
        
        return render_template('listDatasBD.html', dolar = indicators, rows = rows )
    else:
        return render_template('login.html')

@app.route('/exportFiles' , methods = ['post' , 'get'])
def exportFiles():
    if session['username']:
        dados  = request.form
        
        if (dados['method'] == "json"):
            exportFile.jsonCreate(dados)
        elif (dados['method'] == "csv"):
            exportFile.csvCreate(dados['stockPrice'] , dados['enterpriseValue'])     
        else:
            print("Sem dados")
        
        return render_template('exportFiles.html', dolar=indicators)
    else:
        return render_template('login.html')

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.run(debug=True)

