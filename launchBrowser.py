#launch the browser

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time


driver=webdriver.Chrome(executable_path='C:\\Users\\Emp ID - 1481\\PycharmProjects\\python_selenium\\drivers\\chromedriver.exe')

driver.get("https://www.google.com/")

driver.maximize_window()




#just testing another youtube(maximize,minimize)
'''
from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path='C:\\Users\\Emp ID - 1481\\PycharmProjects\\python_selenium\\drivers\\chromedriver.exe')


driver.get("https://www.youtube.com/")

driver.find_element_by_name("search_query").send_keys('nikhil an actor')
driver.maximize_window()
time.sleep(4)
driver.minimize_window()

driver.quit()
'''
