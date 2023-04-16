from selenium import webdriver
from selenium.webdriver.common.by import By
def test_lambdatest_todo_app():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.wikipedia.org/")
    ahmed = driver.find_element(By.ID, "searchInput")

    ahmed.send_keys("Hello World")
    ahmed.submit()
    print(driver.find_element("id", "firstHeading").text)
    print(driver.find_element(By.XPATH, '//*[@id="firstHeading"]/span').text + "hamada")

    assert driver.title == "\"Hello, World!\" program - Wikipedia"

