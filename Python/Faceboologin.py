from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

import unittest
import time

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.facebook.com/")

    def test_login(self):

        driver = self.driver
        un = "xxxx@xxxx.com"
        pw = "xxxxxxx"
        emailF      = "email"
        passF       = "pass"
        loginbutton = "//input[@value='로그인']"



        emailFElement = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_id(emailF))
        passFElement = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_id(passF))
        loginbuttonElement = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_xpath(loginbutton))



        emailFElement.clear()
        emailFElement.send_keys(un)
        time.sleep (1)
        passFElement.clear()
        passFElement.send_keys(pw)
        time.sleep (1)
        loginbuttonElement.click()




        def tearDown(self):
            self.driver.quit()



if __name__ == '__main__':
    unittest.main()



