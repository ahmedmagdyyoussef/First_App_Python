#this app return links from the pages ;)
from selenium import webdriver
from selenium.webdriver.common.by import By
def test_ReturnURLS():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.youtube.com/")
    elems = driver.find_elements(By.XPATH,"//a")
    #elems = driver.find_elements(By.TAG_NAME,"a")

    for elem in elems:
       # print(elem.get_attribute("href"))
        print(elem.get_attribute("title"))

    driver.close()