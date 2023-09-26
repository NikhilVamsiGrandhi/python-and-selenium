#login github account and printing it is successful are not

'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\Emp ID - 1481\\PycharmProjects\\python_selenium\\drivers\\chromedriver.exe")

driver.get("https://github.com/login")

# Find the username and password input fields and the login button
time.sleep(2)
driver.find_element(By.ID,"login_field").send_keys("nikhil.grandhi@kanerika.com")
time.sleep(2)
driver.find_element_by_id('password').send_keys("Nikhil@5775")
driver.find_element_by_name('commit').click()

driver.maximize_window()
name_obj=driver.title

if name_obj=="GitHub":
    print('login is succesfull')
else:
    print("login fail")

time.sleep(3)
driver.quit()
'''

'''
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="C:\\Users\\Emp ID - 1481\\PycharmProjects\\python_selenium\\drivers\\chromedriver.exe")
driver.get('https://demo.nopcommerce.com/')

# serv_obj=Service("C:\\Users\\Emp ID - 1481\\PycharmProjects\\python_selenium\\drivers\\chromedriver.exe")
# driver=webdriver.Chrome(service=serv_obj)  {not working}

driver.maximize_window()
#driver.find_element(By.ID,"small-searchterms").send_keys("Lenovo Thinkpad X1 Caebon Laptop")
driver.find_element(By.LINK_TEXT,"Register").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Reg").click()
driver.quit()
'''

#css selectors (tag and id)


# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# # driver = webdriver.Chrome(executable_path="C:\\Users\\Emp ID - 1481\\PycharmProjects\\python_selenium\\drivers\\chromedriver.exe")
# # driver.get('https://www.facebook.com/')
# #
# # #tag and id(''syntax:- tagname#valueOfId'') ex:-input#email
# #
# # # driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("nikhil vamsi")
# # #driver.find_element(By.CSS_SELECTOR,"#email").send_keys("nikhil vamsi")
# # # tag name is optional
# #
# # #tag and class (''syntax:- tagname.valueOfClass'') ex:-
# #
# # # driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("nikhil@gmail.com")
# # #driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys("nikhil@gmail.com")
# # # tag name is optional
# #
# # #tag and attribute (''syntax:- tagname[attribute=value] )
# #
# # # driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").send_keys("nikhil@gmail.com")
# # # driver.find_element(By.CSS_SELECTOR,"[data-testid=royal_email]").send_keys("nikhil@gmail.com")
# # # tag name is optional
# #
# # #class and attribute
# #
# # driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_pass]").send_keys("123456")
#
#
#

# import pytest
# import math
#
# def test_sqrt():
#    num = 25
#    assert math.sqrt(num) == 5
#
# def testsquare():
#    assert 7*7 == 49
#
# def testquality():
#    assert 10 == 10
#
# def testnikki():
#    print("nikhil")
#
# def test_login():
#    assert "admin" == "admin"