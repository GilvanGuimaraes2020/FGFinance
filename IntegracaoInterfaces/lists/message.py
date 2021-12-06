
def messagesBD(metodo , table):
    message = []
    if table == "valuation":
                
        if metodo == "salvar":
            message.insert(0 , "INSERT INTO ")
            message.insert(1 ,"(ano1 , ano2, ano3, ano4, ano5, ticker) VALUES %s ")
            message.insert(2 , "(qtd_acoes , ebit, ebitda, ncl, valor_empresa, valor_patrimonial, valor_acao, ticker) VALUES %s ")
            message.insert(3 , "RETURNING id_empresa; ")
                                
        elif metodo == "atualizar" :
            message.insert(0 , "UPDATE ")
            message.insert(1 , "SET ano1 = %s , ano2 = %s, ano3 = %s, ano4 = %s, ano5 = %s, ticker) WHERE id_empresa = %s ")
            message.insert(2 , "(SET qtd_acoes = %s , valor_empresa = %s, valor_patrimonial = %s, valor_acao %s, ticker) WHERE id_empresa = %s ")
            message.insert(3 , "RETURNING id_empresa; ")

    elif  table == "usuario":
        if metodo == "salvar":
            message.insert(0 , "INSERT INTO tb_usuarios ")
            message.insert(1 ,"(nm_usuario , email, senha) VALUES %s ")
            message.insert(2 , "RETURNING id_usuario; ")
        
        if metodo == "atualizar":
            message.insert(0 , "UPDATE tb_usuarios ")
            message.insert(1 ,"(SET nm_usuario = %s , email = %s, senha = %s) WHERE id_usuario = %s ")
            message.insert(2 , "RETURNING id_usuario; ")
    
    return message