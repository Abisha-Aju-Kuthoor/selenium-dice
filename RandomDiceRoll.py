from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest

driver= webdriver.Chrome()
driver.get("https://www.google.com/")

assert "google",driver.title

time.sleep(3)
searchbar = driver.find_element(By.NAME,"q")
searchbar.click
searchbar.send_keys("random number")
searchbar.send_keys(Keys.ENTER)

min = driver.find_element(By.ID,"UMy8j").clear()
time.sleep(2)
min= driver.find_element(By.ID,"UMy8j")
min.send_keys("1")

max = driver.find_element(By.ID,"nU5Yvb").clear()
time.sleep(2)
max= driver.find_element(By.ID,"nU5Yvb")
max.send_keys("6")
generate = driver.find_element(By.ID,"vMxoHf")
generate.click()
assert "No results" not in driver.page_source
time.sleep(7)
res = driver.find_element(By.CLASS_NAME,"gws-csf-randomnumber__result")
print(res.text)
driver.quit()


