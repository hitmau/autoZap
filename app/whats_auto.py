#!/usr/bin/env python
#encoding: utf-8
#coding: utf-8
#Autor Maurcio Rodrigues (mauriciosist@gmail.com)
#V 1.0.27
import mysql_zap as mysql
import novo_cadastro as nc
import busca_cep as cep

from selenium import webdriver
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os, platform, time, re, subprocess
import selenium.webdriver.support.ui as ui
import random, base64

try:
    from StringIO import StringIO
    from StringIO import BytesIO
except ImportError:
    from io import StringIO
    from io import BytesIO

from PIL import Image

from pyscreenshot import grab as img
#import pillow
#import commands
#import subprocess
# import selenium.webdriver.support.expected_conditions as EC
import unittest

class zap:
    def __init__(self, cod, tel):
        self.codusuario = cod
        self.tel = '+55 ' + str(tel[:2] + ' ' + tel[2:][:5] + '-' + tel[2:][5:])
        print("Usuario " , str(cod), ', telefone: ', self.tel)
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 600)
        self.imagem = 'C:/Users/hitma/Pictures/Saved Pictures/teste.png'
        #target = str(input('Enter name of person/group you want to send message to:'))
        self.target = str('Esposa Amada')
        #string = str(input('Enter your message: '))
        self.usarAqui = '_1WZqU PNlAR' #class
        self.mata = False
        self.string = str('oi teste')
        self.class_todos = '/html/body/div[1]/div/div/div[4]/div/header/div[2]/div/div/span'
        self.n = int(1)
        self.url = "https://web.whatsapp.com/"
        self.box = '_2UaNq' #//div[@class="_2wP_Y"]'
        self.nome = '_19RFN' # '//div[@class=""]'_1wjpf   _25Ooe
        self.ultmsg = '_2_LEW' # '//div[@class="_2_LEW"]'
        self.nummsg = '_1ZMSM' # '//div[@class="_1AwDx"]/div[2]' #'OUeyt' #
        self.textbox = '_3u328.copyable-text.selectable-text'
        self.dataHora = datetime.now()
        #self.dirarquivo = '/home/hitmau/Documentos/Projetos/python/whatsapp/'
        #self.arquivo = self.dirarquivo + "parametros.txt"
        #self.arquivoMeu = self.dirarquivo + "arquivoMeu.txt"
        #self.parametros = self.dirarquivo + "parametros.txt" #self.dirarquivo +
        self.target = '98031-7641' # número do dono do celular
        self.Nome_lista = '//span[contains(@title, '+ '"' + str(self.tel) + '"'+ ')]'
        self.buscaNome = '/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/input'
        #-----------------------------------------------------------------------------------------------------
        self.msgEntrada = '//div[contains(@class,"_1zGQT._2ugFP.message-in")]'
        self.msgSaida = '//div[contains(@class,"_1zGQT._2ugFP.message-out")]'
        #-----------------------------------------------------------------------------------------------------
        self.ultConvPrincipalMeu = '//span[contains(@class,"selectable-text invisible-space copyable-text")]'
        self.ultConvPrincipalContato = '//span[@class="selectable-text invisible-space copyable-text"]'
        self.ultHoraConvPrincipalMeu = '//span[contains(@class,"_3EFt_")]'
        self.nomePrincipal = '//div[contains(@class,"_3XrHh")]'
        self.primeiroNomeLista = ''
        #criado funcao para separar diretório de arquivo
        #self.dirScripts = '/home/hitmau/Documentos/Projetos/python/whatsapp/'
        #Comando a ser executado
        self.comando = ''
        #Nome do comendo que foi escrido, anterior ao comando que executa a tarefa
        self.terceiraLinha = ''
        self.segundaLinha = ''
        #entra na função de confirmação
        self.confirma = False

        self.confi = False
        #Definição de tipo de execução (> ou < ou -)
        self.defineTipo = ''
        #Texto para novo contato (cadastro)
        self.cadastroDeContato = 'Identificamos que seu cadastro nao existe em nossa base de dados. Gostaria de ser cadastrado? (S/N)'
        self.consultaEntradas = []
        self.consultaContato = []
        self.consultaContatoTodos = []
        self.consultaParametroContato = []
        self.listarComandos = []
        self.tentativaDeAcesso = 0
        #self.home()


    def consultas(self):
        #parametro add contato ativado ou desativado
        self.getConsultaContatos()
        self.getConsultaParametroContato()
        self.getConsultaEntrada()
        self.getListarComandos()
        self.getConsultaContatoTodos()

    def getListarComandos(self):
        self.listarComandos = mysql.listaComandos(self.codusuario)
        #print('self.listarComandos:: ' + str(self.listarComandos))
        return self.listarComandos

    def getConsultaEntrada(self, inteiro = '0'):
        self.consultaEntradas = mysql.consultaEntrada(self.codusuario, inteiro)
        #print('self.consultaEntradas:: ' + str(self.consultaEntradas))
        return self.consultaEntradas

    def getConsultaContatos(self, inteiro = 'C'):
        self.consultaContato = mysql.consultaContato(self.codusuario, inteiro)
        print('self.consultaContato:: ' + str(self.consultaContato))
        return self.consultaContato

    def getConsultaContatoCadastrado(self, inteiro):
        self.consultaContatoCadastrado = mysql.consultaContato(self.codusuario, inteiro)
        print('self.consultaContatoCadastrado:: ' + str(self.consultaContatoCadastrado))
        return self.consultaContatoCadastrado

    def getConsultaContatoTodos(self):
        self.consultaContatoTodos = mysql.consultaContato(self.codusuario)
        #print('self.consultaContato:: ' + str(self.consultaContatoTodos))
        return self.consultaContatoTodos

    def getConsultaParametroContato(self):
        try:
            self.consultaParametroContato = mysql.consultaParametro(self.codusuario, "T")
            print('self.consultaParametroContato:: ' + str(self.consultaParametroContato))
            return self.consultaParametroContato
        except:
            print("Erro em getConsultaParametroContato ou mysql.consultaParametro")

    def navegate(self):
        """
        Abre o browser e navega pelo endereco que esta contino na fariavel self.ult.
        Apos o browser abrir ele e minimizado.
        """
        self.driver.get(self.url)
        #print('Erro ' + str(e))
        #self.driver.minimize_window()
        #self.driver.maximize_window()

        #print('navegate')

    def qrCode(self):
        print("inicio do qrCode")
        try:
            #redimenssiona tela
            self.driver.get_window_size()
            #define novo tamanho para tela
            self.driver.set_window_size(800, 600)
            #armazena função para variavel
            png = self.driver.get_screenshot_as_png() # saves screenshot of entire page
            im = Image.open(BytesIO(png)) # uses PIL library to open image in memory
            #print da localidade pre definida
            im = im.crop((400, 130, 750, 440)) # defines crop points
            #salva imagem
            im.save(self.imagem)

        	#region.save('C:/wamp64/www/start/novo.jpg', 'JPEG', optimize=True, quality=95)

            mysql.insereImagem(self.imagem)
            print('antes')
            #tentativaDeAcesso é incrementado no metodo zerar
            if (self.tentativaDeAcesso >= 5):
                print('refresh na página para tentar novamente!')
                self.driver.refresh()
                self.tentativaDeAcesso = 0
                self.zerar('API whatsapp iniciada: ' + str(self.dataHora.day) + '/' + str(self.dataHora.month) + '/' + str(self.dataHora.year) + ' ' + str(self.dataHora.hour) + ':' + str(self.dataHora.minute))
            else:
                print('Tentativa: ' + str(self.tentativaDeAcesso) + '.')
                self.zerar('API whatsapp iniciada: ' + str(self.dataHora.day) + '/' + str(self.dataHora.month) + '/' + str(self.dataHora.year) + ' ' + str(self.dataHora.hour) + ':' + str(self.dataHora.minute))
            print('depois')
            #StaleElementReferenceException ,
        except (NoSuchElementException, TimeoutException) as ex:
            print("qrCode: " + str(ex))
            self.qrCode()

    def verificaNovoContato(self, string):
        """
        verificaNovoContato(self, string)
        entrada: string com novo contato, verifica se existe o + e se o proximo é numero.
        """
        nContato = string
        if str(nContato[0]) == '+' and bool(self.is_int(nContato[1])):
            return True
        else:
            return False
        print('novo contato encontrado, o que fazer!')


    def nomeEntra(self, stringEntrada = None):
        nomeS = stringEntrada
        print("entrou em nomes: " + nomeS)
        try:
            person_title = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//span[contains(@title, '+ '"' + nomeS + '"'+ ')]')))
            person_title.click()
            #print(str(self.consultaParametroContato))
            #print("-1-")
            if bool(self.consultaParametroContato):
                print("entra no addcontato-----------------------------------")
                if bool(self.verificaNovoContato(nomeS)): #verifica se tem os caracteres +1xxxxxxxxx
                    self.novoContato(nomeS)
        except Exception as ex:
            print("Tempo excedido ao zerar: " + str(ex))
            pass

    def novoContato(self, string):
        string = string.replace("+", "")
        string = string.strip(" ")
        string = string.replace(" ", "")
        cadastrado = True
        pergunta = False
        print(self.textPrincipal()[-2].lower())
        print('=')
        print(self.textResposta()[-1].lower())
        if (self.textPrincipal()[-1].lower() != self.cadastroDeContato.lower()):
            self.send(self.cadastroDeContato)
        if (self.textPrincipal()[-2].lower() == self.cadastroDeContato.lower() and (self.textResposta()[-1].lower() == 's' or self.textResposta()[-1].lower() == 'sim')):
            self.send('Nome completo?')
            self.send('E-mail?')
            self.send('Data de Nascimento (dd/mm/yyyy)?')
            self.send('Endereço?')
            self.send('Bairro?')
            self.send('Cidade?')
            self.send('Estado?')
            self.send('CEP')
        else:
            mysql.insereContato('','S','N',string,self.codusuario)

        for todosContatos in self.consultaContatos:
            print(todosContatos[1] + " - " + string)
            if todosContatos[1] == string:
                cadastrado = False
            if todosContatos[4] == "":
                if (self.textoPrincipal()[-2] == self.cadastroDeContato) and (self.textoPrincipal()[-1].lower() == 'sim'):
                    mysql.atualizaContato(old, new, nome, tel, cadastro, ativo)
                #else:
                #    grava n

        if bool(cadastrado):
            print("if not bool(cadastrado):")
            cadastrado = True
            print("inserido com sucesso: " + str(mysql.insereContato(string, "S")))
            self.send(self.cadastroDeContato)



        if bool(pergunta):
            print("if bool(pergunta):")
            pergunta = False
            if (self.textoPrincipal()[-2] == self.cadastroDeContato) and (self.textoPrincipal()[-1].lower() == 'sim'):
                print("vamos ao cadastro")
                self.sent("vamos ao cadastro")


        #
        #if (self.textPrincipal()[-1].lower() == 's' or self.textPrincipal()[-1].lower() == 'sim') and self.textPrincipal()[-2] == self.cadastroDeContato:
        #    self.send('Informe seu nome completo:')

    def zerar(self, string = ''):
        #print('zerar ini')
        try:
            print('buscanome: ', self.buscaNome)
            #Marca campo de busca
            buscas = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.buscaNome)))
            #Digita o telefone do usuario/admin
            buscas.send_keys(self.tel)
            print('clica no nome: ', self.Nome_lista)
            #Marca campo de busca
            person_title = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.Nome_lista)))
            #Clica no usuario encontrado
            person_title.click()
            #Obtem data e hora atual
            dataHora = datetime.now()
            #Envia data e hora atual pelo metodo send.
            if len(string) > 0:
                self.send('API whatsapp iniciada: ' + str(dataHora.day) + '/' + str(dataHora.month) + '/' + str(dataHora.year) + ' ' + str(dataHora.hour) + ':' + str(dataHora.minute))
            print('esc')
            #Remove busca
            buscas.send_keys(Keys.ESCAPE)
        except (TimeoutException, NoSuchElementException, StaleElementReferenceException) as ex:
            try:
                self.tentativaDeAcesso += 1
                self.qrCode()
            except:
                self.retornar()
                print("Tempo excedido ao zerar: " + str(ex))

