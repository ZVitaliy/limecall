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
usr_login = "zakharkin@purple-rain.io"
usr_pass = "Q!w2e3r4"


driver.get(base_url)
driver.maximize_window()


def test_team_create():
    users_menu = driver.find_element(By.CLASS_NAME, "fa fa-user")
    users_menu.click()
    team_tab = driver.find_element(By.XPATH, "//div[@class='nav nav-md']//a[2]")
    team_tab.click()
    create_team_btn = driver.find_element(By.CLASS_NAME, "btn btn-fw primary")
    create_team_btn.click()
    name_field = driver.find_element(By.ID, "name-input")
    team_name = str("Team " + randint(0, 10))
    name_field.send_keys(team_name)
    save_btn = driver.find_element(By.CLASS_NAME, "btn primary")
    save_btn.click()
    success_alert = driver.find_element(By.CLASS_NAME, "alert alert-success")
    team_table = driver.find_element(By.XPATH,
        "//td[contains(text(),'" + Team + "')]")
    assert success_alert.is_displayed() and team_table.is_displayed == True
