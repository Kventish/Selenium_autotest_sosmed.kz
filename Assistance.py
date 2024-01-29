import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from config import browser

def assistance():
    element_to_hover_over_service = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[3]/div/ul/li[1]/div")
    hover = ActionChains(browser).move_to_element(element_to_hover_over_service)
    hover.perform()

    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[3]/div/ul/li[1]/ul/li[2]/a").click()

    element = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[1]/ul/li[18]/button")
    browser.execute_script("arguments[0].scrollIntoView(true);", element)

    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[1]/ul/li[18]/button").click()
    browser.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div[2]/form/div[2]/div/div/span/input").send_keys('test')
    browser.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div[2]/form/div[3]/div/div/span/input").send_keys('77777777777')
    browser.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div[2]/form/div[4]/div/div/span/input").send_keys('test@test.test')
    browser.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div[2]/form/div[1]/div/div/span/textarea").send_keys('testtestetstestestetestettetetestetest')
    browser.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/button").click()