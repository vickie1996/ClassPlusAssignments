from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import requests

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
options = webdriver.ChromeOptions() 
driver.get('https://google.co.in/')   ##any URL can be given to find the broken links as per requirement
links = driver.find_elements(By.CSS_SELECTOR, "a")

for link in links:
    r = requests.head(link.get_attribute('href'))
    url = link.get_attribute('href')
    statusCode = r.status_code
    if statusCode == 400 or statusCode == 403 or statusCode == 404 or statusCode == 408 or statusCode == 410 or statusCode == 503:
        print("Link is broken", url)
    else:
        print("Link is not Broken : ", url)
