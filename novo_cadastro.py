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

#wait = WebDriverWait(driver, 600)

entrarL = 'identifierId' #"//div[@class='ry3kXd']"
entrarP = "/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/form/content/section/div/content/div[1]/div/div[1]/div/div[1]/input"
login = 'hitmau1'
password = 'mauricio74com.'
mais = '/html/body/div[7]/div[2]/header/div[4]/div[2]/div/c-wiz/div/div[1]/div/div/button'
nome = '/html/body/div[7]/div[4]/div/div[2]/content/div/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div[1]/input'
sobrenome = '/html/body/div[7]/div[4]/div/div[2]/content/div/div[2]/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div[3]/div/div[1]/div/div[1]/input'
telefone = '/html/body/div[7]/div[4]/div/div[2]/content/div/div[2]/div[1]/div/div/div[7]/div/div/div[2]/div[1]/div[2]/div[1]/div/div[1]/input'
email = '/html/body/div[7]/div[4]/div/div[2]/content/div/div[2]/div[1]/div/div/div[6]/div/div/div[2]/div[1]/div[1]/div/div[1]/input'
maisCampos = '/html/body/div[7]/div[4]/div/div[2]/content/div/div[3]/button'
endereco = '/html/body/div[7]/div[4]/div/div[2]/content/div/div[2]/div[1]/div/div/div[8]/div/div/div[2]/div[1]/c-wiz/div/div/div[4]/div/div[1]/div/div[1]/input'
bairro = '/html/body/div[7]/div[4]/div/div[2]/content/div/div[2]/div[1]/div/div/div[8]/div/div/div[2]/div[1]/c-wiz/div/div/div[6]/div/div[1]/div/div[1]/input'
cidade = '/html/body/div[7]/div[4]/div/div[2]/content/div/div[2]/div[1]/div/div/div[8]/div/div/div[2]/div[1]/c-wiz/div/div/div[7]/div[1]'
estado = '/html/body/div[7]/div[4]/div/div[2]/content/div/div[2]/div[1]/div/div/div[8]/div/div/div[2]/div[1]/c-wiz/div/div/div[8]/div[1]'
cep = '/html/body/div[7]/div[4]/div/div[2]/content/div/div[2]/div[1]/div/div/div[8]/div/div/div[2]/div[1]/c-wiz/div/div/div[9]/div/div[1]/div/div[1]/input'
marcador = '/html/body/div[7]/div[4]/div/div[2]/content/div/div[2]/div[1]/div/div/div[6]/div/div/div[2]/div[2]/div/div[1]/input[2]'
aniversario = '/html/body/div[7]/div[4]/div/div[2]/content/div/div[2]/div[1]/div/div/div[9]/div/div/div[2]/div/div[1]/div/div[1]/input'
salvar = '/html/body/div[7]/div[4]/div/div[2]/content/div/div[3]/div/button[2]'
cancelar = '/html/body/div[7]/div[4]/div/div[2]/content/div/div[3]/div/button[1]/span'
url = "https://www.google.com/contacts/"
#driver = ''


def navegate():
    """
    Abre o browser e navega pelo endereco que esta contino na fariavel ult.
    Apos o browser abrir ele e minimizado.
    """
    global url
    d = webdriver.Firefox()
    d.get(url)
    return d

def fechar(cc):
    cc.close()

def loginContatos(dd):
    global entrarL, entrarP, login, password
    driver = dd
    log = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, entrarL)))
    log.send_keys(login)
    log.send_keys(Keys.RETURN)
    time.sleep(2)
    senha = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, entrarP)))
    senha.send_keys(password)
    senha.send_keys(Keys.RETURN)

def botaoMais(dd):
    global mais
    driver = dd
    botao = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, mais)))
    botao.send_keys(Keys.RETURN)

def separaNome(string):
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

def cadastraContato(driver, lista):
    print(lista)
    global estado, cidade, bairro, nome, sobrenome, email, telefone, endereco, cep, marcador, aniversario, maisCampos
    Nnome, Nsobrenome = separaNome(lista[0])
    Nemail = lista[1]
    Ntelefone = lista[2]
    Ndata = lista[3]
    Nendereco = lista[4]
    Nbairro = lista[5]
    Ncidade = lista[6]
    Nestado = lista[7]
    Ncep = lista[8]
    Nmarcador = lista[9]
    print(Nestado,Ncidade)
    _nome = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, nome)))
    _nome.send_keys(Nnome)
    _sobrenome = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, sobrenome)))
    _sobrenome.send_keys(Nsobrenome)
    _email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, email)))
    _email.send_keys(Nemail)
    _telefone = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, telefone)))
    _telefone.send_keys(Ntelefone)
    _maisCampos = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, maisCampos))).click()
    _endereco = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, endereco)))
    _endereco.send_keys(Nendereco)
    #driver.execute_script('window.scrollBy(0, 50)')
    _cep = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, cep)))
    _cep.send_keys(Ncep)
    driver.find_element_by_xpath(estado).click()
    estado = driver.find_elements_by_xpath(estado)
    for i in estado:
        for j in i.find_elements_by_class_name('vRMGwf.oJeWuf'):
            #print('-|'+ j.text.lower() +'='+Nestado.lower()+'|-***')
            if j.text.lower() == Nestado.lower():
                j.click()
                break
    time.sleep(1)
    driver.find_element_by_xpath(cidade).click()
    cidade = driver.find_elements_by_class_name('vRMGwf.oJeWuf')
    for i in cidade:
        a = i.text.encode("utf-8")
        if a == '':
            continue
        else:
            print('***-|'+ a.lower() +'='+Ncidade.lower()+'|-***')
            if a.lower() == Ncidade.lower():
                i.click()
                break
    bairro = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, bairro)))
    bairro.send_keys(Nbairro)
    marcador = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, marcador)))
    marcador.send_keys(Nmarcador)
    aniversario = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, aniversario)))
    aniversario.send_keys(Ndata)
    lista = []

def salvaContato():
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, salvar))).click()

def cancelaContato():
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, cancelar))).click()

def iniciaCadastro():
    m = navegate()
    loginContatos(m)
    botaoMais(m)
    #cadastraContato (m, ['Mauricio Rodrigues da Silva','hitmau1@gmail.com','21980317641','28/03/1987','Trav. Paulo Scotelaro, 89','venda das pedras','itaboraí','rio de janeiro','24804718','marcador teste'])
    return m

#ff = webdriver.Firefox()
#c = zap(ff)

#navegate()
#c.loginContatos()
#c.botaoMais()
#c.cadastraContato()
#c.salvaContato()


    #vezes = input('Enter para continuar!')
    #print('Rodou, ' + str(i) + ' vezes de 10.')
