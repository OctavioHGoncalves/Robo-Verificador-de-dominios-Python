from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import xlrd

print("Inciando nosso robô...\n")
arq = open("resultado.txt","w")

dominios = []
#Lendo do excel
workbook = xlrd.open_workbook("dominio.xlsx")
sheet = workbook.sheet_by_index(0)

for linha in range(0,10):
    dominios.append(sheet.cell_value(linha,0))

options = Options()

options.headless = False

options.add_argument("--start-maximized")

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
#driver = webdriver.Chrome('C:\Apps\Robos\chromedriver')
driver.get("https://registro.br/")

#dominios = ["roboscompython.com.br", "udemy.com", "uol.com.br", "pythoncurso.com"]
for dominio in dominios:
    pesquisa = driver.find_element_by_id("is-avail-field")
    pesquisa.clear()  # Limpando a barra de pesquisa
    pesquisa.send_keys(dominio)
    pesquisa.send_keys(Keys.RETURN)
    time.sleep(3)
    resultados = driver.find_elements_by_tag_name("strong")
    texto = ("Dominio %s %s\n" % (dominio, resultados[4].text))
    arq.write(texto)
arq.close()
driver.close()



