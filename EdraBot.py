from simulacao import *
from info import *
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import numpy as np
from time import sleep


marca_motor = marca_motors.split(',')
modelo_motor = modelo_motors.split(',')
bateria = baterias.split(',')


navegador = webdriver.Chrome(ChromeDriverManager().install())


#Processo de Login
url_login = "https://www.ecalc.ch/calcmember/login.php?https://www.ecalc.ch/xcoptercalc.php"



navegador.get(url_login)
sleep(2)
login_ecalc = navegador.find_element_by_xpath('//*[@id="username"]')
login_ecalc.send_keys(login)
senha_ecalc = navegador.find_element_by_xpath('//*[@id="password"]')
senha_ecalc.send_keys(senha)
logar = navegador.find_element_by_xpath('//*[@id="myButton"]')
logar.click()
sleep(2)

navegador.switch_to.alert.accept();

sleep(5)

cookie = navegador.find_element_by_xpath('/html/body/div[3]/div')
cookie.click()


d = np.empty(shape = (1,len(marca_motor)),dtype='object')
n = np.empty(shape = (1,len(marca_motor)),dtype='object')
n2 = np.empty(shape = (1,len(bateria)),dtype='object')
t = np.empty(shape = (1,1),dtype='object')
t2 = np.empty(shape = (1,len(marca_motor)),dtype='object')
d2 = np.empty(shape = (len(marca_motor),len(bateria)),dtype='object')