#Função send envia a mensagem.
#Necessita que algum contato esteja selecionado.
    def send(self, string):
        #print('send ini')
        try:
            msg_box = self.driver.find_element_by_class_name(self.textbox)
            msg_box.send_keys(string)
            msg_box.send_keys(Keys.RETURN)
        except (NoSuchElementException, StaleElementReferenceException) as ex:
            self.zerar()
            print("Tempo excedido em send: " + str(ex))
            pass
        #print('send fim')

#Funcção textoPrincipal pega os textos das conversas, independente de quem enviou.
#Necessita que algum contato esteja selecionado.
    def textPrincipal(self):
        #print('textoPrincipal')
        conversa = []
        try:
            person_title = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.msgEntrada)))
            for uconv in self.driver.find_elements_by_xpath(self.msgEntrada):
                conversa.append(uconv.text)
                #print("teste 1" + str(uconv.text))
        except (TimeoutException, StaleElementReferenceException) as ex:
            print("Erro function textPrincipal: " + str(ex))
            self.zerar()
            for uconv in self.driver.find_elements_by_xpath(self.msgEntrada):
                conversa.append(uconv.text)
                #print "teste 2" + str(uconv.text)
        return conversa

    def textResposta(self):
        #print('textoPrincipal')
        conversa = []
        try:
            person_title = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.msgSaida)))
            for uconv in self.driver.find_elements_by_xpath(self.msgSaida):
                conversa.append(uconv.text)
                #print("teste 1" + str(uconv.text))
        except (TimeoutException, StaleElementReferenceException) as ex:
            print("Erro function textPrincipal: " + str(ex))
            self.zerar()
            for uconv in self.driver.find_elements_by_xpath(self.msgSaida):
                conversa.append(uconv.text)
                #print "teste 2" + str(uconv.text)
        return conversa

    def _get_boxes(self):
        print('_get_boxes')
        return self.driver.find_elements_by_class_name(self.box)
        #for i in self.driver.find_elements_by_class_name(self.box):
            #print i.text

    def _get_nome_principal(self, box):
        try:
            novo = ''
            novo = novo.encode('utf8')
            person_title = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, self.nome)))
            for i in box.find_elements_by_class_name(self.nome):
                #print('================' + i.text)
                novo = i.text
            #print (novo.encode('utf8'))
            return novo #.encode('utf8')
        except (StaleElementReferenceException, NoSuchElementException, TimeoutException) as ex:
            return "null"
            self.retornar()
            print("Erro function _get_hr_ult_msg: " + str(ex))


    def _get_ultima_msg(self, box):
        try:
            return box.find_element_by_class_name(self.ultmsg)
        except NoSuchElementException:
            pass

    def _get_hr_ult_msg(self, box):
        """
        try:
            for num in box.find_elements_by_class_name("_3Bxar"):
                if bool(self.is_int(num.text)):
                    return num.text
        except (ElementClickInterceptedException ,StaleElementReferenceException):
            print("Tempo excedido ao quantidadeMsgNaoLida: " + str(ex))
        #return num
        """
        try:
            return box.find_element_by_class_name(self.nummsg)
        except NoSuchElementException as ex:
            return "null"
            print("Erro function _get_hr_ult_msg: " + str(ex))

    def _get_qtd_msg(self):
        """
        try:
            novo = ''
            person_title = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, self.nummsg)))
            for i in box.find_elements_by_class_name(self.nummsg):
                print("testes " + str(i))
                if bool(self.is_int(i.text)) and len(i.text) != 0 and i.text != ' ':
                    novo = str(i.text)
                    #print "inteiros - " + str(i.text)
                else:
                    novo = ''
            return novo
        except (TimeoutException, StaleElementReferenceException) as ex:
            self.zerar()
            print("erro no numero de msg nao lidas!" + str(ex))
        """
        matriz = []
        try:
            box = self.driver.find_elements_by_class_name(self.box)
            for i in range(len(box)):
                linha = []
                try:
                    if int(box[i].text.split()[-1]):
                        #print(box[i].text.split()[-1])
                        #print(box[i].text.split('\n')[0])
                        linha.append(box[i].text.split('\n')[0])
                        linha.append(box[i].text.split()[-1])
                        matriz.append(linha)
                except Exception as e:
                    #print(str(e))
                    pass
            #print('len: ' + str(len(matriz)))
            #print(matriz)
            if len(matriz) > 0:
                return matriz
            else:
                lixo = ['0', '0']
                matriz.append(lixo)
                #print(matriz)
                return matriz
        except (ElementClickInterceptedException ,StaleElementReferenceException, NoSuchElementException) as ex:
            print("erro _get_qtd_msg: " + str(ex))
            self.zerar()
            pass

    def is_int(self, num):
        try:
            if len(num) > 0:
                int(num)
                return True
            else:
                return False
        except:
            pass
            return False

    def busca(self, string):
        #print('busca palavra ini ' + string)
        teste = ''
        passa = ''
        executar = ''
        achouLista = False
        achouComand = False
        achou = False
        texto = string
        if len(texto) > 0:
            #arq = open(self.parametros, "r")
            #linha = arq.readline()
            for linha in  self.consultaEntradas:
                #print(linha[1])
                #print(" self.consultaEntradas: " , linha)
                if linha[1] == '$':
                    if texto.lower() == linha[2].lower():
                        self.retornaListarComandos()
                        break
                #Se a conversa for com servidor '='
                elif linha[1] == '=':
                    if texto.lower() == linha[2].lower():
                        if '>' in linha[4]:
                            self.mata = True
                            #print(executar)
                            #executar = executar.replace('>', '').replace('-', '').replace('<', '')
                            self.comando = linha[5] #[91, '=', 'geracnpj', 1, '>', 'C:/Users/hitma/Documents/GitHub/geradorCNPJ/app/geradorCNPJ.py', 'S']
                            self.defineTipo = '>'
                            self.terceiraLinha = linha[2].lower()
                            self.executaScript()
                            time.sleep(1)
                            break
                        elif '-' in linha[4]:
                            self.mata = True
                            #print(executar)
                            self.comando = linha[5]
                            self.defineTipo = '-'
                            self.executaTerminal()
                            time.sleep(1)
                        elif '<' in linha[4]:
                            self.mata = True
                            #print(executar)
                            self.comando = linha[5]
                            self.defineTipo = '<'
                            self.executaScriptRetorno()
                            time.sleep(1)
                        elif '@' in linha[4]:
                            #print('--------------------> @' + string)
                            #print('entrando no comparavirgula: ' + texto + ' - ' + str(linha[2]))
                            if (texto.lower() == linha[2].lower()): #re.search(linha[2].lower(), texto.lower(), re.IGNORECASE):
                                #print('|-------------------->' + str(self.consultaEntradas[len(linha)]))
                                respostasEleatorias = []
                                for i in self.consultaEntradas:
                                        if i[0] == linha[0]:
                                            respostasEleatorias.append(i)
                                #respostasEleatorias = self.getConsultaEntrada(linha[0])
                                print("respostasEleatorias: " + str(respostasEleatorias))
                                indice = len(respostasEleatorias)-1
                                self.send(respostasEleatorias[random.randint(0, indice)][5])
                                break
                elif linha[1] == '%':
                    #print('--------------------> %' + string)
                    #print('entrando no comparavirgula: ' + texto + ' - ' + str(linha[2]))
                    if bool(self.comparaComVirgula(texto, linha[2])): #re.search(linha[2].lower(), texto.lower(), re.IGNORECASE):
                        print('|-------------------->' + str(self.consultaEntradas[len(linha)]))
                        respostasEleatorias = []
                        for i in self.consultaEntradas:
                                if i[0] == linha[0]:
                                    respostasEleatorias.append(i)
                        #respostasEleatorias = self.getConsultaEntrada(linha[0])
                        print("respostasEleatorias: " + str(respostasEleatorias))
                        indice = len(respostasEleatorias)-1
                        self.send(respostasEleatorias[random.randint(0, indice)][5])
                        break




    def buscaConversa(self, string):
        #print('busca palavra ini')
        teste = ''
        executar = ''
        achouLista = False
        achouC = False
        achouComand = False
        achou = False
        ok = False
        texto = string
        if len(texto) > 0:
            #arq = open(self.parametros, "r")
            #linha = arq.readline()
            for linha in  self.consultaEntradas:
                #print(linha)
                #if ('-' not in linha) and ('<' not in linha) and ('>' not in linha) and ('=' not in linha) and ('#' not in linha):
                #if texto.lower() == linha.replace('\n', '').lower():#re.search(palavras, linha, re.IGNORECASE):
                if linha[1] == '$':
                    if texto.lower() == linha[2].lower():
                        achou = True
                        self.comando3 = linha[2]
                        #linha = arq.readline()
                        executar = linha[5]
                        break
                if linha[1] == '%':
                    #obtem os registros que podem estar em um texto
                    a,i = 0, 0
                    ent = []
                    ent.append('')
                    #print("linha[2]" + linha[2])
                    while i < len(linha[2]):
                        #print("while" + str(i))
                        if linha[2][i] == ',':
                            if linha[2][i+1] == ' ':
                                ent.append('')
                                i+=1
                                a+=1
                            else:
                                ent.append('')
                                a+=1
                        else:
                            ent[a] += linha[2][i]
                        i+=1
                    #fim obter ent[frases]
                    #print("ent = " + str(ent))
                    for i in ent:
                        #print('uuuuuuuuuuu '+i)
                        if re.search(i.lower(), texto.lower(), re.IGNORECASE):
                            ok = True
                        else:
                            ok = False
                            break
                    print("ok " + str(ok))
                    if bool(ok):
                        ok = False
                        achouC = True
                        self.comando3 = i
                        #linha = arq.readline()
                        executar = linha[5]
                        break

        if bool(achouC):
            achouC = False
            ac = True
            con = 0
            l =  self.consultaEntradas[linha[0]]
            self.send(l[random.randint(1, int(l[-1][3]))][5])

        if bool(achou):
            achou = False
            if '=' in linha[4]:
                if texto.lower() == linha[4].lower():#re.search(palavras, linha, re.IGNORECASE):
                    self.retornaListarComandos()
            if '>' in linha[4]:
                print(linha[4])
                self.mata = True
                #print(executar)
                executar = executar.replace('>', '').replace('-', '').replace('<', '')
                self.comando = executar
                self.defineTipo = '>'
                self.executaScript()
                time.sleep(1)
            if '-' in linha[4]:
                self.mata = True
                #print(executar)
                executar = executar.replace('>', '').replace('-', '').replace('<', '')
                self.comando = executar
                self.defineTipo = '-'
                self.executaTerminal()
                time.sleep(1)

            if '<' in linha[4]:
                self.mata = True
                #print(executar)
                executar = executar.replace('>', '').replace('-', '').replace('<', '')
                self.comando = executar
                self.defineTipo = '<'
                self.executaScriptRetorno()
                time.sleep(1)

    def comparaComVirgula(self, entrada, consulta):
        """
        Verificar se na ENTRADA existe palavras com virgulas e se essas palavras
        conte no texto origem digitada.
        Caso tenha retorna True, o contrario False
        """
        #print("busca virgula " + entrada + " -- " + consulta)
        temVirgula = False
        a, i = 0, 0
        ent = []
        ent.append('')
        #print("linha[2]" + linha[2])
        while i < len(consulta):
            #print("while" + str(i))
            if consulta[i] == ',':
                if consulta[i+1] == ' ':
                    ent.append('')
                    i+=1
                    a+=1
                else:
                    ent.append('')
                    a+=1
            else:
                ent[a] += consulta[i]
            i += 1
        #fim obter ent[frases]
        #print("ent = " + str(ent))
        listaEncontrada = []
        listaEntrada = entrada.split()
        print("entrada = " + str(entrada))
        print(ent)
        print("listaEntrada = " + str(listaEntrada))
        for i in ent:
            print('for i: ' + str(i))
            for j in listaEntrada:
                if (i == j):#print('uuuuuuuuuuu '+i)
                    listaEncontrada.append(j)
            if i != '*':
                if re.search(i.lower(), entrada.lower(), re.IGNORECASE):
                    print(i)
                    temVirgula = True
                else:
                    print(entrada)
                    temVirgula = False
                    break
        #print(ent)
        #print(listaEncontrada)
        #if (ent == listaEncontrada):
        #    return True
        #else:
        #    return False
        return temVirgula

    def retornaListarComandos(self):
        cont = 1
        #linhas = self.listarComandos
        i = 0
        for linha in self.listarComandos:
            #não pega fixos do sistema / não envia respostas duplicadas ou triplicada
            txt = str(cont) + ' - ' + linha
            self.send(txt)
            cont += 1
        self.send("---fim---")

    def executaTerminal(self):
        retorno = ''
        #print('ExecutaTerminal')
        if bool(self.mata):
            print(">>>>>>>>>>>> " + self.comando)
            self.mata = False
            self.confi = True
            if bool(self.confirma) == False:
                self.send("Deseja realmente executar este comando: Sim ou Nao?")
            if bool(self.confirma):
                self.confirma = False
                self.confi = False
                #retorno = commands.getoutput(self.comando)
                retorno = os.popen(self.comando).read()
                #retorno = os.system(self.comando)
                print('Comando executado >>>>>>' + str(retorno))
                self.send(retorno)
                if retorno == '':
                    self.send('Nenhum retorno do comando (' + self.comando + ').')
                else:
                    self.send('Comando (' + self.comando + ') enviado ao servidor!')

    def executaScript(self):
        print('executa_script')
        if bool(self.mata):
            print(">>>>>>>>>>>> " + self.comando)
            self.mata = False
            self.confi = True
            print(self.mata)
            print(self.confi)
            print(self.confirma)
            if bool(self.confirma) == False:
                self.send("Deseja realmente executar este comando: Sim ou Nao?")
            if bool(self.confirma):
                self.confirma = False
                self.confi = False
                #separa o diretorio do arquivo
                dir, arqi = self.separaDiretorio(self.comando)
                if bool(re.search('.py', arqi, re.IGNORECASE)):
                    #commands.getoutput("python " + self.comando)
                    os.popen("python " + self.comando).read()
                    #os.system("python " + self.comando)
                    print("python " + self.comando)
                    self.send("Script python " + self.comando + " executado!")
                if bool(re.search('.sh', arqi, re.IGNORECASE)):
                    #commands.getoutput('cd ' + arqi + ' && chmod 777 ' + arqi + ' && ./' +  arqi)
                    os.popen('cd ' + dir + ' && chmod 777 ' + arqi + ' && ./' +  arqi).read()
                    #os.system('cd ' + dir + ' && chmod 777 ' + arqi + ' && ./' +  arqi)
                    print('cd ' + dir + ' && chmod 777 ' + arqi + ' && ./' +  arqi)
                    self.send("Script shell " + self.comando + " executado!")

    def executaScriptRetorno(self):
        print('executa_script1')
        retornoComando = ''
        if bool(self.mata):
            print(">>>>>>>>>>>> " + self.comando)
            self.mata = False
            self.confi = True
            if bool(self.confirma) == False:
                self.send("Deseja realmente executar este comando: Sim ou Nao?")
            if bool(self.confirma):
                self.confirma = False
                self.confi = False
                #separa o diretorio do arquivo
                dir, arqi = self.separaDiretorio(self.comando)
                if re.search('.py', self.comando, re.IGNORECASE):
                    #retornoComando = commands.getoutput("python " + self.comando)
                    retornoComando = subprocess.run("python " + teste, capture_output=True)
                    print('Python ' + self.comando + ' retorno = ' + retornoComando)
                    self.send("Script (" + self.comando + ") enviado ao servidor!")
                    if retornoComando != '':
                        self.send(retornoComando)
                elif re.search('.sh', self.comando, re.IGNORECASE):
                    #commands.getoutput('cd ' + arqi + ' && chmod 777 ' + arqi + ' && ./' +  arqi)
                    retornoComando = os.popen('cd ' + dir + ' && chmod 777 ' + arqi + ' && ./' +  arqi).read()
                    #retornoComando = subprocess.run('cd ' + dir + ' && chmod 777 ' + arqi + ' && ./' +  arqi, capture_output=True)
                    print('Shell ' + self.comando + ' retorno = ' + retornoComando)
                    self.send("Script (" + self.comando + ") enviado ao servidor!")
                    if retornoComando != '':
                        self.send(retornoComando)
                elif re.search('.bat', self.comando, re.IGNORECASE):
                    #commands.getoutput('cd ' + arqi + ' && chmod 777 ' + arqi + ' && ./' +  arqi)
                    retornoComando = os.popen('cd ' + arqi + ' && chmod 777 ' + arqi + ' && ./' +  arqi).read()
                    #retornoComando = subprocess.run('cd ' + arqi + ' && chmod 777 ' + arqi + ' && ./' +  arqi, capture_output=True)
                    print('Shell ' + self.comando + ' retorno = ' + retornoComando)
                    self.send("Script (" + self.comando + ") enviado ao servidor!")
                    if retornoComando != '':
                        self.send(retornoComando)

    def confirmaComando(self):
        try:
            #print('confirmaComando')
            if bool(self.confi):
                print('exto.lower() ' + self.textPrincipal()[-3].lower() + ' = ' + self.terceiraLinha + ' --- sim ' + self.textPrincipal()[-1].lower() + ' == sim')
                if (self.textPrincipal()[-3].lower().strip(' ') == self.terceiraLinha) and (self.textPrincipal()[-1].lower().strip(' ') == 'sim'):
                    print('entrou')
                    self.confirma = True
                    self.mata = True
                    if self.defineTipo == '>':
                        self.executaScript()
                    elif self.defineTipo == '-':
                        self.executaTerminal()
        except:
            pass

    def get_all_data(self):
        """
        get_all_data()
        entrada: None
        saida: Busca blocos com nomes, textos e numeros.
        """
        print('get_all_data')
        textos = ''
        qtd = ''
        nomeP = ''
        try:
            #print(boxes)
            #for boxs in self._get_boxes():
            for boxs in self._get_qtd_msg():
                nomeP, qtd = boxs
                print('qtd: ' + str(qtd) + ' nomeP: ' + str(nomeP))
                #print(nomeP + ' ----------*-*-/-*/-*/-*/-*/-*/-*/-*/ ' + str(qtd))
                #nomeP = self._get_nome_principal(boxs)
                #print('boxes')
                #print(str(qtd))
                if qtd != '0':
                    #print(str(qtd))
                    #print(nomeP)
                    #print()
                    #testes = self.buscaRelacaoNome(nomeP)
                    #print("teste " + str(testes))
                    #Se encontrar conversa em aberta entra
                    if bool(self.buscaRelacaoNome(nomeP)):
                        #função que entra do contato
                        self.nomeEntra(nomeP)
                    #self.comigo()
        except (ElementNotVisibleException, StaleElementReferenceException) :
            self.retornar()
            print('Erro de seleção, será auto-corrigido!get_all_data ------------------------------------------------------2')

    def finalidade(self):
        """
        pega a ultima conversa e analisa a relação de palavras no banco de dados.
        """
        try:
            self.busca(self.textPrincipal()[-1])
        except IndexError:
            self.retornar()
            print('Erro de seleção, será auto-corrigido!finalidade ------------------------------------------------------2')


    def separaDiretorio(self, string):
        #print('separaDiretorio')
        #print(string + ' - ' + tipo)
        novo = string
        arq = ''
        dir = ''
        count = 0
        for i in novo:
            if (i == '/'):
                count += 1
        for i in novo:
            if count == 0:
                arq += i
            if i == '/':
                count -= 1
        for i in novo:
        #     print(str(i))
            if i == '/':
                count += 1
        #     print('total de /: ' + str(count))
        for i in novo:
            if count == 0:
                break
            if count >= 0:
                dir += i
                #print(saida)
            if i == '/':
                count -= 1
                 #print('total do count: ' + str(count))
        return dir, arq

    def buscaRelacaoNome(self, string):
        print("buscaRelacaoNome - " + string)
        retorna = False
        print(self.consultaContatoTodos)
        if  (self.consultaContatoTodos[0][2].lower() == 's'):
            retorna = True
        else:
            ContatosCadastrados = self.consultaContato
            for i in ContatosCadastrados:
                #print(i)
                if (i[2].lower() == 's'):
                    #print('(S == linha[2])|' + linha[1].lower() +'|')
                    #print(string)
                    if i[1].lower() == string.lower():
                    #print(linha[1].lower().strip() , string.lower().strip())
                        retorna = True
                        break
        return retorna

    def retornar(self):
        try:
            #self.driver.find_element_by_class_name('_1WZqU PNlAR').click()
            person_title = WebDriverWait(self.driver, 50).until(EC.presence_of_element_located(By.CLASS_NAME, '_1WZqU.PNlAR'))
            person_title.click()
            self.zerar()
            self.send('API voltou.')
        except (ElementClickInterceptedException ,StaleElementReferenceException, NoSuchElementException) as ex:
            print("retornar não encontrado: " + str(ex))
            self.home()
            pass

    def home(self):
        self.tentativaDeAcesso = 0
        self.navegate()
        self.consultas()
        print("fim navegate")
        #if __name__ == "__main__":
            #print("if __name__")
        self.qrCode()
        print('Iniciando')
        while True:
            try:
                self.finalidade()
                self.confirmaComando()
                self.get_all_data()
                t = ''
                for i in self.driver.find_elements_by_xpath(self.class_todos):
                    t = i.text

                #self.novoContato(t)
                #mysq.consultaContato()
                #self.buscaRelacaoNome()
                #self.retornar()
            except ElementNotVisibleException :
                print('Erro de seleção, será auto-corrigido!home ------------------------------------------------------3')
                pass



#ff = webdriver.Firefox()
#c = zap(ff)
#self.navegate()
#print("fim navegate")
#if __name__ == "__main__":
#    print("if __name__")
#    self.qrCode()
#print('Iniciando')
##self.zerar()
#dataHora = datetime.now()
#self.send('API whatsapp iniciada: ' + str(dataHora.day) + '/' + str(dataHora.month) + '/' + str(dataHora.year) + ' ' + str(dataHora.hour) + ':' + str(dataHora.minute))
#self.home()



    #vezes = input('Enter para continuar!')
    #print('Rodou, ' + str(i) + ' vezes de 10.')
