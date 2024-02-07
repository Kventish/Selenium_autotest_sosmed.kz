import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from config import browser
from selenium.webdriver.common.keys import Keys

def preyskurant():
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[3]/div/ul/li[5]/a").click()
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/div[2]/ul/li[1]/ul[1]/li/div/button").click()
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/div[2]/ul/li[1]/ul[2]/li/div/button").click()
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/button[1]").click()
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/div[2]/ul/li[2]/ul[10]/li/div/button").click()
    time.sleep(1)
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[4]/div/div[1]/div/img").click()
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/div[1]/input").send_keys('Общий анализ крови')
    time.sleep(1)
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/div[2]/ul/li/ul/li/div/button").click()
    time.sleep(1)
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[4]/div/div[1]/div/img").click()
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/div[1]/input").send_keys(Keys.SHIFT + Keys.HOME + Keys.DELETE)
    time.sleep(1)
    print("preyskurant done")