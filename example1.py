from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\Users\\Emp ID - 1481\\PycharmProjects\\python_selenium\\drivers\\chromedriver.exe")
driver.get('https://demo.opencart.com/')

def fetchAllTabs():
    driver.maximize_window()
    all_responses = driver.find_elements(By.XPATH, "//*[@id='menu']")

    response_text = []

    for i in all_responses:
        response_text.append(i.text)

    print(*response_text)

    driver.quit()
#
fetchAllTabs()


#for opening mac

# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# import time
#
#
#
# def main():
#     # Setup ChromeDriver using WebDriverManager
#     driver = webdriver.Chrome(executable_path="C:\\Users\\Emp ID - 1481\\PycharmProjects\\python_selenium\\drivers\\chromedriver.exe")
#     driver.get('https://demo.opencart.com/')
#
#
#     fetchAllTabs(driver)
#     time.sleep(1)
#
#     Navigate(driver)
#     time.sleep(1)
#
#     validateTabSwitch(driver)
#     driver.back()
#     time.sleep(2)
#     #responseText1=fetchAllTabs(driver)
#     #moveToAllnav(driver,responseText1)
#
#     driver.close()
#
#
# def fetchAllTabs(driver):
#     driver.maximize_window()
#     menuElement = driver.find_element(By.XPATH, "//nav[@id='menu']")
#     responseText = menuElement.text
#     return (responseText)
#
# def moveToAllnav(driver,responseText1):
#         driver.maximize_window()
#         actions=ActionChains(driver)
#         for i in responseText1:
#             actions.move_to_element(By.LINK_TEXT,"i").click().perform()
#             time.sleep(2)
#             actions.back()
#
#
#
#
# def Navigate(driver):
#     driver.maximize_window()
#     desktops = driver.find_element(By.XPATH, "//div[@id='narbar-menu']/ul/li[1]/a")
#     desktops.click()
#     time.sleep(2)
#
#     if desktops.is_enabled():
#         mac = driver.find_element(By.XPATH, "//div[@id='narbar-menu']/ul/li[1]/div/div/ul/li[2]/a")
#         mac.click()
#
#
# def validateTabSwitch(driver):
#     expectedTitle = driver.find_element(By.XPATH, "//div[@id='content']/h2")
#     actualTitle = driver.find_element(By.XPATH, "/html/body/header/div")
#
#     if actualTitle.text != expectedTitle.text:
#         print("New tab successfully opened")
#     else:
#         print("Failed to open the new tab")
#
# main()

