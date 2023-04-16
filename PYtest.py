# Implementation of Selenium test automation for this Selenium Python Tutorial
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
from time import sleep

def test_lambdatest_todo_app():
    chrome_driver = webdriver.Chrome()

    chrome_driver.get('https://lambdatest.github.io/sample-todo-app/')
    chrome_driver.maximize_window()

    chrome_driver.find_element(By.NAME,"li1").click()
    chrome_driver.find_element(By.NAME,"li2").click()

    title = "Sample page - lambdatest.com"
    assert title == chrome_driver.title

    sample_text = "Happy Testing at LambdaTest"
    email_text_field = chrome_driver.find_element(By.ID,"sampletodotext")
    email_text_field.send_keys(sample_text)
    sleep(1)

    chrome_driver.find_element(By.ID,"addbutton").click()
    sleep(1)

    output_str = chrome_driver.find_element(By.NAME,"li6").text
    sys.stderr.write(output_str + "  ahmed")

    sleep(2)
    chrome_driver.close()