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
        self.box = '_2wP_Y' # '//div[@class="_2wP_Y"]'
        self.nome = '_25Ooe' # '//div[@class=""]'_1wjpf
        self.ultmsg = '_2_LEW' # '//div[@class="_2_LEW"]'
        self.nummsg = '_3Bxar' # '//div[@class="_1AwDx"]/div[2]' #'OUeyt' #
        self.textbox = '_3u328.copyable-text.selectable-text'
        self.dataHora = datetime.now()
        #self.dirarquivo = '/home/hitmau/Documentos/Projetos/python/whatsapp/'
        #self.arquivo = self.dirarquivo + "parametros.txt"
        #self.arquivoMeu = self.dirarquivo + "arquivoMeu.txt"
        #self.parametros = self.dirarquivo + "parametros.txt" #self.dirarquivo +
        self.target = '98031-7641' # número do dono do celular
        self.Nome_lista = '//span[contains(@title, '+ '"' + str(self.tel) + '"'+ ')]'
        self.buscaNome = '/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/input'
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
        #entra na função de confirmação
        self.confirma = False

        self.confi = False
        #Definição de tipo de execução (> ou < ou -)
        self.defineTipo = ''
        #Texto para novo contato (cadastro)
        self.cadastroDeContato = 'Identificamos que seu cadastro nao existe em nossa base de dados. Gostaria de ser cadastrado? (S/N)'
        self.consultaEntradas = []
        self.consultaContato = []
        self.consultaParametroContato = []
        #self.home()


    def consultas(self):
        #parametro add contato ativado ou desativado
        self.getConsultaContatos()
        self.getConsultaParametroContato()
        self.getConsultaEntrada()

    def getConsultaEntrada(self, inteiro = '0'):
        self.consultaEntradas = mysql.consultaEntrada(self.codusuario, inteiro)
        print(self.consultaEntradas)
        return self.consultaEntradas

    def getConsultaContatos(self, inteiro = '0'):
        self.consultaContato = mysql.consultaContato(self.codusuario, inteiro)
        print(self.consultaContato)
        return self.consultaContato

    def getConsultaParametroContato(self):
        self.consultaParametroContato = mysql.consultaParametro(self.codusuario, "T")
        print(self.consultaParametroContato)
        return self.consultaParametroContato

    def navegate(self):
        """
        Abre o browser e navega pelo endereco que esta contino na fariavel self.ult.
        Apos o browser abrir ele e minimizado.
        """
        self.driver.get(self.url)
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
            if bool(self.getConsultaParametroContato()):
                print("entra no addcontato-----------------------------------")
                if bool(self.verificaNovoContato(nomeS)):
                    self.novoContato(nomeS)
        except TimeoutException as ex:
            print("Tempo excedido ao zerar: " + str(ex))
            pass
    def novoContato(self, string):
        string = string.replace("+", "")
        string = string.strip(" ")
        string = string.replace(" ", "")
        cadastrado = True
        pergunta = False
        for todosContatos in consultaContatos:
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

    def zerar(self, string = None):
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
        print('textoPrincipal')
        conversa = []
        try:
            person_title = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.ultConvPrincipalMeu)))
            for uconv in self.driver.find_elements_by_xpath(self.ultConvPrincipalMeu):
                conversa.append(uconv.text)
                #print("teste 1" + str(uconv.text))
        except (TimeoutException, StaleElementReferenceException) as ex:
            print("Erro function textPrincipal: " + str(ex))
            self.zerar()
            for uconv in self.driver.find_elements_by_xpath(self.ultConvPrincipalMeu):
                conversa.append(uconv.text)
                #print "teste 2" + str(uconv.text)
        return conversa

    def _get_boxes(self):
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
            return box.find_element_by_class_name('_15G96')
        except NoSuchElementException as ex:
            return "null"
            print("Erro function _get_hr_ult_msg: " + str(ex))

    def _get_qtd_msg(self, box):
        try:
            novo = ''
            person_title = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, self.nummsg)))
            for i in box.find_elements_by_class_name(self.nummsg):
                #print "testes str int -" + i.text
                if bool(self.is_int(i.text)) and len(i.text) != 0 and i.text != ' ':
                    novo = str(i.text)
                    #print "inteiros - " + str(i.text)
                else:
                    novo = ''
            return novo
        except (TimeoutException, StaleElementReferenceException) as ex:
            self.retornar()
            print("erro no numero de msg nao lidas!" + str(ex))


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
        print('busca palavra ini ' + string)
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
                print(" self.consultaEntradas: " , linha)
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
                            self.comando = linha[5]
                            self.defineTipo = '>'
                            self.terceiraLinha = linha[2].lower()
                            self.executaScript()
                            time.sleep(1)
                        if '-' in linha[4]:
                            self.mata = True
                            #print(executar)
                            self.comando = linha[5]
                            self.defineTipo = '-'
                            self.executaTerminal()
                            time.sleep(1)

                        if '<' in linha[4]:
                            self.mata = True
                            #print(executar)
                            self.comando = linha[5]
                            self.defineTipo = '<'
                            self.executaScriptRetorno()
                            time.sleep(1)
                elif linha[1] == '%':
                    #print('--------------------> %' + string)
                    if bool(self.comparaComVirgula(texto, linha[2])): #re.search(linha[2].lower(), texto.lower(), re.IGNORECASE):
                        #print(self.consultaEntradas[len(linha)])
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
        #print("busca virgula " + entrada + " -- " + consulta)
        ok = False
        a,i = 0, 0
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
            i+=1
        #fim obter ent[frases]
        #print("ent = " + str(ent))
        for i in ent:
            #print('uuuuuuuuuuu '+i)
            if re.search(i.lower(), entrada.lower(), re.IGNORECASE):
                ok = True
            else:
                ok = False
                break
        #print("ok" + str(ok))
        return ok

    def retornaListarComandos(self):
        cont = 1
        linhas =  self.consultaEntradas
        i = 0
        for linha in linhas:
            #não pega fixos do sistema / não envia respostas duplicadas ou triplicadas
            if ('=' != linha[4]) and linha[0] != i:
                txt = str(cont) + ' - ' + linha[2]
                self.send(txt)
                cont += 1
                i = linha[0]
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
            print('confirmaComando')
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
        textos = ''
        qtd = ''
        nomeP = ''
        try:
            boxes = self._get_boxes()
            for boxs in boxes:
                qtd = self._get_qtd_msg(boxs)
                nomeP = self._get_nome_principal(boxs)
                if len(str(qtd)) > 0 and qtd != None:
                    print(str(qtd))
                    #print(nomeP)
                    #print()
                    testes = self.buscaRelacaoNome(nomeP)
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
            #if mysq.consultaParametr(1) == 'S':
            #    self.buscaServidor(self.textPrincipal()[-1])
            #elif mysq.consultaParametr('servconv') == 'conversa':
            #    self.buscaConversa(self.textPrincipal()[-1])
            #print(self.textPrincipal()[-1])
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
        print("buscaRelacaoNome")
        retorna = False
        nTodos = True
        linhas = self.consultaEntradas
        for i in linhas:
            #print(i)
            if i[1] == 'todos' and i[2] == 'S':
                nTodos = False
        if bool(nTodos):
            for linha in linhas:
                if ('S' == linha[2]):
                    #print('(S == linha[2])|' + linha[1].lower() +'|')
                    #print(string)
                    if linha[1].lower() == string.lower():
                    #print(linha[1].lower().strip() , string.lower().strip())
                        retorna = True
                        break
                    else:
                        retorna = False
        else:
            retorna = True
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
