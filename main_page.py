import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from config import browser

def header():


    element_to_hover_over_service = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[3]/div/ul/li[1]/div")
    hover = ActionChains(browser).move_to_element(element_to_hover_over_service)
    hover.perform()

    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[3]/div/ul/li[1]/ul/li[1]/a").click()
    # time.sleep(1)
    hover.perform()
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[3]/div/ul/li[1]/ul/li[2]/a").click()
    # time.sleep(1)

    element_to_hover_over_Check_Up = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[3]/div/ul/li[2]/div")
    hover = ActionChains(browser).move_to_element(element_to_hover_over_Check_Up)
    hover.perform()
    # time.sleep(1)

    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[3]/div/ul/li[2]/ul/li[1]/a").click()
    # time.sleep(1)
    hover.perform()
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[3]/div/ul/li[2]/ul/li[2]/a").click()
    # time.sleep(1)

    element_to_hover_over_Doc = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[3]/div/ul/li[3]/a")
    hover = ActionChains(browser).move_to_element(element_to_hover_over_Doc)
    hover.perform()

    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[3]/div/ul/li[3]/a").click()
    # time.sleep(1)

    element_to_hover_over_info = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[3]/div/ul/li[4]/div")
    hover = ActionChains(browser).move_to_element(element_to_hover_over_info)
    hover.perform()
    # time.sleep(1)

    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[3]/div/ul/li[4]/ul/li[1]/a").click()
    # time.sleep(1)
    hover.perform()
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[3]/div/ul/li[4]/ul/li[2]/a").click()
    # time.sleep(1)
    hover.perform()
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[3]/div/ul/li[4]/ul/li[3]/a").click()
    # time.sleep(1)
    hover.perform()
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[3]/div/ul/li[4]/ul/li[4]/a").click()
    # time.sleep(1)

    element_to_hover_over_pricelist = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[3]/div/ul/li[5]/a")
    hover = ActionChains(browser).move_to_element(element_to_hover_over_pricelist)
    hover.perform()
    # time.sleep(1)

    element_to_hover_over_cart = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[3]/div/div[2]/div[1]/div[1]")
    hover = ActionChains(browser).move_to_element(element_to_hover_over_cart)
    hover.perform()
    # time.sleep(1)

    element_to_hover_over_language = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[3]/div/div[2]/div[2]/div[1]")
    hover = ActionChains(browser).move_to_element(element_to_hover_over_language)
    hover.perform()
    # time.sleep(1)

    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[3]/div/div[2]/div[2]/div[2]/div/span[3]").click()
    time.sleep(1)
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[3]/div/div[2]/div[2]/div[2]/div/span[2]").click()

    element_to_hover_over_medT = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[3]/div/div[2]/a[1]/button/div")
    hover = ActionChains(browser).move_to_element(element_to_hover_over_medT)
    hover.perform()
    # time.sleep(1)

    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[3]/div/div[2]/a[1]/button/div").click()
    time.sleep(1)

    element_to_hover_over_medD = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[3]/div/div[2]/a[2]/button/div")
    hover = ActionChains(browser).move_to_element(element_to_hover_over_medD)
    hover.perform()
    


