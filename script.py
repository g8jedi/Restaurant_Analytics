#!/usr/bin/env python3
import datetime
from time import sleep
from os import getcwd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from local_settings import EMAIL, PASSWORD, DRIVER_PATH, LOOP20


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
chrome_options.add_experimental_option("prefs", {"download.default_directory": getcwd()})
driver = webdriver.Chrome(options=chrome_options, executable_path=DRIVER_PATH)
driver.get('https://www.toasttab.com/login')
driver.find_element_by_id("email").send_keys(EMAIL)
driver.find_element_by_id("password").send_keys(PASSWORD)
sleep(2)
driver.find_element_by_id("log-in").click()
sleep(1)
driver.find_element_by_id("switch-restaurants-menu").click()
sleep(1)
driver.find_element_by_link_text(LOOP20.name).click()
sleep(1)
driver.get("https://www.toasttab.com/restaurants/admin/reports/home")
sleep(1)
driver.find_element_by_id("first-load-container").find_element_by_tag_name("button").click()
sleep(2)
date_dropdown = driver.find_element_by_id("date-dropdown-container")
date_dropdown.click()
custom_button = date_dropdown.find_element_by_link_text("Custom Date")
custom_button.click()

today = datetime.datetime.today()
days_delta = (today - LOOP20.first_day).days

for i in range(0, days_delta):
    report_date_start = driver.find_element_by_name("reportDateStart")
    driver.execute_script("arguments[0].value = ''", report_date_start)
    report_date_start.send_keys(LOOP20.first_day.strftime("%m-%d-%Y"))
    report_date_start.send_keys(Keys.RETURN)
    sleep(1)
    report_date_end = driver.find_element_by_name("reportDateEnd")
    driver.execute_script("arguments[0].value = ''", report_date_end)
    report_date_end.send_keys(LOOP20.first_day.strftime("%m-%d-%Y"))
    report_date_end.send_keys(Keys.RETURN)
    sleep(2)
    driver.find_element_by_id("report-restaurants").click()
    sleep(2)
    driver.find_element_by_id("update-btn").click()
    try:
        element = WebDriverWait(driver, 8).until(
            EC.presence_of_element_located((By.ID, "sales-summary-content"))
        )
    finally:
        summary_content = driver.find_element_by_id("sales-summary-content")
        export_button = summary_content.find_element_by_css_selector('div a')
        export_button.click()
        sleep(1)
        LOOP20.first_day += datetime.timedelta(days=1)
        print(i, LOOP20.first_day)
