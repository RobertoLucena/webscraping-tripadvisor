
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

#abrindo navegador
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
navegador = webdriver.Chrome()

navegador.get("https://www.tripadvisor.com.br/")

#aguardando o banner de cookies
try:
    WebDriverWait(navegador, timeout=10).until(EC.presence_of_element_located((By.ID, 'onetrust-banner-sdk')))
except:
    pass

navegador.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()

#aguardando a pesquisa ser clicável
try:
    WebDriverWait(navegador, timeout=10).until(EC.element_to_be_clickable((By.XPATH, '//input[contains(@placeholder, "Aonde você quer ir?")]')))
except:
    pass

navegador.find_element(By.XPATH, '//input[contains(@placeholder, "Aonde você quer ir?")]').click()

navegador.find_element(By.XPATH, '//input[contains(@placeholder, "Aonde você quer ir?")]').send_keys('foz do iguaçu')

#aguardando os resultados serem carregados
try:
    WebDriverWait(navegador, timeout=5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'bPaPP w z _S _F Wc Wh Q B- _G')))
except:
    pass

navegador.find_element(By.XPATH, '//*[@id="typeahead_results"]/a[1]').click()

#aguardando o carregamento dos ads
try:
   WebDriverWait(navegador, timeout=5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'ad eWQWb _h Gi f e j u')))
except:
    pass

#obtendo os resultados da pesquisa
local = navegador.find_element(By.XPATH, '//*[@id="lithium-root"]/main/div[1]/div[1]/div/h1/span/span[2]').text

resumodolocal = navegador.find_element(By.XPATH, '//*[@id="lithium-root"]/main/div[6]/div/div/div[2]/div').text

resultado = [local, resumodolocal]

pontos_turisticos = [navegador.find_element(By.XPATH, '//*[@id="lithium-root"]/main/div[7]/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div/ul/li[1]/div[1]/a/div[2]/div[1]/div').text,
                     navegador.find_element(By.XPATH, '//*[@id="lithium-root"]/main/div[7]/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div/ul/li[2]/div[1]/a/div[2]/div[1]/div').text,
                     navegador.find_element(By.XPATH, '//*[@id="lithium-root"]/main/div[7]/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div/ul/li[3]/div[1]/a/div[2]/div[1]/div').text]

#salvando os arquivos em .txt
with open('resumo_do_local', 'w', encoding='utf-8') as arquivo:
    for valor in resultado:
        arquivo.write(f'{(str(valor))}\n')
    for valor in pontos_turisticos:
        arquivo.write(f' Ponto Turístico: {(str(valor))}\n')

#fechando o navegador
navegador.quit()
