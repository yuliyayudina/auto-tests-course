# -*- coding: utf-8 -*-
import math
from selenium import webdriver 
import time 

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)
   
    input1 = browser.find_element_by_css_selector("form>*:nth-child(1) input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("form>*:nth-child(2) input") 
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector("form>*:nth-child(3) input")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_css_selector("form>*:nth-child(4) input")
    input4.send_keys("Russia")
    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

