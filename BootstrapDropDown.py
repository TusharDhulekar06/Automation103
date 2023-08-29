import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

service = ChromeService(executable_path=ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.implicitly_wait(10)
driver.maximize_window()

driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()
countrylist=driver.find_elements(By.XPATH,"//ul[@id='select2-billing_country-results']/li")
print(len(countrylist))
for contry in countrylist:
    if contry.text=='Angola':
        contry.click()
        break
time.sleep(5)