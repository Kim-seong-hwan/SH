from selenium import webdriver
import time
import unittest
import xlsxwriter
import os

#workbook = xlsxwriter.Workbook('/Users/KimSeonHwan/Documents/CSsheet/TEST.xlsx')
#worksheet = workbook.add_worksheet()
#bold = workbook.add_format({'bold': True})

#loginbutton = "//input[@type='submit']"


class Test01_Cafe(unittest.TestCase):

 def test1(self):

     chromedriver = "/Users/KimSeonHwan/Desktop/chromedriver"
     os.environ["webdriver.chrome.driver"] = chromedriver
     self.driver = webdriver.Chrome(chromedriver)
     self.driver.get("http://www.daum.net/?t__nil_top=refresh&nil_rc=C6CIwH")
     self.driver.find_element_by_link_text(u"카페").click()
     time.sleep(2)
     print("크롬 카페 이동 성공")

     self.driver.quit()

     #worksheet.write('G2', 'Pass')
     self.driver = webdriver.Firefox()
     self.driver.get("http://www.daum.net/?t__nil_top=refresh&nil_rc=C6CIwH")
     self.driver.find_element_by_link_text(u"카페").click()
     time.sleep(2)
     print("파이어폭스 카페 이동 성공")

     self.driver.quit()

     #worksheet.write('H2', 'Pass')


class Test02_Login(unittest.TestCase):


  def test2(self):

     chromedriver = "/Users/KimSeonHwan/Desktop/chromedriver"
     os.environ["webdriver.chrome.driver"] = chromedriver
     self.driver = webdriver.Chrome(chromedriver)
     self.driver.get("http://www.daum.net/?t__nil_top=refresh&nil_rc=C6CIwH")
     self.driver.find_element_by_id("id").clear()
     self.driver.find_element_by_id("id").send_keys("xxxxxx")
     self.driver.find_element_by_id("inputPwd").clear()
     self.driver.find_element_by_id("inputPwd").send_keys("xxxxx")
     self.driver.find_element_by_id('loginSubmit').click()
     time.sleep(2)
     print("크롬 로그인 성공")

     self.driver.quit()

     #worksheet.write('C4', 'Pass')

     self.driver = webdriver.Firefox()
     self.driver.get("http://www.daum.net/?t__nil_top=refresh&nil_rc=C6CIwH")
     self.driver.find_element_by_id("id").clear()
     self.driver.find_element_by_id("id").send_keys("xxxx")
     self.driver.find_element_by_id("inputPwd").clear()
     self.driver.find_element_by_id("inputPwd").send_keys("xxxxx")
     self.driver.find_element_by_id('loginSubmit').click()
     time.sleep(2)
     print("파이어폭스 로그인 성공")

     self.driver.quit()

     #worksheet.write('D4', 'Pass')

class Test03_Blog(unittest.TestCase):

 def test3(self):

     chromedriver = "/Users/KimSeonHwan/Desktop/chromedriver"
     os.environ["webdriver.chrome.driver"] = chromedriver
     self.driver = webdriver.Chrome(chromedriver)
     self.driver.get("http://www.daum.net/?t__nil_top=refresh&nil_rc=C6CIwH")
     self.driver.find_element_by_link_text(u"블로그").click()
     time.sleep(2)
     print("크롬 블로그 이동 성공")

     self.driver.quit()


     self.driver = webdriver.Firefox()
     self.driver.get("http://www.daum.net/?t__nil_top=refresh&nil_rc=C6CIwH")
     self.driver.find_element_by_link_text(u"블로그").click()
     time.sleep(2)
     print("파이어폭스 블로그 이동 성공")

     self.driver.quit()

     #worksheet.write('G4', 'Pass')
     #workbook.close()


if __name__ == '__main__':
    unittest.main()
