from selenium import webdriver
from pages.LoginPage import LoginPage
import time
class LoginTest:
    driver=webdriver.Chrome("C:/drivers/chromedriver.exe")
    driver.get("https://iq-qa.efi.com/iq/#/")
    Login=LoginPage(driver)
    Login.clickSignup()
    time.sleep(2)
    driver.back()
    driver.quit()
    print("Test Completed")


