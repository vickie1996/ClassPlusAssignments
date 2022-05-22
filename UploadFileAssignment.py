from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.techlistic.com/p/selenium-practice-form.html')
driver.implicitly_wait(10)

driver.maximize_window()
driver.find_element(By.XPATH, "//a[@id='cookieChoiceDismiss']").click()
print("Cookies Closed")
driver.find_element(By.NAME, "firstname").send_keys("Vivek")
print("First Name Entered")
driver.find_element(By.NAME, "lastname").send_keys("Berwal")
print("Last Name Entered")
driver.find_element(By.XPATH, "//input[@value='Male']").click()
print("Gender Entered")
driver.find_element(By.XPATH, "//input[@value='3']").click()
print("Experience")
driver.find_element(By.XPATH, "//input[@id='datepicker']").send_keys("5/20/2022")
print("Date Entered")
driver.find_element(By.XPATH, "//input[@value='Automation Tester']").click()
print("Profession Entered")
driver.find_element(By.XPATH, "//input[@value='Selenium Webdriver']").click()
print("Automation tools Entered")

time.sleep(10)
########################Continent###################
dropdown = driver.find_element(By.XPATH,"//select[@name='continents']")
dropdown.find_element(By.XPATH,"//option[. = 'Asia']").click()
print("Continent Entered")

#######################Selenium Commands###########################
dropdown = driver.find_element(By.XPATH,"//select[@id='selenium_commands']")
dropdown.find_element(By.XPATH,"//option[.='WebElement Commands']").click()
print("Selenium command Entered")

########################Scrolling######################################
element = driver.find_element(By.XPATH, "//input[@name='photo']")
actions = ActionChains(driver);
actions.move_to_element(element);

#############################Image Upload##########################
imageUpload = driver.find_element(By.XPATH, "//input[@name='photo']")
imageUpload.send_keys("/home/c-vivekb/Downloads/AppleTV-logo.png")  #give any path of image in local system
print("Image Uploaded")

########################################################################################################################################################
##############################   USE THIS CODE TO HANDLE AD IF IS STATIC#########################################################
#Download is opening a link and in that link Ad coming is Dynamic by which its getting hard to get the locators for the same because everytime it changing
# print("Main window")
# driver.find_element(By.LINK_TEXT, "Click here to Download File").click()
# print("File Downloaded")
# print("AD window")
# time.sleep(5)

####################### #Iframe Ad closing#####################
# iFrame = driver.find_element(By.ID, "google_ads_iframe_/1254144,22662382379/techlistic_com-pixel1_0")
# driver.switch_to.frame(iFrame)
# driver.find_element(By.XPATH, "//div[@id='dismiss-button']").click()
# print("Github window")
#############################################################################################################################################################

time.sleep(5)
driver.back()

###############Submit##################
driver.find_element(By.ID, "submit").click()
print("Submit")
driver.close()
