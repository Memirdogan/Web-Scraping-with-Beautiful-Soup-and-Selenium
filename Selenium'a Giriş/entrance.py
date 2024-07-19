# Selenium, web tarayıcılarını otomatize etmek için kullanılan açık kaynaklı bir test otomasyon aracıdır

"""
Neden Selenium?

* JavaScript ile etkileşimde bulunabilir

* Dinamik etkileşime açıktır

* Tarayıcıyı otomatik olarak kontrol eder

* Dezavantajı: BeautifulSoup'a göre biraz daha yavaş
"""

#################
# Getting Started
#################
# pip install selenium

# Webdriver istediğimiz tarayıcıyı açmamıza ve kontrol etmemize yarıyor
from selenium import webdriver

options = webdriver.ChromeOptions()
# options.add_argument("--headless") # tarayıcı açıldığında arka planda çalışır az ram yer


driver = webdriver.Chrome(options)  # chrome tarayıcısını değişkene eşitleyerek erişilebilir hale getirdik
driver.get("https://www.example.com")  # açılan tarayıcıda istenilen sayfaya gider
driver.title  # sayfanın başlığını çekme
driver.current_url  # tarayıcıda açık olan linki görme
# driver.quit()  # açılan tarayıcıyı kapatır
