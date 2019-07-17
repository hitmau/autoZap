#! /usr/bin/env python
#encoding: utf-8
#coding: utf-8
#Autor: Mauricio Rodrigues
import urllib as ur
import cgi
#import urllib.request as ur
#
#   Busca CEP
#
def buscaCep(cep):
    """
    Inserir cep (entrada como string).
    retorno: rua + " " + end, bairro, cidade, ufs(str(uf.strip()))
    buscaCep[0] = endereco.
    buscaCep[1] = cidade.
    buscaCep[2] = bairro.
    buscaCep[3] = estado.

    Caso não exista retorna campos vazios.
    """
    cep_busca = cep.replace('.','')
    cep_busca = cep_busca.replace('-','')
    cep_busca = cep_busca.replace(' ','')
    #cep_busca   = '24804718';
    url         = "http://cep.republicavirtual.com.br/web_cep.php?cep="+ str(cep_busca) + "&formato=query_string"
    pagina      = ur.urlopen(url)
    conteudo    = pagina.read().decode('utf-8')
    resultado   = cgi.parse_qs(conteudo)

    if resultado['resultado'][0] == '1':
        #print("Endereço com cidade de CEP único: ")
        #rua = rua.encode("utf-8")
        rua = resultado['tipo_logradouro'][0]
        #print(rua)
        #end = end.encode("utf-8")
        end = resultado['logradouro'][0]
        #print(end)
        #bairro = bairro.encode("utf-8")
        bairro = resultado['bairro'][0]
        #print(bairro)
        #cidade = cidade.encode("utf-8")
        cidade = resultado['cidade'][0]
        #print(cidade)
        #uf = uf.encode("utf-8")
        uf = resultado['uf'][0]
        #print(uf)
        return rua + " " + end, bairro, cidade, ufs(str(uf.strip()))

    elif resultado['resultado'][0] == '2':
        #print ("Endereço com cidade de CEP único: ")
        cidade = resultado['cidade'][0]
        uf = resultado['uf'][0]
        return ' ' ,' ', cidade, ufs(str(uf.strip()))
    else:
        return ' ',' ',' ',' '

def ufs(string):
    """
    Funcao usf
    Inserir uf (com 2 difitos em maiúsculo).
    retorno: descrição do Estado completo.
    """
    if string == 'AC':
    	return 'Acre'
    elif string == 'AL':
    	return 'Alagoas'
    elif string == 'AP':
    	return 'Amapa'
    elif string == 'AM':
    	return 'Amazona'
    elif string == 'BA':
    	return 'Bahia'
    elif string == 'CE':
    	return 'Ceara'
    elif string == 'DF':
    	return 'Distrito Federal'
    elif string == 'ES':
    	return 'Espírito Santo'
    elif string == 'GO':
    	return 'Goiás'
    elif string == 'MA':
    	return 'Maranhão'
    elif string == 'MT':
    	return 'Mato Grosso'
    elif string == 'MS':
    	return 'Mato Grosso do Sul'
    elif string == 'MG':
    	return 'Minas Gerais'
    elif string == 'PA':
    	return 'Pará'
    elif string == 'PB':
    	return 'Paraíba'
    elif string == 'PR':
    	return 'Parana'
    elif string == 'PE':
    	return 'Pernambuco'
    elif string == 'PI':
    	return 'Piauí'
    elif string == 'RJ':
    	return 'Rio de Janeiro'
    elif string == 'RN':
    	return 'Rio Grande do Norte'
    elif string == 'RS':
    	return 'Rio Grande do Sul'
    elif string == 'RO':
    	return 'Rondônia'
    elif string == 'RR':
    	return 'Roraima'
    elif string == 'SC':
    	return 'Santa Catarina'
    elif string == 'SP':
    	return 'São Paulo'
    elif string == 'SE':
    	return 'Sergipe'
    elif string == 'TO':
    	return 'Tocantins'

#print(buscaCep(24800000))
