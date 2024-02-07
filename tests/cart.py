import time
from selenium.webdriver.common.by import By
from config import browser

def check_button():
    #Удаление + заполнение формы оплаты
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[3]/div/div[2]/div[1]/div[1]").click()
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[3]/div/div[2]/div[1]/div[2]/div/ul/li[3]/button").click()
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[3]/div/div[2]/div[1]/div[2]/div/div/button").click()
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/div/form/div[1]/div/div/span/input").send_keys('Смолевский Дмитрий')
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/div/form/div[2]/div/div/span/input").send_keys('test@test.test')
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/div/form/div[3]/div/div/span/input").send_keys('77777777777')
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/div/form/div[4]/div/div/span/textarea").send_keys('test<1.32,<(&%!!#)')
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/div/form/div[5]/div/div/span/div/label/span/input").click()
    #Переход на страницу оплаты
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[2]/div/form/div[8]/div/div/span/button").click()
    time.sleep(5)
    browser.execute_script("window.history.go(-1)")
    #Выход на главный экран
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[3]/div/a[1]").click()
    time.sleep(3)
    print("cart done")