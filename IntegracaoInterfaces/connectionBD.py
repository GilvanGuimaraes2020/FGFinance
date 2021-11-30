import psycopg2

pg = psycopg2
try:
    con = pg.connect(
        database = "tb_livraria",
        user = "postgres",
        password = "postgres",
        host = "127.0.0.1",
        port = "5432"
    )
    print ("Conexao realizado com sucesso")
    cur = con.cursor()
    #sql = """INSERT INTO tb_livro (id_editora, titulo) VALUES (1 ,'PYTHON COOKBOOK');"""
    #cur.execute(sql)
    #sql = "INSERT INTO tb_livro (id_editora, titulo) VALUES ( %s ,%s);"
    """sql = "INSERT INTO tb_livro (id_editora, titulo) VALUES ( %s ,%s) RETURNING id_livro;"
    cur.execute(cur.mogrify(sql, (1 , 'PYTHON ADVANCED')))
    id = cur.fetchone()[0]
    print("ID = %s" %id)

    con.commit()
    print("Tabela criada com sucesso")"""

    sql = "SELECT * FROM tb_livro"
    cur.execute(sql)
    linhas = cur.fetchall()
    for linha in linhas:
        print("ID = %d" %linha[0])
        print("Titulo = %s" %linha[2])
   

    sql = "UPDATE tb_livro SET titulo = %s WHERE id_livro = %s"
    cur.execute(cur.mogrify(sql , ('BANCO DE DADOS' , 6)))

    con.commit()
    print("Total linhas atualizadas: %s" %cur.rowcount)

    sql = "DELETE FROM tb_livro WHERE id_livro = %s"
    cur.execute(cur.mogrify(sql , "5"))
    print("Total linhas atualizadas: %s" %cur.rowcount)
    con.commit()

    con.close()




except Exception as erro:
    print (erro)


"""CREATE TABLE tb_livro (
        id_livro integer NOT NULL AUTOINCREMENT,
        id_editora INTEGER,
        titulo varchar(255)
        CONSTRAINT pk_tb_livro_id_livro PRIMARY KEY (id_livro) ,
        CONSTRAINT fk_tb_livro_id_editora FOREIGN KEY (id_editora) REFERENCE
        tb_editora(id_editora)
        );"""