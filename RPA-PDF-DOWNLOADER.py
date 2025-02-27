import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

# Configurar o WebDriver (exemplo para Chrome)
driver = webdriver.Chrome()  # Certifique-se de que o ChromeDriver está no PATH

# Navegar até a página desejada
driver.get("https://www.sindbancarios.org.br/noticia/12512/coe-entrega-pauta-de-reivindicacoes-a-direcao-do-banrisul")

# Localizar o elemento do link usando XPath
link_element = driver.find_element(By.XPATH, "//a[contains(text(), 'pauta de reivindicações')]")

# Extrair o URL do href
pdf_url = link_element.get_attribute('href')

# Fazer o download do PDF
response = requests.get(pdf_url)

# Salvar o PDF no disco
with open('C:\\Users\\aneli\\MyPy\\RPA-pdf-downloader\\pauta_de_reivindicacoes.pdf', 'wb') as file:
    file.write(response.content)


# Fechar o WebDriver
driver.quit()

print("Download concluído!")