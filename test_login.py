from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
import os


driverlocation = "/usr/bin/chromedriver"
os.environ["webdriver.chromedriver.driver"] = driverlocation
driver = webdriver.Chrome()

base_url = 'https://qa.limecall.com/'
usr_login = 'zakharkin@purple-rain.io'
usr_pass = 'Q!w2e3r4'


driver.get(base_url)
driver.maximize_window()
print('Maximized')

class LoginUserTest:
    def test_user_login(self):
        login_field = driver.find_element(By.ID, 'login-username')
        print('Login field founded')
        login_field.send_keys(usr_login)
        pass_field = driver.find_element(By.ID, 'login-password')
        print('Password field founded')
        pass_field.send_keys(usr_pass)
        sign_in_btn = driver.find_element(By.XPATH,
        '//button[@class="btn btn-rounded btn-hero-success btn-block custom-btn-color"]')
        sign_in_btn.click()


login = LoginUserTest()
login.test_user_login()
