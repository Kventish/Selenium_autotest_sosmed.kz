from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.maximize_window()
browser.get('https://sosmed.kz/ru/')
