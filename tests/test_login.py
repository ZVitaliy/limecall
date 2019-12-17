from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from random import randint
import pytest
import time
import os


driverlocation = "/usr/bin/chromedriver"
os.environ["webdriver.chromedriver.driver"] = driverlocation
driver = webdriver.Chrome()

base_url = "https://qa.limecall.com/"
tab_url = "https://limecall.com/pricing/"
usr_login = "purpleraintest@gmail.com"
usr_pass = "Q!w2e3r4"


driver.get(base_url)
driver.maximize_window()


def test_user_login():
    login_field = driver.find_element(By.ID, 'login-username')
    login_field.send_keys(usr_login)
    pass_field = driver.find_element(By.ID, 'login-password')
    pass_field.send_keys(usr_pass)
    sign_in_btn = driver.find_element(By.XPATH,
    '//button[@class="btn btn-rounded btn-hero-success btn-block custom-btn-color"]')
    sign_in_btn.click()
    driver.implicitly_wait(2)
    page_title = driver.find_element(By.ID, 'pageTitle')
    assert page_title.is_displayed() == True

def test_team_create():
    users_menu = driver.find_element(By.XPATH, "//i[@class='fa fa-user']")
    users_menu.click()
    team_tab = driver.find_element(By.XPATH, "//div[@class='nav nav-md']//a[2]")
    team_tab.click()
    create_team_btn = driver.find_element(By.XPATH,
        "//a[@class='btn btn-fw primary']")
    create_team_btn.click()
    name_field = driver.find_element(By.ID, "name-input")
    team_name = "Team " + str(randint(0, 10))
    name_field.send_keys(team_name)
    save_btn = driver.find_element(By.XPATH, "//button[@class='btn primary']")
    save_btn.click()
    success_alert = driver.find_element(By.XPATH,
        "//div[@class='alert alert-success']")
    team_table = driver.find_element(By.XPATH,
        "//td[contains(text(),'" + team_name + "')]")
    assert team_table.is_displayed()
