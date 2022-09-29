from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium .webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path=r"D:\User\Anahi\Documents\Escuela\SEMESTRE_7\SQA\chromedriver.exe")
url = "https://demoblaze.com/index.html"

driver.maximize_window()
driver.get(url)
time.sleep(2)

#Registro
driver.find_element(By.XPATH,"//*[@id='signin2']").click()
time.sleep(2)

usuario = driver.find_element(By.XPATH,"//*[@id='sign-username']")
usuario.send_keys("Anahi")
password = driver.find_element(By.XPATH,"//*[@id='sign-password']")
password.send_keys("aft5890A")
usuario.send_keys(Keys.ENTER)

#Ingresar
driver.find_element(By.XPATH,"//*[@id='signInModal']/div/div/div[3]/button[2]").click()
time.sleep(2)


#Agregar productos

#Carrito de compras

#Comprar (Rellenar formulario)

#Generar reporte
