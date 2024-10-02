from flask import Flask, request, render_template
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from time import sleep
from bs4 import BeautifulSoup

app = Flask(__name__)

# Função para detectar navegador
def detectar_navigator():
    user_agent = driver.execute_script("return navigator.userAgent;")
    if "Chrome" in user_agent and "Edg" not in user_agent:
        chrome_options = ChromeOptions()
        chrome_service = ChromeService(executable_path='driver/webdriver_chrome/chrome.exe')
        driver_chrome = webdriver.Chrome(service=chrome_service, options=chrome_options)

        msg = print("Navegador em uso (Chrome):", detectar_navigator(driver_chrome))
        driver_chrome.quit()
        return msg
        
    elif "Edg" in user_agent:
        edge_options = EdgeOptions()
        edge_service = EdgeService(executable_path='driver/webdriver_edge/msedgedriver.exe')
        driver_edge = webdriver.Edge(service=edge_service, options=edge_options)

        msg = print("Navegador em uso (Edge):", detectar_navigator(driver_edge))
        return "Microsoft Edge"
    else:
        return "Unknown Browser"

# Configurando o pacote de webdriver chrome
driver = webdriver.Chrome(executable_path='driver/webdriver_chrome/chrome.exe')

url = 'https://www.caixa.gov.br/voce/habitacao/imoveis-venda/Paginas/default.aspx'

@app.route('/', methods=['GET', 'POST'])
def home():
    data = request.form # Pegar os dados do formulario enviado via post

    return render_template('index.html')

if __name__ =='__main__':
    app.run(debug=True)
