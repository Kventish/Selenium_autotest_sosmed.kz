import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from config import browser
from selenium.webdriver.common.keys import Keys

def docktors_main():
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[3]/div/ul/li[3]/a").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[1]/div/div[1]/input").send_keys('Муратбаева Роза Ильясовна')
    time.sleep(0.5)
    element_to_hover_over_Check_Up = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[1]/div/div[2]/div/div/div/div/div")
    hover = ActionChains(browser).move_to_element(element_to_hover_over_Check_Up)
    hover.perform()
    time.sleep(1)

    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[1]/div/div[2]/div/div/div/div/div/div/a").click()
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[3]/div/ul/li[3]/a").click()
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[1]/div/div[1]/div[2]").click()
    time.sleep(1)
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[1]/div/div[1]/div[2]/p[1]").click()
    time.sleep(1)
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[1]/div/div[1]/div[2]/div/img[1]").click()
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[1]/div/div[1]/div[3]/input").send_keys('Терапевт')
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[1]/div/div[1]/div[3]/ul/li[1]/div/label").click()
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[1]/div/div[1]/div[3]/input").send_keys(Keys.SHIFT + Keys.HOME + Keys.DELETE)
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[1]/div/div[1]/div[3]/ul/li[1]/div/label").click()
    time.sleep(1)
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[1]/div/div[1]/ul[2]/li[2]/label").click()
    time.sleep(1)
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[1]/div/div[1]/ul[2]/li[2]/label").click()
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[1]/div/div[2]/button").click()
    time.sleep(2)
    print("docktors_main done")

def doctor_page():
    element = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[1]/div/div[2]/div/div/div[1]/div/div")
    browser.execute_script("arguments[0].scrollIntoView(true);", element)

    element_to_hover_over_Check_Up = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[1]/div/div[2]/div/div/div[1]/div/div")
    hover = ActionChains(browser).move_to_element(element_to_hover_over_Check_Up)
    hover.perform()
    time.sleep(1)

    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[1]/div/div[2]/div/div/div[1]/div/div/div/a").click()
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/div[1]/div[4]/div/div[2]/button/span[2]").click()
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/div[1]/div[4]/div/div[1]/button[1]").click()
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/div[1]/div[4]/div/div[2]/button").click()
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/div[1]/div[4]/div/div[2]/button/span[2]").click()
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/div[1]/div[4]/div/div[1]/button[2]").click()

    time.sleep(1)
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[4]/div/div[1]/div").click()
    print("doctor_page done")
