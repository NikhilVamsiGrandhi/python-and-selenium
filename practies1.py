# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# import time
#
#
# def main():
#     # Setup ChromeDriver using WebDriverManager
#     driver = webdriver.Chrome(
#         executable_path="C:\\Users\\Emp ID - 1481\\PycharmProjects\\python_selenium\\drivers\\chromedriver.exe")
#     driver.get('https://demo.opencart.com/')
#
#     responseText1=fetchAllTabs(driver)
#     time.sleep(1)
#
#     moveToAllNav(driver, responseText1)
#
#     driver.close()
#
#
# def fetchAllTabs(driver):
#     driver.maximize_window()
#     menuElement = driver.find_element(By.XPATH, "//nav[@id='menu']")
#     #nav_links = menuElement.find_elements(By.TAG_NAME, "a")
#     responseText = menuElement.text
#
#     return responseText
#
#
# def moveToAllNav(driver, nav_links):
#     driver.maximize_window()
#     actions = ActionChains(driver)
#
#     for link in nav_links:
#         print(link)
#         linkAncors=driver.find_element(By.LINK_TEXT, "link")
#         linkAncorsforEach=linkAncors.find_elements(By.TAG_NAME,"a")
#         #link_text = link.text
#
#
#         # Perform a move action to hover over the link
#         actions.move_to_element(linkAncorsforEach).perform()
#         #
#
#         # Do something with the link (you can add your actions here)
#         #print(f"Hovered over: {link}")
#
#         # Navigate back to the original page
#         # actions.move_to_element(nav_links[0]).perform()
#         # time.sleep(2)
#
#
#
# main()



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# import time
#
#
# def main():
#     # Setup ChromeDriver using WebDriverManager
#     driver = webdriver.Chrome(
#         executable_path="C:\\Users\\Emp ID - 1481\\PycharmProjects\\python_selenium\\drivers\\chromedriver.exe")
#     driver.get('https://demo.opencart.com/')
#
#     responseText1 = fetchAllTabs(driver)
#     time.sleep(1)
#
#     moveToAllNav(driver, responseText1)
#
#     driver.close()
#
#
# def fetchAllTabs(driver):
#     driver.maximize_window()
#     menuElement = driver.find_element(By.XPATH, "//nav[@id='menu']")
#     nav_links = menuElement.find_elements(By.TAG_NAME, "a")
#     return nav_links
#
#
# def moveToAllNav(driver, nav_links):
#     driver.maximize_window()
#     actions = ActionChains(driver)
#
#     for link in nav_links:
#         # Get the text of the navigation link
#         link_text = link.text
#
#         # Perform a move action to hover over the link
#         actions.move_to_element(link).perform()
#         #time.sleep(2)
#
#         # Do something with the link (you can add your actions here)
#         print(f"Hovered over: {link_text}")
#
#         # Navigate back to the original page
#         # actions.move_to_element(nav_links[0]).perform()
#         #time.sleep(2)
#
#
#
# main()


#navigating through nav_bar names dinamically

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def main():
    name = input("Enter nav_name:- ")
    sub_name = input("Enter nav_sub_name:- ")
    driver = webdriver.Chrome(executable_path="C:\\Users\\Emp ID - 1481\\PycharmProjects\\python_selenium\\drivers\\chromedriver.exe")
    driver.get('https://demo.opencart.com/')
    driver.maximize_window()
    fetchAllTabs(driver)
    time.sleep(1)
    navigate(driver,name,sub_name)

def fetchAllTabs(driver):
    driver.maximize_window()
    menuElement = driver.find_element(By.XPATH, "//nav[@id='menu']")
    responseText = menuElement.text
    print(responseText)


def navigate(driver, name, sub_name):
    nav_button=driver.find_element(By.LINK_TEXT,name)
    nav_button.click()
    time.sleep(2)

    if nav_button.is_enabled():
        driver.find_element(By.PARTIAL_LINK_TEXT,sub_name).click()
        current_tittle=driver.title
        #click_name=driver.title
        time.sleep(2)
        driver.back()
        time.sleep(2)

        ##it about the link
        # expected_url = 'https://demo.opencart.com/index.php?route=product/category&path=20'
        # if driver.current_url!= expected_url:
        #     print("Navigation to 'Monitors' was successful.")
        # else:
        #     print("Navigation to 'Monitors' was not successful.")

        #condtion with tittle

        if sub_name==current_tittle:
            print("Navigation to 'Monitors' was successful.")
        else:
            print("Navigation to 'Monitors' was not successful.")


main()

