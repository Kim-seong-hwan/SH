import pyautogui
import time
import unittest




pyautogui.doubleClick(507, 400)
prompt = (2)
for i in range(0, prompt):

    time.sleep(3)
    pyautogui.typewrite('COMMENT Test (%d)' % i, 0.25)
    time.sleep(2)
    pyautogui.click(550, 428)
    time.sleep(2)
    pyautogui.click(507, 400)




    print ('=============== Done (%d) ===============' % i)


if __name__ == '__main__':
    unittest.main()