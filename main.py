#Creater Emre Osman - 03/05/2023
#Whatsapp Web Automate Photo Sender

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import time


filePath= input(str("Enter the photos location"))
name = input(str("Enter the user full name"))

def launchBrowser():
    path = "C:\Program Files (x86)\chromedriver.exe"
    options = Options()
    options.add_experimental_option("detach", True)
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(path, options=options)
    driver.get("https://web.whatsapp.com/")

    return driver


driver = launchBrowser()

input("Scan thr QR code and enter")

#accesse to user chat
user = driver.find_element(By.XPATH, "//span[@title='{}']".format(name)).click()
driver.implicitly_wait(5)

try:
    for x in os.listdir(filePath):
        if x.endswith(".png") or x.endswith(".jpg"):
            # access to file path in the folder
            photoFile = "{}\\{}".format(filePath,x)
            #send the photos to user
            driver.find_element(By.CSS_SELECTOR,"span[data-icon='clip']").click()
            time.sleep(0.2)
            driver.find_element(By.CSS_SELECTOR,"input[type='file']").send_keys(photoFile)       
            driver.find_element(By.XPATH, "//span[@data-testid='send' and @data-icon='send']").click()
            time.sleep(1)
except:
    pass      


