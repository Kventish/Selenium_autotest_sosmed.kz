import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from config import browser

def stock():
    element_to_hover_over_Check_Up = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[3]/div/ul/li[2]/div")
    hover = ActionChains(browser).move_to_element(element_to_hover_over_Check_Up)
    hover.perform()

    time.sleep(1)
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[3]/div/ul/li[2]/ul/li[1]/a").click()
    time.sleep(0.5)
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/ul/li/div/a").click()
    time.sleep(0.5)
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/a").click()
    time.sleep(0.5)
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/ul/li/div/a").click()
    time.sleep(1)
    element_to_hover_over_Check_Up = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/div[2]/div/button")
    hover = ActionChains(browser).move_to_element(element_to_hover_over_Check_Up)
    hover.perform()
    time.sleep(1)
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/div[2]/div/button").click()
    time.sleep(0.5)
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/div[2]/div/button").click()
    print("stock done")

def programm():
    element_to_hover_over_Check_Up = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[3]/div/ul/li[2]/div")
    hover = ActionChains(browser).move_to_element(element_to_hover_over_Check_Up)
    hover.perform()
    time.sleep(0.5)
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[3]/div/ul/li[2]/ul/li[2]/a").click()
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/ul/li[1]/div/a").click()
    time.sleep(0.5)
    element = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/div[2]/div/button")
    browser.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(0.5)
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/div[2]/div/button").click()
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/div[2]/div/button").click()
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/a").click()
    time.sleep(1)
    print("programm done")