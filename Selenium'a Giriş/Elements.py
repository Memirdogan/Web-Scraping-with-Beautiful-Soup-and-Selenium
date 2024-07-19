#############################################
# Finding Elements and Extracting Data
#############################################

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.example.com")

# elementleri bulma komutu
element_a = driver.find_element(By.XPATH, "//a")
# 1. argüman bulunacak element hangi yolla bulunacak
# 2. argüman bulunacak elementi bulduran sorgu

element_a.text
element_a.get_attribute("innerText") # text ile aynı
element_a.get_attribute("href")
element_a.get_attribute("innerHTML")





#############################################
# Finding Elements and Extracting Data (better method)
#############################################

# driver'ı get ettikten sonra web sayfası tam yüklenmeden diğer kodlar çalıştığı için elementler bulunamayabiliyor
# çözümü birkaç kütüphane vs

from selenium import webdriver
from selenium.webdriver.common.by import By

import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver.get("https://www.example.com")
time.sleep(2)
# sorgu kodları .......//a
# sorgu kodları .......//h1


selector = (By.XPATH, "//p") #seçici sorgumuz
wait = WebDriverWait(driver, 10) #10 sn delay atıyoruz
p_element = wait.until(EC.visibility_of_element_located(selector)) # selectorün sorgusundaki element görünenebilir olana kadar wait süreci boyunca bekle sorguyu yapmak için
# eğer wait üresi içerisinde sorgu görünür olmazsa (10sn) hata mesajı geliyor


driver.find_elements() # find_all gibi tüm elementleri liste halinde dönrürür
p_elements = driver.find_elements(By.XPATH, "//p")


elem = None
if p_elements:
    elem = p_elements[0]
else:
    print("elements not found")

print(elem)




#######################################################
# Interacting with Elements (elementler ile etkileşim)
#######################################################

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.miuul.com")
time.sleep(2)

btn_elements = driver.find_elements(By.XPATH,"//a[@id='login']")
btn = btn_elements[0]
btn.click()

input_elements = driver.find_elements(By.XPATH,"//input[@name = 'arama']")
input = input_elements[0]
input.send_keys("data science", Keys.ENTER)