def body():
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/header/div[3]/div/a[1]").click()
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/section[1]/div[1]/div[1]/a/span").click()
    browser.execute_script("window.history.go(-1)")
    time.sleep(2)
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/section[1]/div[1]/div[3]/ul/li[2]").click()
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/section[1]/div[1]/div[1]/a/span").click()
    browser.execute_script("window.history.go(-1)")
    time.sleep(2)
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/section[1]/div[1]/div[3]/ul/li[3]").click()
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/section[1]/div[1]/div[1]/a/span").click()
    browser.execute_script("window.history.go(-1)")
    time.sleep(2)
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/section[1]/div[1]/div[3]/ul/li[4]").click()
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/section[1]/div[1]/div[1]/a/span").click()
    browser.execute_script("window.history.go(-1)")
    time.sleep(2)

    element = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/section[2]/div[1]")
    browser.execute_script("arguments[0].scrollIntoView(true);", element)


    element_to_hover_over_doc1 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/section[2]/div[1]/div/div/div[1]")
    hover = ActionChains(browser).move_to_element(element_to_hover_over_doc1)
    hover.perform()

    time.sleep(1)

    element_to_hover_over_doc2 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/section[2]/div[1]/div/div/div[2]")
    hover = ActionChains(browser).move_to_element(element_to_hover_over_doc2)
    hover.perform()

    time.sleep(1)

    element_to_hover_over_doc3 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/section[2]/div[1]/div/div/div[3]")
    hover = ActionChains(browser).move_to_element(element_to_hover_over_doc3)
    hover.perform()

    time.sleep(1)

    element_to_hover_over_doc4 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/section[2]/div[1]/div/div/div[4]")
    hover = ActionChains(browser).move_to_element(element_to_hover_over_doc4)
    hover.perform()

    time.sleep(1)

    element_to_hover_over_doc5 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/section[2]/div[1]/div/div/div[5]")
    hover = ActionChains(browser).move_to_element(element_to_hover_over_doc5)
    hover.perform()

    time.sleep(1)

    element_to_hover_over_doc6 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/section[2]/div[1]/div/div/div[6]")
    hover = ActionChains(browser).move_to_element(element_to_hover_over_doc6)
    hover.perform()
    time.sleep(1)

    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/section[2]/div[1]/div/div/div[6]/div/div/div/a").click()
    time.sleep(1)
    browser.execute_script("window.history.go(-1)")
    time.sleep(1)

    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/section[2]/div[1]/a").click()
    time.sleep(1)
    browser.execute_script("window.history.go(-1)")

    time.sleep(1)

    element = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/section[3]/div[1]")
    browser.execute_script("arguments[0].scrollIntoView(true);", element)

    element_to_hover_over_post1 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/section[3]/div[1]/div/article[1]")
    hover = ActionChains(browser).move_to_element(element_to_hover_over_post1)
    hover.perform()

    time.sleep(1)

    element_to_hover_over_post2 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/section[3]/div[1]/div/article[2]")
    hover = ActionChains(browser).move_to_element(element_to_hover_over_post2)
    hover.perform()

    time.sleep(1)

    element_to_hover_over_post3 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/section[3]/div[1]/div/article[3]")
    hover = ActionChains(browser).move_to_element(element_to_hover_over_post3)
    hover.perform()

    time.sleep(1)

    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/section[3]/div[1]/div/article[3]").click()
    time.sleep(0.5)
    browser.execute_script("window.history.go(-1)")

    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/section[3]/div[1]/div/article[1]/a/a/span").click()
    time.sleep(0.5)
    browser.execute_script("window.history.go(-1)")

    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/section[3]/div[1]/a").click()
    time.sleep(1)

    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[1]/div[1]/nav/ul/li[1]").click()
    time.sleep(0.5)

    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[1]/div[1]/nav/ul/li[2]").click()
    time.sleep(0.5)

    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div[1]/div[1]/nav/ul/li[3]").click()
    time.sleep(0.5)
    browser.execute_script("window.history.go(-1)")
    time.sleep(1)

    element = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/div")
    browser.execute_script("arguments[0].scrollIntoView(true);", element)

    element_to_hover_over_infohover1 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/div/div/div[1]/div[1]")
    hover = ActionChains(browser).move_to_element(element_to_hover_over_infohover1)
    hover.perform()

    time.sleep(0.5)

    element_to_hover_over_infohover2 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/div/div/div[1]/div[2]")
    hover = ActionChains(browser).move_to_element(element_to_hover_over_infohover2)
    hover.perform()

    time.sleep(0.5)

    element_to_hover_over_infohover3 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/div/div/div[1]/div[3]")
    hover = ActionChains(browser).move_to_element(element_to_hover_over_infohover3)
    hover.perform()

    time.sleep(0.5)

    element_to_hover_over_infohover4 = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/div/div/div[1]/div[4]")
    hover = ActionChains(browser).move_to_element(element_to_hover_over_infohover4)
    hover.perform()

    time.sleep(0.5)
def footer():

    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/footer/div/div[1]/div[6]/form/div[5]/div/div/span/button").click()
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/footer/div/div[1]/div[6]/form/div[1]/div/div/span/textarea").send_keys('test')
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/footer/div/div[1]/div[6]/form/div[2]/div/div/span/input").send_keys('test')
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/footer/div/div[1]/div[6]/form/div[3]/div/div/span/input").click()
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/footer/div/div[1]/div[6]/form/div[3]/div/div/span/input").send_keys('7777777777')
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div/footer/div/div[1]/div[6]/form/div[4]/div/div/span/input").send_keys('test@test.test')

    time.sleep(5)
    