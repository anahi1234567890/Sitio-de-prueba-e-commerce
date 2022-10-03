from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium .webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import time

driver = webdriver.Chrome(executable_path=r"D:\User\Anahi\Documents\Escuela\SEMESTRE_7\SQA\chromedriver.exe")
url = "https://demoblaze.com/index.html"

driver.maximize_window()
driver.get(url)
alert = Alert(driver)


#Sign up
def sign_up():
    driver.find_element(By.ID, "signin2").click()
    time.sleep(2)

    user = driver.find_element(By.ID,"sign-username")
    user.send_keys("Anahi")
    password = driver.find_element(By.ID,"sign-password")
    password.send_keys("aft5890A")
    user.send_keys(Keys.ENTER)

    driver.find_element(By.XPATH, "//*[@id='signInModal']/div/div/div[3]/button[2]").click()
    time.sleep(2)
    alert.accept()
    
#Login
def login():
    driver.find_element(By.ID, "login2").click()
    time.sleep(2)

    user = driver.find_element(By.ID,"loginusername")
    user.send_keys("Anahi")
    password = driver.find_element(By.ID,"loginpassword")
    password.send_keys("aft5890A")
    user.send_keys(Keys.ENTER)

    driver.find_element(By.XPATH, "//*[@id='logInModal']/div/div/div[3]/button[2]").click()
    time.sleep(2)

#Add to cart
def add_cart():

    articles = {
            "Phones" : ['//*[@id="tbodyid"]/div[4]/div/div/h4/a', '//*[@id="tbodyid"]/div[7]/div/div/h4/a'],
            "Laptops" : ['//*[@id="tbodyid"]/div[5]/div/div/h4/a', '//*[@id="tbodyid"]/div[2]/div/div/h4/a'],
            "Monitors" : ['//*[@id="tbodyid"]/div[1]/div/div/h4/a', '//*[@id="tbodyid"]/div[2]/div/div/h4/a']
            }


login()
add_cart()
time.sleep(2)
