import time
from selenium.webdriver.common.by import By
from config import browser

def button_check():
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[3]/div/div[2]/a[2]/button").click()
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/div[2]/div[2]/div[1]/a").click()
    time.sleep(1)
    browser.execute_script("window.history.go(-1)")
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/div[2]/div[2]/div[2]/a").click()
    time.sleep(1)
    browser.execute_script("window.history.go(-1)")
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/div[2]/div[2]/div[3]/a").click()
    time.sleep(1)
    print("Mc_Dostyk done")