if len(bateria) == 1:
    select_bateria = navegador.find_element_by_xpath('//*[@id="inBCell"]')
    opcao_bateria = Select(select_bateria)
        
    opcao_bateria.select_by_visible_text(bateria[z])
            
    select_s = navegador.find_element_by_xpath('//*[@id="inBS"]')
    select_s.send_keys(s)
    select_s.send_keys(Keys.ARROW_LEFT)
    select_s.send_keys(Keys.BACKSPACE)


    select_pas = navegador.find_element_by_xpath('//*[@id="inPBlades"]')
    select_pas.send_keys(pas)
    select_pas.send_keys(Keys.ARROW_LEFT)
    select_pas.send_keys(Keys.BACKSPACE)
    
    
    select_quadro = navegador.find_element_by_xpath('//*[@id="inGFrame"]')
    select_quadro.send_keys(quadro)
    select_quadro.send_keys(Keys.ARROW_LEFT)
    select_quadro.send_keys(Keys.ARROW_LEFT)
    select_quadro.send_keys(Keys.ARROW_LEFT)
    select_quadro.send_keys(Keys.BACKSPACE)
    select_quadro.send_keys(Keys.BACKSPACE)
    select_quadro.send_keys(Keys.BACKSPACE)

    select_helice = navegador.find_element_by_xpath('//*[@id="inPType"]')
    opcao_helice = Select(select_helice)
    opcao_helice.select_by_visible_text(helice)

    diametro = navegador.find_element_by_xpath('//*[@id="inPDiameter"]')
    if float(diametro_helice).is_integer():
        diametro.send_keys(Keys.BACKSPACE)
        diametro.send_keys(diametro_helice)
        diametro.send_keys(Keys.ARROW_LEFT)
        diametro.send_keys(Keys.ARROW_LEFT)
        diametro.send_keys(Keys.BACKSPACE)
    else:
        diametro.send_keys(Keys.BACKSPACE)
        diametro.send_keys(diametro_helice)
        diametro.send_keys(Keys.ARROW_LEFT)
        diametro.send_keys(Keys.ARROW_LEFT)
        diametro.send_keys(Keys.ARROW_LEFT)
        diametro.send_keys(Keys.BACKSPACE)

    passo = navegador.find_element_by_xpath('//*[@id="inPPitch"]')
    if  float(passo_helice).is_integer():
        if len(diametro_helice) == 1:
            diametro.send_keys(Keys.BACKSPACE) 
            diametro.send_keys(diametro_helice)
            diametro.send_keys(Keys.ARROW_LEFT)
            diametro.send_keys(Keys.BACKSPACE)
        else:
            diametro.send_keys(Keys.BACKSPACE) 
            diametro.send_keys(diametro_helice)
            diametro.send_keys(Keys.ARROW_LEFT)
            diametro.send_keys(Keys.ARROW_LEFT)
            diametro.send_keys(Keys.BACKSPACE)
    else:
        passo.send_keys(Keys.BACKSPACE)
        passo.send_keys(Keys.BACKSPACE)
        passo.send_keys(passo_helice)
        passo.send_keys(Keys.ARROW_LEFT)
        passo.send_keys(Keys.ARROW_LEFT)
        passo.send_keys(Keys.ARROW_LEFT)
        passo.send_keys(Keys.BACKSPACE)
            
    select_ESC = navegador.find_element_by_xpath('//*[@id="inEType"]')
    opcao_ESC = Select(select_ESC)
    opcao_ESC.select_by_visible_text(ESC)
    
    for j in range(0,len(marca_motor)):
        
        z = 0
        


        #inicio da automatização


        
        #Fim do Login

        #inicio da inserção de dados

        #caso bateria,ESC,Helice fixas:
        
        

        select_motor_marca = navegador.find_element_by_xpath('//*[@id="inMManufacturer"]')
        opcao_motor_marca = Select(select_motor_marca)
        opcao_motor_marca.select_by_visible_text(marca_motor[j])

        sleep(1)

        select_motor_modelo = navegador.find_element_by_xpath('//*[@id="inMType"]')
        opcao_motor_modelo = Select(select_motor_modelo)
        opcao_motor_modelo.select_by_visible_text(modelo_motor[j])


        peso = navegador.find_element_by_xpath('//*[@id="inGWeight"]')
        if j > 0:
        
            peso.send_keys(Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,mass_min)
        else:
            peso.send_keys(Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,mass_min)


        sleep(0.5)

        # coluna 1: Peso total, Coluna 2: Tempo de voo, Coluna 3: Peso empuxo, Coluna 4: Empuxo especifico, Coluna 5: Peso componentes.

        #inicio da simulação e coleta de dados

        i=0
        delta = mass_max - mass_min
        Dados = np.zeros(shape = ((delta//mass_interval+1),6))
        for k in range(mass_min,mass_max+mass_interval,mass_interval):
            
            peso = navegador.find_element_by_xpath('//*[@id="inGWeight"]')
            peso.send_keys(Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,k)
            calculador = navegador.find_element_by_xpath('//*[@id="theForm"]/table/tbody/tr[5]/td[17]/input')
            calculador.click()
            sleep(1.5)
            Peso_total = navegador.find_element_by_xpath('//*[@id="outTotAUW"]').text
            Tempo_de_voo = navegador.find_element_by_xpath('//*[@id="outBHoverFlightTime"]').text
            Peso_empuxo = navegador.find_element_by_xpath('//*[@id="outTotThrustWeight"]').text
            Empuxo_esp = navegador.find_element_by_xpath('//*[@id="outPEfficiency"]').text
            Peso_comp = navegador.find_element_by_xpath('//*[@id="outTotDriveWeight"]').text
            Velocidade_max = navegador.find_element_by_xpath('//*[@id="outCopterV"]').text
            
            Dados[i,0] = Peso_total
            Dados[i,1] = Tempo_de_voo
            Dados[i,2] = Peso_empuxo
            Dados[i,3] = Empuxo_esp
            Dados[i,4] = Peso_comp
            Dados[i,5] = Velocidade_max
            
            i += 1 
            
        d[0,j] = marca_motor[j] + ' ' + modelo_motor[j].replace('/','-') + ' - ' + bateria[z].replace('/','-') + ' - ' + diametro_helice + 'x' + passo_helice
        
        
        
        np.savetxt( 'csv/' + marca_motor[j] + ' ' + modelo_motor[j].replace('/','-') + ' - ' + bateria[z].replace('/','-') + ' - ' + diametro_helice + 'x' + passo_helice + '.csv', Dados, delimiter=",",fmt='%1.3f')

    
    
    for x in range(0,len(marca_motor)):
        n[0,x] = marca_motor[x] + ' ' + modelo_motor[x].replace('/','-')  
    
    t[0,0] = bateria[z].replace('/','-') + ' ' + s + 'S' + ' - ' + helice + ' ' + diametro_helice + 'x' + passo_helice + ' ' + ESC
    
    np.savetxt('data/d.csv', d, delimiter=",",fmt='%s')
    
    np.savetxt('data/n.csv', n, delimiter=",",fmt='%s')
    
    np.savetxt('data/t.csv', t, delimiter=",",fmt='%s')

if len(bateria) > 1:
    
    
    select_s = navegador.find_element_by_xpath('//*[@id="inBS"]')
    select_s.send_keys(s)
    select_s.send_keys(Keys.ARROW_LEFT)
    select_s.send_keys(Keys.BACKSPACE)
    select_quadro = navegador.find_element_by_xpath('//*[@id="inGFrame"]')
    select_quadro.send_keys(quadro)
    select_quadro.send_keys(Keys.ARROW_LEFT)
    select_quadro.send_keys(Keys.ARROW_LEFT)
    select_quadro.send_keys(Keys.ARROW_LEFT)
    select_quadro.send_keys(Keys.BACKSPACE)
    select_quadro.send_keys(Keys.BACKSPACE)
    select_quadro.send_keys(Keys.BACKSPACE)
    
    
    select_pas = navegador.find_element_by_xpath('//*[@id="inPBlades"]')
    select_pas.send_keys(pas)
    select_pas.send_keys(Keys.ARROW_LEFT)
    select_pas.send_keys(Keys.BACKSPACE)
    
    
    select_helice = navegador.find_element_by_xpath('//*[@id="inPType"]')
    opcao_helice = Select(select_helice)
    opcao_helice.select_by_visible_text(helice)

    diametro = navegador.find_element_by_xpath('//*[@id="inPDiameter"]')
    if float(diametro_helice).is_integer():
        if len(diametro_helice) == 1:
            diametro.send_keys(Keys.BACKSPACE) 
            diametro.send_keys(diametro_helice)
            diametro.send_keys(Keys.ARROW_LEFT)
            diametro.send_keys(Keys.BACKSPACE)
        else:
            diametro.send_keys(Keys.BACKSPACE) 
            diametro.send_keys(diametro_helice)
            diametro.send_keys(Keys.ARROW_LEFT)
            diametro.send_keys(Keys.ARROW_LEFT)
            diametro.send_keys(Keys.BACKSPACE)  
    else:
        diametro.send_keys(Keys.BACKSPACE)
        diametro.send_keys(diametro_helice)
        diametro.send_keys(Keys.ARROW_LEFT)
        diametro.send_keys(Keys.ARROW_LEFT)
        diametro.send_keys(Keys.ARROW_LEFT)
        diametro.send_keys(Keys.BACKSPACE)


    passo = navegador.find_element_by_xpath('//*[@id="inPPitch"]')
    if  float(passo_helice).is_integer():
        passo.send_keys(Keys.BACKSPACE)
        passo.send_keys(Keys.BACKSPACE)
        passo.send_keys(passo_helice)
        passo.send_keys(Keys.ARROW_LEFT)
        passo.send_keys(Keys.BACKSPACE)
    else:
        passo.send_keys(Keys.BACKSPACE)
        passo.send_keys(Keys.BACKSPACE)
        passo.send_keys(passo_helice)
        passo.send_keys(Keys.ARROW_LEFT)
        passo.send_keys(Keys.ARROW_LEFT)
        passo.send_keys(Keys.ARROW_LEFT)
        passo.send_keys(Keys.BACKSPACE)

    
    
    
    for j in range(0,len(marca_motor)):
        for z in range(0,len(bateria)):
            
            


            #inicio da automatização


            
            #Fim do Login

            #inicio da inserção de dados

            #caso bateria,ESC,Helice fixas:
            
            select_bateria = navegador.find_element_by_xpath('//*[@id="inBCell"]')
            opcao_bateria = Select(select_bateria)
        
            opcao_bateria.select_by_visible_text(bateria[z])
            
            select_ESC = navegador.find_element_by_xpath('//*[@id="inEType"]')
            opcao_ESC = Select(select_ESC)
            opcao_ESC.select_by_visible_text(ESC)

            select_motor_marca = navegador.find_element_by_xpath('//*[@id="inMManufacturer"]')
            opcao_motor_marca = Select(select_motor_marca)
            opcao_motor_marca.select_by_visible_text(marca_motor[j])

            sleep(1)

            select_motor_modelo = navegador.find_element_by_xpath('//*[@id="inMType"]')
            opcao_motor_modelo = Select(select_motor_modelo)
            opcao_motor_modelo.select_by_visible_text(modelo_motor[j])

            
            peso = navegador.find_element_by_xpath('//*[@id="inGWeight"]')
            if j > 0:
            
                peso.send_keys(Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,mass_min)
            elif z>0:
                peso.send_keys(Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,mass_min) 
            else:
                peso.send_keys(Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,mass_min)


            sleep(0.5)

            # coluna 1: Peso total, Coluna 2: Tempo de voo, Coluna 3: Peso empuxo, Coluna 4: Empuxo especifico, Coluna 5: Peso componentes, coluna 6: velocidade_max

            #inicio da simulação e coleta de dados

            i=0
            delta = mass_max - mass_min
            Dados = np.zeros(shape = ((delta//mass_interval+1),6))
            for k in range(mass_min,mass_max+mass_interval,mass_interval):
                
                peso = navegador.find_element_by_xpath('//*[@id="inGWeight"]')
                peso.send_keys(Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,k)
                calculador = navegador.find_element_by_xpath('//*[@id="theForm"]/table/tbody/tr[5]/td[17]/input')
                calculador.click()
                sleep(1.5)
                Peso_total = navegador.find_element_by_xpath('//*[@id="outTotAUW"]').text
                Tempo_de_voo = navegador.find_element_by_xpath('//*[@id="outBHoverFlightTime"]').text
                Peso_empuxo = navegador.find_element_by_xpath('//*[@id="outTotThrustWeight"]').text
                Empuxo_esp = navegador.find_element_by_xpath('//*[@id="outPEfficiency"]').text
                Peso_comp = navegador.find_element_by_xpath('//*[@id="outTotDriveWeight"]').text
                Velocidade_max = navegador.find_element_by_xpath('//*[@id="outCopterV"]').text
                
                Dados[i,0] = Peso_total
                Dados[i,1] = Tempo_de_voo
                Dados[i,2] = Peso_empuxo
                Dados[i,3] = Empuxo_esp
                Dados[i,4] = Peso_comp
                Dados[i,5] = Velocidade_max
                
                
                i += 1 
                
            d2[j,z] = marca_motor[j] + ' ' + modelo_motor[j].replace('/','-') + ' - ' + bateria[z].replace('/','-') + ' - ' + diametro_helice + 'x' + passo_helice
            
            
            np.savetxt( 'csv/' + marca_motor[j] + ' ' + modelo_motor[j].replace('/','-') + ' - ' + bateria[z].replace('/','-') + ' - ' + diametro_helice + 'x' + passo_helice + '.csv', Dados, delimiter=",",fmt='%1.3f')

        t2[0,j] = marca_motor[j] + ' ' + modelo_motor[j].replace('/','-') + ' - ' + helice + ' ' + diametro_helice + 'x' + passo_helice + ' ' + ESC
    
    for x in range(0,len(bateria)):
        n2[0,x] = bateria[x].replace('/','-') + ' ' + s + 'S'
            
    np.savetxt('data/dB.csv', d2, delimiter=",",fmt='%s')
    np.savetxt('data/nB.csv', n2, delimiter=",",fmt='%s')
    np.savetxt('data/tB.csv', t2, delimiter=",",fmt='%s')       




navegador.close()
