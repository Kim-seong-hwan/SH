from selenium import webdriver
import time
import unittest
import xlsxwriter
import os

#크롬/파폭 동시 테스트

class Go(unittest.TestCase):

 def test1(self):

     self.driver = webdriver.Firefox()
     self.driver.get("http://naver.com")
     self.driver.find_element_by_link_text(u"카페").click()
     print("카페 이동 성공")
     time.sleep(2)
     self.driver.quit()

     chromedriver = "/Users/KimSeonHwan/Desktop/chromedriver"
     os.environ["webdriver.chrome.driver"] = chromedriver
     self.driver = webdriver.Chrome(chromedriver)
     self.driver.get("http://naver.com")
     self.driver.find_element_by_link_text(u"카페").click()
     print("카페 이동 성공")
     time.sleep(2)
     self.driver.quit()



class go2(unittest.TestCase):

 def test2(self):

     self.driver = webdriver.Firefox()
     self.driver.get("http://naver.com")
     self.driver.find_element_by_link_text(u"메일").click()
     print("메일 이동 성공")
     time.sleep(2)
     self.driver.quit()


class LoginTest(unittest.TestCase):

  def test(self):

     self.driver = webdriver.Firefox()
     self.driver.get("http://naver.com")
     self.driver.find_element_by_id("id").clear()
     self.driver.find_element_by_id("id").send_keys("ID")
     self.driver.find_element_by_id("pw").clear()
     self.driver.find_element_by_id("pw").send_keys("PW")
     self.driver.find_element_by_xpath(loginbutton).click()
     print("로그인 성공")
     time.sleep(2)

     time.sleep(2)
     self.driver.quit()


     worksheet.write('G2', 'Pass')
     worksheet.write('G3', 'Pass')
     worksheet.write('G4', 'Pass')
     workbook.close()




if __name__ == '__main__':
    unittest.main()
