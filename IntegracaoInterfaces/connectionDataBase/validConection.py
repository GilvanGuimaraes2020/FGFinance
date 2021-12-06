import connectionDataBase.connectionBD as BD

def validUser( usuario , senha):
    try:
        con = BD.connection()
        cur = con.cursor()
        sql = """SELECT nm_usuario , senha
         FROM tb_usuarios 
         WHERE (nm_usuario = %s AND senha = %s);"""
        
        cur.execute(cur.mogrify(sql , (usuario , senha)))
        row = cur.fetchone()
        con.commit()
        con.close()
        return True if row else False
    except Exception as erro:
        print (erro)
        return False
