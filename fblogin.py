from selenium import webdriver
import getpass
import time


usr = input("Enter the user-id: ")
pswd = input("Enter the Password: ")


driver = webdriver.Firefox(executable_path="/home/spanidea/Downloads/geckodriver-v0.24.0-linux32/geckodriver")
driver.get("https://en-gb.facebook.com/login/")
print("Facebook login page opened")
time.sleep(3)

user_button=driver.find_element_by_name("email")
user_button.send_keys(usr)
print("user-id entered.")
time.sleep(2)

password_button=driver.find_element_by_name("pass")
password_button.send_keys(pswd)
print("password entered.")
time.sleep(2)

loin_button=driver.find_element_by_name("login")
loin_button.click()
print("Facebook oepened")

time.sleep(5)

driver.quit()





