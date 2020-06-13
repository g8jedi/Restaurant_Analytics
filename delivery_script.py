#!/usr/bin/env python3
import datetime
from time import sleep
from os import getcwd

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from local_settings import EMAIL, PASSWORD, DRIVER_PATH, DELMAR


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
driver.find_element_by_link_text(DELMAR.name).click()
sleep(1)
driver.get("https://www.toasttab.com/restaurants/admin/reports/home#sales-orders")
sleep(2)
date_dropdown = driver.find_element_by_id("date-dropdown-container")
date_dropdown.click()
custom_button = date_dropdown.find_element_by_link_text("Custom Date")
custom_button.click()

today = datetime.datetime.today()
restaurant_first_day = DELMAR.first_day
limit_end_date = DELMAR.first_day + datetime.timedelta(days=770)

report_date_start = driver.find_element_by_name("reportDateStart")
driver.execute_script("arguments[0].value = ''", report_date_start)
report_date_start.send_keys(DELMAR.first_day.strftime("%m-%d-%Y"))
report_date_start.send_keys(Keys.RETURN)
sleep(1)
report_date_end = driver.find_element_by_name("reportDateEnd")
driver.execute_script("arguments[0].value = ''", report_date_end)
report_date_end.send_keys(limit_end_date.strftime("%m-%d-%Y"))
report_date_end.send_keys(Keys.RETURN)
driver.find_element_by_id("more-dropdown-container").click()
driver.find_element_by_link_text("Dining Option").click()
driver.find_element_by_id("report-restaurants").click()
sleep(1)
driver.find_element_by_id("dining-option-option").click()
sleep(1)
driver.find_element_by_link_text("Deliver (Sushi Madre)").click()
sleep(2)
driver.find_element_by_id("update-btn").click()
sleep(10)
