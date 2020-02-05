#encoding: utf-8
#coding: utf-8
#Autor Maurcio Rodrigues (mauriciosist@gmail.com)
#V 1.0.27
import mysql_zap as mysql
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os, platform, time, re, subprocess
import selenium.webdriver.support.ui as ui
import random
#import sys
#reload(sys)
#sys.setdefaultencoding('utf8')
#import commands
#import subprocess
# import selenium.webdriver.support.expected_conditions as EC
import unittest
import busca_cep as cep
#class zap:

#wait = WebDriverWait(self.driver, 600)


#driver = ''

class addContatos:
    def __init__(self, cod, lista):#nomeCompleto = None, email = None, telefone = None, aniversario = None,endereco = None,bairro = None,cidade = None, estado = None,    cep = None, marcador = None):
        self.lista = []
        self.lista.append(lista[0])
        self.lista.append(lista[1])
        self.lista.append(lista[2])
        self.lista.append(lista[3])
        self.lista.append(lista[4])
        self.lista.append(lista[5])
        self.lista.append(lista[6])
        self.lista.append(lista[7])
        self.lista.append(lista[8])
        self.lista.append(lista[9])
        #self.lista.append(maisCampos)

        self.driver = webdriver.Firefox()
        self.entrarL = 'identifierId' #"//div[@class='ry3kXd']"
        self.entrarP = "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/span/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input"
        self.login = 'hitmau1'
        self.password = 'mauricio74com.'
        self.mais = '/html/body/div[7]/div[2]/header/div[4]/div[2]/div/c-wiz/div/div[1]/div/div/button'
        self.nome = '/html/body/div[7]/div[4]/div/div[2]/span/div/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div[1]/input'
        self.sobrenome = '/html/body/div[7]/div[4]/div/div[2]/span/div/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div[3]/div/div[1]/div/div[1]/input'
        self.telefone = '/html/body/div[7]/div[4]/div/div[2]/span/div/div[2]/div[1]/div/div/div[7]/div/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/input'
        self.email = '/html/body/div[7]/div[4]/div/div[2]/span/div/div[2]/div[1]/div/div/div[6]/div/div/div[2]/div[1]/div[1]/div/div[1]/input'
        self.maisCampos = '/html/body/div[7]/div[4]/div/div[2]/span/div/div[3]/button'
        self.endereco = '/html/body/div[7]/div[4]/div/div[2]/span/div/div[2]/div[1]/div/div/div[8]/div/div/div[2]/div[1]/c-wiz/div/div/div[4]/div/div[1]/div/div[1]/input'
        self.bairro = '/html/body/div[7]/div[4]/div/div[2]/span/div/div[2]/div[1]/div/div/div[8]/div/div/div[2]/div[1]/c-wiz/div/div/div[6]/div/div[1]/div/div[1]/input'

        self.cidade = '/html/body/div[7]/div[4]/div/div[2]/span/div/div[2]/div[1]/div/div/div[8]/div/div/div[2]/div[1]/c-wiz/div/div/div[7]/div[1]' #'/html/body/div[7]/div[4]/div/div[2]/content/div/div[2]/div[1]/div/div/div[8]/div/div/div[2]/div[1]/c-wiz/div/div/div[7]/div[1]'

        self.estado = '/html/body/div[7]/div[4]/div/div[2]/span/div/div[2]/div[1]/div/div/div[8]/div/div/div[2]/div[1]/c-wiz/div/div/div[8]/div[1]' #'/html/body/div[7]/div[4]/div/div[2]/content/div/div[2]/div[1]/div/div/div[8]/div/div/div[2]/div[1]/c-wiz/div/div/div[8]/div[1]'

        self.cep = '/html/body/div[7]/div[4]/div/div[2]/span/div/div[2]/div[1]/div/div/div[8]/div/div/div[2]/div[1]/c-wiz/div/div/div[9]/div/div[1]/div/div[1]/input'
        self.marcador = '/html/body/div[7]/div[4]/div/div[2]/span/div/div[2]/div[1]/div/div/div[8]/div/div/div[2]/div[3]/div/div[1]/input[2]'
        self.aniversario = '/html/body/div[7]/div[4]/div/div[2]/span/div/div[2]/div[1]/div/div/div[9]/div/div/div[2]/div/div[1]/div/div[1]/input'
        self.salvar = '/html/body/div[7]/div[4]/div/div[2]/span/div/div[3]/div/button[2]'
        self.cancelar = '/html/body/div[7]/div[4]/div/div[2]/span/div/div[3]/div/button[1]'
        self.url = "https://www.google.com/contacts/"

    def navegate(self):
        """
        Abre o browser e navega pelo endereco que esta contino na fariavel ult.
        Apos o browser abrir ele e minimizado.
        """
        #global url
        #d = webdriver.Firefox()
        self.driver.get(self.url)

    def fechar(self):
        self.driver.close()

    def loginContatos(self):
        log = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, self.entrarL)))
        log.send_keys(self.login)
        log.send_keys(Keys.RETURN)
        time.sleep(2)
        senha = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.entrarP)))
        senha.send_keys(self.password)
        senha.send_keys(Keys.RETURN)

    def botaoMais(self):
        botao = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.mais)))
        botao.send_keys(Keys.RETURN)

    def separaNome(self, string):
        """
        separaNome(string)
        entrada: String, nome conpleto
        saida: 2 strings
        [0] = primeiro nome
        [1] = restante do nome
        """
        lista = []
        nome = ''
        sobrenome = ''
        lista.append('')
        a = 0
        for i in string:
            if i != ' ':
                lista[a] += i
            else:
                lista.append('')
                a += 1
        for i in lista[:1]:
            nome += i
        for i in lista[1:]:
            if i == lista[-1]:
                sobrenome += i
            else:
                sobrenome += i + ' '
        return nome, sobrenome

    def cadastraContato(self):
        #print(lista)
        #global estado, cidade, bairro, nome, sobrenome, email, telefone, endereco, cep, marcador, aniversario, maisCampos
        Nnome, Nsobrenome = self.separaNome(self.lista[0])
        Nemail = self.lista[1]
        Ntelefone = self.lista[2]
        Ndata = self.lista[3]
        Nendereco = self.lista[4]
        Nbairro = self.lista[5]
        Ncidade = self.lista[6]
        Nestado = self.lista[7]
        Ncep = self.lista[8]
        Nmarcador = self.lista[9]
        print(Nestado, Ncidade)
        _nome = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.nome)))
        _nome.send_keys(Nnome)
        _sobrenome = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.sobrenome)))
        _sobrenome.send_keys(Nsobrenome)
        _email = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.email)))
        _email.send_keys(Nemail)
        _telefone = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.telefone)))
        _telefone.send_keys(Ntelefone)
        _maisCampos = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.maisCampos))).click()
        _endereco = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.endereco)))
        _endereco.send_keys(Nendereco)
        #driver.execute_script('window.scrollBy(0, 50)')
        _cep = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.cep)))
        _cep.send_keys(Ncep)
        self.driver.find_element_by_xpath(self.estado).click()
        estado = self.driver.find_elements_by_xpath(self.estado)
        for i in estado:
            for j in i.find_elements_by_xpath('/html/body/div[7]/div[4]/div/div[2]/span/div/div[2]/div[1]/div/div/div[8]/div/div/div[2]/div[1]/c-wiz/div/div/div[8]/div[1]/div[1]/div[1]/div[1]/span'):#class_name('vRMGwf.oJeWuf'):
                #print('-|'+ j.text.lower() +'='+Nestado.lower()+'|-***')
                if j.text.lower() == Nestado.lower():
                    j.click()
                    break
        time.sleep(1)
        self.driver.find_element_by_xpath(self.cidade).click()
        cidade = self.driver.find_elements_by_class_name('vRMGwf.oJeWuf')
        for i in cidade:
            a = i.text.encode("utf-8")
            if a == '':
                continue
            else:
                print('***-|'+ a.lower() +'='+Ncidade.lower()+'|-***')
                if a.lower() == Ncidade.lower():
                    i.click()
                    break
        bairro = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.bairro)))
        bairro.send_keys(Nbairro)
        marcador = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.marcador)))
        marcador.send_keys(Nmarcador)
        aniversario = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.aniversario)))
        aniversario.send_keys(Ndata)
        lista = []

    def salvaContato(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.salvar))).click()

    def cancelaContato(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.cancelar))).click()

    def iniciaCadastro(self):
        m = navegate()
        loginContatos(m)
        botaoMais(m)
        #cadastraContato (m, ['Mauricio Rodrigues da Silva','hitmau1@gmail.com','21980317641','28/03/1987','Trav. Paulo Scotelaro, 89','venda das pedras','itaboraí','rio de janeiro','24804718','marcador teste'])
        return m

    def home(self):
        self.navegate()
        self.loginContatos()
        self.botaoMais()
        self.cadastraContato()

#ff = webdriver.Firefox()
#c = zap(ff)

#navegate()
#c.loginContatos()
#c.botaoMais()
#c.cadastraContato()
#c.salvaContato()


    #vezes = input('Enter para continuar!')
    #print('Rodou, ' + str(i) + ' vezes de 10.')
