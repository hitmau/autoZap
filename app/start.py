import mysql_zap as mysql
import time
import os
from threading import Thread as thread
import whats_auto as wza

mysql.abrirConexao()
while True:
    try:
        if len(mysql.consultaLogin()) > 0:
            for i in mysql.consultaLogin():
                print(i)
                #input("Pressione ENTER para continuar")
                #consultaLogin: 0 codusuario - 1 = start (site iniciou) - 2 = status (start.py iniciou)
                if i[1] == 'S' and (i[2] == 'N' or i[2] == ''):
                    print("entrou no if Executar usuario: " + str(i[0]) + " - " + str(i[1]) + " - " + str(i[2]))
                    #input("Pressione ENTER para continuar")
                    print(wza.zap(i[0]))
                    thread(target=wza.zap,args=[i[0]]).start()
                    mysql.atualizaLogin(i[0])
                    time.sleep(5)
            time.sleep(1)
    except:
        pass
        mysql.statusConexao()
    break
