from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path=r"D:\User\Anahi\Documents\Escuela\SEMESTRE_7\SQA\chromedriver.exe")
action = ActionChains(driver)
url = "https://demoblaze.com/index.html"

driver.maximize_window()
driver.get(url)
time.sleep(3)

#Registro
driver.find_element(By.XPATH,"//*[@id='signin2']").click()
time.sleep(3)

#Ingresar

#Agregar productos

#Carrito de compras

#Comprar (Rellenar formulario)

#Generar reporte
