# Importando as bibliotecas
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
from time import sleep

#  Abrir o Microsoft Edge
driver = webdriver.Edge(service=Service('driver/webdriver_edge/msedgedriver.exe'))
url = 'https://venda-imoveis.caixa.gov.br/sistema/busca-imovel.asp?sltTipoBusca=imoveis'

# Aguardando 10 segundos para finalizar
sleep(10)

# Acessando a página no navegador
driver.get(url)

# Seleciona o estado e a cidade
wait = WebDriverWait(driver,20)

# Criar uma instancia da classe select para o estado
select_estado = driver.find_element(By.XPATH,'//*[@id="cmb_estado"]')
select_estado.send_keys(Keys.DOWN) # Seleciona o estado desejado
for char in "SP":
    select_estado.send_keys(char)

select_estado.send_keys(Keys.ENTER)

select_city = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="cmb_cidade"]')))
select_city.select_by_value('SAO PAULO') # Selecione o cidade desejada

select_modality = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="cmb_modalidade"]')))
select_modality.select_by_value('Concorrência Pública')

# Clicar no btn para efetuar a busca
btn_buscar = wait.until(EC.presence_of_element_located((By.XPATH,' //*[@id="btn_next0"]')))
btn_buscar.click()

sleep(3) # Aguardando atualização

# Extrai os dados dos imóveis (ajuste os XPath's conforme necessário)
wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="resultado-busca"]')))  # Aguarda a carga dos resultados
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

imoveis = soup.find_all('div', class_='imovel')
dados_imoveis = []
for imovel in imoveis:
    preco = imovel.find('span', class_='preco').text.strip()
    area = imovel.find('span', class_='area').text.strip()
    quartos = imovel.find('span', class_='quartos').text.strip()
    # ... adicione mais dados conforme necessário ...
    dados_imoveis.append([preco, area, quartos])


# 3 Salvar os dados em um arquivo CSV =========================================================================================
import pandas as pd
# Cria um DataFrame
df = pd.DataFrame(dados_imoveis, columns=['Preço', 'Área', 'Quartos'])

# Salva em CSV
df.to_csv('imoveis_caixa.csv', index=False)

# 4 Apresentar na página web os dados extraidos ===============================================================================

driver.quit()