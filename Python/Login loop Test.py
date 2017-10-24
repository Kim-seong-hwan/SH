from selenium import webdriver
import time


count = 3
for i in range(0, count):

 driver = webdriver.Firefox()
 driver.get("http://www.daum.net/?t__nil_top=refresh&nil_rc=C6CIwH")


 driver.find_element_by_id("id").click()
 driver.find_element_by_id("id").clear()
 driver.find_element_by_id("id").send_keys("xxxxx")
 driver.find_element_by_id("inputPwd").clear()
 driver.find_element_by_id("inputPwd").send_keys("xxxxxxx")
 driver.find_element_by_id('loginSubmit').click()
 time.sleep(2)
 driver.quit()
 time.sleep(1)


 print ('=============== Done (%d) ===============' % i)
