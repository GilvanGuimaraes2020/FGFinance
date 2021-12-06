
from re import S
import psycopg2


from lists.message import *
def connection():
    pg = psycopg2
    try:
        con = pg.connect(
            database = "provanp2_tei",
            user = "postgres",
            password = "FTC2019@Gil#",
            host = "127.0.0.1",
            port = "5432"
        )
        print ("Conexao realizado com sucesso")
        return con

    except Exception as erro:
        print (erro)

def saveUser(dados , sql):
    try:
        con = connection()
        cur = con.cursor()
        tupla = tuple(dados)
        cur.execute(sql , (tupla,))
        con.commit()
        print ("Dados inserido com sucesso")
        
        con.close()
        return True
    except Exception as erro:
        print (erro)
        return False

def saveData(dado , sql , ticker):
    try:
        con = connection()
        cur = con.cursor()  
        tupla = tuple(dado)
        
        tupla +=  (ticker ,)  
        print (tupla)    
        cur.execute(sql , (tupla,))
        id = cur.fetchone()[0]
        con.commit()
        print ("Dados inserido com sucesso")        
        con.close()
        return id
    except Exception as erro:
        print (erro)
        return 0


def saveDatas(Bd , metodo, table, ids):
    
    message = messagesBD(metodo , table)
    
    if table == "valuation":
        tb = " tb_ebit "
        sql = message[0] + tb + message[1] + message[3]
        print (sql)
        ticker = Bd.ticker
                
        id_ebit = saveData(Bd.ebit, sql , ticker )
        print (id_ebit)

        tb = " tb_ebitda "
        sql =  message[0] + tb + message[1] + message[3]

        id_ebitda = saveData(Bd.ebitda ,sql, ticker)
        print (id_ebitda)

        tb = " tb_ncl "
        sql =  message[0] + tb + message[1] + message[3]
        
        id_cg = saveData(Bd.ncl ,sql , ticker) 
        print (id_cg)
        tb = " tb_valuation "
        sql =  message[0] + tb + message[2] + message[3]
        
        dados = [Bd.stocks , id_ebit, id_ebitda, id_cg, Bd.enterprise, Bd.equity, Bd.price]
        id_value = saveData(dados, sql , ticker)
        print (id_value)
    elif table == "usuario":
        
        sql = message[0] +  message[1] + message[2]
        print (sql)
        dados = [Bd.nm_usuario , Bd.email, Bd.senha]
        confUser = saveUser(dados , sql)
    else:
        return False

def consultDatas():
    try:
        con = connection()
        cur = con.cursor()
        sql = """SELECT * FROM tb_valuation;"""
        
        cur.execute(cur.mogrify(sql))
        rows = cur.fetchall()
        con.commit()
               
        con.close()
        return rows
    except Exception as erro:
        print (erro)

def delete(idDelete):
    try:
        con = connection()
        cur = con.cursor()
        sql = """DELETE FROM tb_valuation WHERE (id_empresa) = (%s);"""
        cur.execute(cur.mogrify(sql , (idDelete[0])))
        con.commit()
        print ("Dados Deletado com sucesso")
        
        con.close()
        return ("Dados Deletado")
    except Exception as erro:
        print (erro)

def action_on_bd(dados):
    for d in dados:
        chave = d    
    if chave == "idDelete": 
        return delete (dados[chave])
    elif chave == "idUpdate":
       return search_to_update(dados[chave])


def search_to_update(idEmpresa):

    try:
        con = connection()
        cur = con.cursor()
        sql = """SELECT *
         FROM tb_valuation v
         JOIN tb_ebit e ON e.id_empresa = v.ebit
         JOIN tb_ebitda da ON da.id_empresa = v.ebitda
         JOIN tb_ncl n ON n.id_empresa = v.ncl
         WHERE v.id_empresa = (%s);"""
        
        cur.execute(cur.mogrify(sql , (idEmpresa)))
        rows = cur.fetchall()
        con.commit()
        con.close()
        return rows
    except Exception as erro:
        print (erro)

""" y = b','.join(cur.mogrify("(%s,%s,%s,%s,%s,{ticker})", x ) for x in ebit)
        insert = sql + y.decode() """