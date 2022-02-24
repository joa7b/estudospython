import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

contatos_df = pd.read_excel('') #insira a planilha aqui
midia = '' #insira a midia aqui

#Abre o Chrome
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://web.whatsapp.com/') #abre o site Whatsapp Web

while len(driver.find_elements_by_id('side')) < 1: #reconhece o carregamento
	time.sleep(1)

#lendo a planilha
for i, mensagem in enumerate(contatos_df['Mensagem']):
	pessoa = contatos_df.loc[i, 'Pessoa']
	numero = contatos_df.loc[i, 'Número']
	link = f'https://web.whatsapp.com/send?phone={numero}'
	driver.get(link)
	while len(driver.find_elements_by_id('side')) < 1: #reconhece o carregamento
		time.sleep(15)

#enviando midia
	driver.find_element_by_css_selector("span[data-icon='clip']").click()
    attach = driver.find_element_by_css_selector("input[type='file']")
    attach.send_keys(midia)
    time.sleep(3)
    send = driver.find_element_by_css_selector("span[data-icon='send']")
    send.click()
    time.sleep(10)   


