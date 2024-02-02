from selenium import webdriver
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os

env = os.getenv('APP_ENV', 'local')

print("Starting the browser...")
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox') 
options.add_argument('--disable-dev-shm-usage') 

print("Enabling headless mode...")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
print("Browser is ready to use!")
browser = webdriver.Remote("http://selenium:4444/wd/hub",  DesiredCapabilities.CHROME, options=options) if env == 'CI' else webdriver.Chrome(options=options)
print("Ready to go! Wait 10 seconds...")
browser.implicitly_wait(10)
print("Maximizing the browser...")
browser.maximize_window()
print("Opening the page...")
time.sleep(3)
browser.get('https://sosmed.kz/ru/')
time.sleep(3)
print("Page is opened!")