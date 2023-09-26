# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver = webdriver.Chrome(executable_path="C:\\Users\\Emp ID - 1481\\PycharmProjects\\python_selenium\\drivers\\chromedriver.exe")
# driver.get('https://automationexercise.com/')
#
# driver.maximize_window()
# driver.find_element(By.XPATH,"//*[@id='header']/div/div/div/div[2]/div/ul/li[2]/a").click()
# driver.find_element(By.XPATH, '//*[@id="search_product"]').send_keys("T-shirts")
# driver.find_element(By.XPATH,'//*[@id="submit_search"]').click()
#
# time.sleep(3)
# driver.close()



from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\Emp ID - 1481\\PycharmProjects\\python_selenium\\drivers\\chromedriver.exe")
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

driver.maximize_window()
##application commands

# print(driver.title)
# print(driver.current_url)
# print(driver.page_source)

##conditional commands


driver.close()

