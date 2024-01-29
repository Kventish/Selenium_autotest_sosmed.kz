import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from config import browser
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test():
    element_to_hover_over_service = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[3]/div/ul/li[1]/div")
    hover = ActionChains(browser).move_to_element(element_to_hover_over_service)
    hover.perform()

    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[3]/div/ul/li[1]/ul/li[1]/a").click()

    time.sleep(1)
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[1]/div/div[1]/div").click()
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[1]/div/div[1]/ul[1]/li[1]").click()
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[1]/div/div[1]/ul[2]/li[1]").click()
    time.sleep(1)
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[1]/div/div[3]/div[1]/div[2]/button").click()
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[4]/div/div[3]/div[1]/button[1]").click()
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[3]/div/div[2]/div[1]/div[2]/div/ul/li/button").click()
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[1]/div/div[3]/div[1]/div[2]/button").click()
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[4]/div/div[3]/div[1]/button[1]").click()
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[3]/div/div[2]/div[1]/div[2]/div/ul/li/button").click()
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[1]/div/div[3]/div[1]/div[2]/button").click()
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[4]/div/div[3]/div[1]/button[2]").click()
    time.sleep(1)
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[1]/div/div[1]/ul[2]/li[18]").click()
    time.sleep(1)