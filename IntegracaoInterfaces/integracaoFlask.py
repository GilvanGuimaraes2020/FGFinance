from flask import Flask , render_template
from flask_material import Material

app = Flask(__name__)
app.config['TITLE'] = 'FINANCAS'
Material(app)

@app.route('/')
def index():
    products = ['Baguete', 'Ciabata', 'Pretzel']
    return render_template('index.html' , products=products )

@app.route('/simulation')
def simulation():
    data=[
        ("01/01/2021" , 1000),
        ("02/01/2021", 1300),
        ("03/01/2021", 1400),
        ("04/01/2021", 1500),
        ("05/01/2021", 1800),
        ("06/01/2021", 1900),
        ("07/01/2021", 2000)
    ]

    labelsData = [row[0] for row in data]
    valuesData= [row[1] for row in data]

    return render_template('simulation.html', labelsData=labelsData, valuesData = valuesData)

"""
@app.route('/pessoas/<string:nome>/<string:cidade>')
def pessoa(nome , cidade):
    #return '<h1> Nome: {}, cidade: {} </h1>'.format(nome , cidade)
    return jsonify({'nome':nome , 'cidade':cidade}) """

app.run(debug=True)

