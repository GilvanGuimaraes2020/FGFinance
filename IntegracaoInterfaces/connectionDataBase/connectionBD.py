
import psycopg2
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


def saveDatas(Bd , table):
    
    if table == "valuation":
        
        ticker = Bd.ticker
        
        sql = """INSERT INTO tb_ebit
        (ano1 , ano2, ano3, ano4, ano5, ticker) 
        VALUES %s  RETURNING id_empresa; """
        
        id_ebit = saveData(Bd.ebit, sql , ticker )
        print (id_ebit)

        sql = """INSERT INTO tb_ebitda
        (ano1 , ano2, ano3, ano4, ano5, ticker) 
        VALUES %s  RETURNING id_empresa; """

        id_ebitda = saveData(Bd.ebitda ,sql, ticker)
        print (id_ebitda)

        sql = """INSERT INTO tb_ncl
        (ano1 , ano2, ano3, ano4, ano5, ticker) 
        VALUES %s  RETURNING id_empresa; """
        
        id_cg = saveData(Bd.ncl ,sql , ticker) 
        print (id_cg)

        sql = """INSERT INTO tb_valuation
        (qtd_acoes , ebit, ebitda, ncl, valor_empresa, valor_patrimonial, valor_acao, ticker) 
        VALUES %s  RETURNING id_empresa; """

        dados = [Bd.stocks , id_ebit, id_ebitda, id_cg, Bd.enterprise, Bd.equity, Bd.price]
        id_value = saveData(dados, sql , ticker)
        print (id_value)
    elif table == "usuario":
        sql = """INSERT INTO tb_usuarios
        (nm_usuario , email) 
        VALUES %s  RETURNING id_usuario;"""
        dados = [Bd.nm_usuario , Bd.email]
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

def delete(idUsuario):
    try:
        con = connection()
        cur = con.cursor()
        sql = """DELETE FROM tb_usuarios WHERE (id_usuario) = (%s);"""
        
        cur.execute(cur.mogrify(sql , (idUsuario)))
        con.commit()
        print ("Dados Deletado com sucesso")
        
        con.close()
    except Exception as erro:
        print (erro)

def update(idUsuario , nmUsuario, email):
    try:
        con = connection()
        cur = con.cursor()
        sql = """UPDATE FROM tb_usuarios WHERE (id_usuario) = (%s);"""
        
        cur.execute(cur.mogrify(sql , (idUsuario)))
        con.commit()
        print ("Dados Deletado com sucesso")
        
        con.close()
    except Exception as erro:
        print (erro)

""" y = b','.join(cur.mogrify("(%s,%s,%s,%s,%s,{ticker})", x ) for x in ebit)
        insert = sql + y.decode() """