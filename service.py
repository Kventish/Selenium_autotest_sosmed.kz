import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from config import browser

def test():
    element_to_hover_over_service = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[3]/div/ul/li[1]/div")
    hover = ActionChains(browser).move_to_element(element_to_hover_over_service)
    hover.perform()

    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[3]/div/ul/li[1]/ul/li[1]/a").click()

    time.sleep(4)
