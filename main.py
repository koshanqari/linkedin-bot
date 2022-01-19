from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
import os
driver = webdriver.Chrome(executable_path="c:\chromedriver\chromedriver.exe")

driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&f_E=1&f_WT=2&geoId=92000000&keywords=marketing%20intern&location=Worldwide")


signin = driver.find_element_by_css_selector("body div.base-serp-page header nav div a.nav__button-secondary")
signin.click()

name = driver.find_element_by_name("session_key")
name.send_keys("koshanqari@hotmail.com")

password = driver.find_element_by_name("session_password")
password.send_keys(os.environ.get("PASSWORD"))
password.send_keys(Keys.ENTER)

 #asynchonization

jobs = driver.find_elements_by_css_selector(".jobs-search-results__list-item.occludable-update.p0.relative.ember-view")

for job in jobs:
    try:
        job.click()
        time.sleep(1)
        apply_button = driver.find_element_by_css_selector("button.jobs-apply-button.artdeco-button.artdeco-button--3.artdeco-button--primary.ember-view")
        apply_button.click()

        box = driver.find_element_by_css_selector("input.ember-text-field.ember-view.fb-single-line-text__input")
        box.send_keys("9596113966")

        time.sleep(3)
        driver.find_element_by_css_selector("svg.mercado-match path").click() #cross
        driver.find_element_by_css_selector("button.artdeco-modal__confirm-dialog-btn.artdeco-button.artdeco-button--2.artdeco-button--secondary.ember-view").click() #discard
    
    except NoSuchElementException:
        print("Some Error, job skipped")


