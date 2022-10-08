from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self,driver):
        self.driver=driver

    __signupbtn=(By.XPATH,"//a[@id='home-lnk-siup']")

    def clickSignup(self):
        self.driver.find_element(*self.__signupbtn).click()


