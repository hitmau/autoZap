# -*- Coding: UTF-8 -*-
#coding: utf-8
import pymysql.cursors
import base64
#print("inicio")
# Connect to the database
connection = pymysql.connect(host='localhost',user='root',db='bd',charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()

def abrirConexao():
    try:
        global connection, cursor
        connection = pymysql.connect(host='localhost',user='root',db='bd',charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        cursor = connection.cursor()
        print("Abrindo conexão!")
    except:
        print ("Erro: Impossível abrir conexão!")
#print("cursor")
# Esta senteça SQL seleciona toda a tabela tb_fornecedores.

def consultaContato(codusuario, dado = '0'):
    """
    consultaContato(tabela, dado = '0'):
    dado: sem passar parametro (codcontato), será retornado uma lista.
    """
    global connection, cursor
    abrirConexao()
    if dado != '0':
        sql = 'SELECT * FROM contato where codusuario = ' + str(codusuario) + ' and codcontato = ' + str(dado) + ';'
    else:
        sql = 'SELECT * FROM contato where codusuario = ' + str(codusuario) + ';'
    #print("sql")
    try:
        # Execute o comando SQL
        cursor.execute(sql)
        # le todas as linhas da tabela.
        linhas = cursor.fetchall()
        #print sql
        #print (linhas)
        retorno = []
        for linha in linhas:
            idcontatoX = linha['codcontato']
            nomeX = linha['nome']
            ativoX = linha['ativo']
            telefoneX = linha['telefone']
            cadastroX = linha['cadastro']
            retorno.append([idcontatoX, nomeX, ativoX, telefoneX, cadastroX])

        fechaConexao()
        return retorno
    except:
        print ("Erro: Impossível obter dados (consultaContato)")
    # fecha a conexão
    #connection.close()

def insereContato(nome, ativo = 'N', cadastro = '', telefone = ''):
    """
    insereContato(nome, ativo = 'N')
    nome = Qual nome será inserido
    ativo = S "ativo", vazio ou N "inativo"
    """
    global connection, cursor
    abrirConexao()
     #instancia um objeto cursor utilizando o método cursor
    cursor = connection.cursor()
    print("insert " + str(nome))
    # construção da string SQL que insere um registro.
    sql = "insert into bd.contato (codcontato, nome, ativo, cadastro, telefone) value ((select max(a.codcontato) + 1 from bd.contato a), '" + str(nome) + "', '" + str(ativo.upper()) + "' , '" + str(cadastro) + "', '" + str(telefone) + "');"

    try:
        # Execute o comando
        cursor.execute(sql)
        # Confirme a inserção na base de dados
        connection.commit()
        fechaConexao()
        retorno = True
    except:
        # limpe tudo se algo saiu errado
        connection.rollback()
        retorno = False
        print("Erro na inserção de dados na tabela de contatos")

    # fecha a conexão
    #connection.close()
    return retorno

def atualizaContato(old, new, nome, tel, cadastro, ativo):
    """
    atualizaContato(old, new)
    old = codcontato antivo (que será atualizado)
    new = novo nome
    nome, tel, cadastro, ativo
    """
    global connection, curso
    abrirConexao()
    # Esta senteça SQL atualiza todas as linhas do banco.
    # no caso so temos uma linha
    sql = "update contato SET nome = '" + str(new) + "', telefone = '" + str(tel) + "', cadastro = '" + str(cadastro) + "', ativo =  '" + str(ativo) + "' where codcontato = " + str(old) + ";"
    print(sql)
    try:
        # Execute o comando SQL
        cursor.execute(sql)
        # confirme
        connection.commit()
        fechaConexao()
        retorno = True
    except:
        retorno = False
        print ("Erro: Impossível atualizar")
        #cancela operações
        connection.rollback()

    # fecha a conexão
    #connection.close()
    return retorno

def consultaEntrada(codusuario, dado = '0'):
    """
    consultaEntrada(tabela, dado = '0'):
    dado: sem passar parametro (codcontato), será retornado uma lista.
    Ordem: codinteracaoI, tipoI, entradaI, codsaidaS, tipoS, saidaS, ativoS
    """
    global connection, cursor
    abrirConexao()
    try:
        #print("consultaEntrada")
        if dado != '0':
            sql = "select i.codinteracao as codinteracaoI, i.tipo as tipoI, i.entrada as entradaI, s.codsaida as codsaidaS, s.tipo as tipoS, s.saida as saidaS, s.ativo as ativoS, ps.ativo from interacao i left join saida s on (i.codinteracao = s.codinteracao) inner join parametros pt on (pt.tipo = s.tipo) inner join parametros ps on (ps.tipo = pt.parametro  and ps.ativo = 'S' and ps.parametro = 'servconv') where s.ativo = 'S' and  i.ativo = 'S' and i.codusuario = " + str(codusuario) + " and i.codinteracao = " + str(dado) + " order by 2;"
        else:
            sql = "select i.codinteracao as codinteracaoI, i.tipo as tipoI, i.entrada as entradaI, s.codsaida as codsaidaS, s.tipo as tipoS, s.saida as saidaS, s.ativo as ativoS, ps.ativo from interacao i left join saida s on (i.codinteracao = s.codinteracao) inner join parametros pt on (pt.tipo = s.tipo) inner join parametros ps on (ps.tipo = pt.parametro  and ps.ativo = 'S' and ps.parametro = 'servconv') where s.ativo = 'S' and  i.ativo = 'S' and i.codusuario = " + str(codusuario) + " order by 2;"
        #Execute o comando SQL
        cursor.execute(sql)
        # le todas as linhas da tabela.
        linhas = cursor.fetchall()
        #print sql
        #print (linhas)
        retorno = []
        for linha in linhas:
            codinteracaoI = linha['codinteracaoI']
            tipoI = linha['tipoI']
            entradaI = linha['entradaI']
            codsaidaS = linha['codsaidaS']
            tipoS = linha['tipoS']
            saidaS = linha['saidaS']
            ativoS = linha['ativoS']
            retorno.append([codinteracaoI, tipoI, entradaI, codsaidaS, tipoS, saidaS, ativoS])
        fechaConexao()
        #print(retorno)
        return retorno
    except:
        print ("Erro: Impossível obter dados (consultaEntrada)")
    # fecha a conexão
    ##connection.close()

def insereEntrada(nome, ativo = 'N'):
    """
    insereContato(nome, ativo = 'N')
    nome = Qual nome será inserido
    ativo = S "ativo", vazio ou N "inativo"
    """
    global connection, cursor
    abrirConexao()
     #instancia um objeto cursor utilizando o método cursor
    cursor = connection.cursor()

    # construção da string SQL que insere um registro.
    sql = "insert into bd.contato (codcontato, nome, ativo) value ((select max(a.codcontato) + 1 from bd.contato a), '" + str(nome) + "', '" + str(ativo.upper()) +"');"

    try:
        # Execute o comando
        cursor.execute(sql)
        # Confirme a inserção na base de dados
        connection.commit()
        fechaConexao()
        retorno = True
    except:
        # limpe tudo se algo saiu errado
        connection.rollback()
        retorno = False
        print("Erro na inserção de dados na tabela de fornecedores")

    # fecha a conexão
    #connection.close()
    return retorno

def insereImagem(foto):
    """
    insereContato(nome, ativo = 'N')
    nome = Qual nome será inserido
    ativo = S "ativo", vazio ou N "inativo"
    """
    global connection, cursor
    abrirConexao()
    with open(foto, 'rb') as f:
        photo = f.read()
    encodestring = base64.b64encode(photo)
    sql = "insert INTO imagem (codusuario, imagem) VALUES ('0',%s);"
    #args = (encoded_string, )

     #instancia um objeto cursor utilizando o método cursor
    cursor = connection.cursor()
    #encodestring = base64.b64encode(encoded_string)
    # construção da string SQL que insere um registro.

    #print(sql)
    try:
        # Execute o comando
        cursor.execute(sql,(encodestring,))
        # Confirme a inserção na base de dados
        connection.commit()
        fechaConexao()
        retorno = True
    except:
        # limpe tudo se algo saiu errado
        connection.rollback()
        retorno = False
        print("Erro na inserção de dados na tabela de Imagem")

    # fecha a conexão
    #connection.close()
    return retorno

def atualizaEntrada(new, old):
    """
    atualizaContato(new, old)
    new = novo nome
    old = codcontato antivo (que será atualizado)
    """
    global connection, curso
    abrirConexao()
    # Esta senteça SQL atualiza todas as linhas do banco.
    # no caso so temos uma linha
    sql = "UPDATE contato SET nome = '" + str(new) + "' where codcontato = " + str(old)
    #print(sql)
    try:
        # Execute o comando SQL
        cursor.execute(sql)
        # confirme
        connection.commit()
        fechaConexao()
        retorno = True
    except:
        retorno = False
        print ("Erro: Impossível atualizar")
        #cancela operações
        connection.rollback()

    # fecha a conexão
    #
    return retorno

def fechaConexao():
    global connection, cursor
    connection.close()

def inteiro(numero):
    try:
        num = int(numero)
        return True
    except:
        return False

def consultaParametro(codusuario, tipo):
    """
    consultaParametro(tabela, dado = '0'):
    entrada: Qual o parametro irá consultar.
    dado: sem passar parametro (codcontato), será retornado uma lista.
    T = contatos
    S = servidor
    C = Conversar
    """
    global connection, cursor


    try:
        if bool(inteiro(codusuario)):
            abrirConexao()
            sql = "SELECT p.ativo, p.tipo FROM parametros p where p.tipo = '" + str(tipo) + "' and codusuario = " + str(codusuario) + ";"
            # Execute o comando SQL
            cursor.execute(sql)
            # le todas as linhas da tabela.
            linhas = cursor.fetchall()
            print(sql)
            print(linhas)
            retorno = []
            for linha in linhas:
                ativo = linha['ativo']
                retorno = ativo
            fechaConexao()
            if retorno == "S":
                retorno = True
            #print(retorno)
            return retorno
        else:
            return False
    except:
        print ("Erro: Impossível obter dados (consultaParametro)")

def consultaLogin():
    """
    consultaParametro(tabela, dado = '0'):
    entrada: Qual o parametro irá consultar.
    dado: sem passar parametro (codcontato), será retornado uma lista.
    """
    global connection, cursor
    abrirConexao()
    sql = "SELECT * from login where start = 'S'"
    try:
        # Execute o comando SQL
        cursor.execute(sql)
        # le todas as linhas da tabela.
        linhas = cursor.fetchall()
        #print sql
        #print (linhas)
        retorno = []
        for linha in linhas:
            codusuario = linha['codusuario']
            start = linha['start']
            status = linha['status']
            retorno.append([codusuario, start, status])
        fechaConexao()
        return retorno
    except:
        print ("Erro: Impossível obter dados (consultaLogin)")
    # fecha a conexão
    #connection.close()
def atualizaLogin(codusuario):
    """
    atualizaContato(new, old)
    new = novo nome
    old = codcontato antivo (que será atualizado)
    """
    global connection, curso
    abrirConexao()
    # Esta senteça SQL atualiza todas as linhas do banco.
    # no caso so temos uma linha
    sql = "UPDATE login SET status = 'S' where codusuario = " + str(codusuario)

    try:
        # Execute o comando SQL
        cursor.execute(sql)
        # confirme
        connection.commit()
        fechaConexao()
        retorno = True
    except:
        retorno = False
        print ("Erro: Impossível atualizar")
        #cancela operações
        connection.rollback()

def resetLogin():
    """
    atualizaContato(new, old)
    new = novo nome
    old = codcontato antivo (que será atualizado)
    """
    global connection, cursor
    abrirConexao()
    # Esta senteça SQL atualiza todas as linhas do banco.
    # no caso so temos uma linha
    sql = "UPDATE login SET status = 'N'"

    try:
        # Execute o comando SQL
        cursor.execute(sql)
        # confirme
        connection.commit()
        fechaConexao()
        return True
    except:
        return False
        print ("Erro: Impossível resetar o Login")
        #cancela operações
        connection.rollback()
#print (consultaParametro())
#consultaParametro()
#print("mysql")
#for i in consultaParametro('T','0'):
#    print(i)
#print(consultaParametro(0,'T'))

#for i in consultaEntrada(47):
#    print(i)
#print(consultaParametro())
#print("Usuário " + str(consultaLogin()[0]))
#print("Ativo " + str(consultaLogin()[1]))
#print(insereImagem('/home/hitmau/teste.png'))
#print(resetLogin())
#print(consultaLogin())
