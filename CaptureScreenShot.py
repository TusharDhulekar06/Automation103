from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
driver.implicitly_wait(10)

# driver.save_screenshot("E:\\SoftwareTesting\\Automation Testing'\\YTubeSDET\\PythonProjectSDET2\\Day23\\homepage.png")
driver.save_screenshot(os.getcwd()+"\\homepage.png") #or below driver
# driver.get_screenshot_as_file(os.getcwd()+"\\homepage.png")
driver.quit()

