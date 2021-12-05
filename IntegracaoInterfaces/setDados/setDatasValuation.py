import re


def extValuation(dados):
    ebit = [float(v) for (k ,v) in dados.items() if re.search("\\bebit.\\b", k)]
    ebitda = [float(v) for (k ,v) in  dados.items() if "ebitda" in k ]
    ncg = [float(v) for (k ,v) in dados.items() if "cg" in k]
    stocks = int(dados['stocks'])
    ir = int(dados['IR'])
    growth = int(dados['growth'])
    reinvest = float(dados['reinvest'])
    cash = float(dados['cash'])
    return {'ebit':ebit, 'ebitda' : ebitda, 
    'ncg' :ncg, 'stocks' : stocks, 'IR' : ir,
    'growth' :growth, 'reinvest' : reinvest,
    'cash' : cash}    