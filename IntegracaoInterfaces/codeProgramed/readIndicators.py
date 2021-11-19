
#Implementar classe para buscar os indicadores

class Indicators:
    import json
    import requests
    import os

    navegador = {
        "User-agent" : "Chrome"
    }

    url = f'https://api.hgbrasil.com/finance?key=cecacfc8'
    data = requests.get(url=url, headers=navegador)
    todo = json.loads(data.content)
    moedas = todo['results']['currencies']
    dolar = moedas['USD']
    euro = moedas['EUR']
    taxa_juro = todo['results']['taxes']
    selic = taxa_juro[0]['selic']
    bolsa_valores = todo['results']['stocks']
    ibovespa = bolsa_valores['IBOVESPA']


    # logo = """
    # ======================================================================
    #                         FG Analise Financeira
    # ======================================================================"""

    os.system('cls')

    def cabecalho():
        logo = """
    ======================================================================
                            FG Analise Financeira
    ======================================================================""" #70 sinais de =
        print(logo)
        print("Fechamento do ultimo dia util")
        print(f"Dolar: R${round(dolar['buy'],2)}\tEuro: R${round(euro['buy'],2)}\tSelic: {round(selic,2)}%\tIbovespa: {round(ibovespa['variation'],2)}%")
        print("----------------------------------------------------------------------")




