from os import curdir as cur
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

def create(nmUsuario , email):
    try:
        con = connection()
        cur = con.cursor()
        sql = """INSERT INTO tb_usuarios (nm_usuario , email) VALUES (%s , %s);"""
        
        cur.execute(cur.mogrify(sql , (nmUsuario , email)))
        con.commit()
        print ("Dados inserido com sucesso")
        
        con.close()
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

