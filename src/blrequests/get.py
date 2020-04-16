# -*- coding: utf-8 -*-
""" encapsulates functions to scrape live data from myrequests.bl.uk
"""
from blrequests import authentication
from blrequests.data_definitions import Credentials
from bs4 import BeautifulSoup
from bs4 import Tag
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


MYREQUESTS_LOGIN_URL = "https://myrequests.bl.uk/"
MYREQUESTS_USERNAME_FIELD_ID = "ctl00_PageDetails_uiUsername"
MYREQUESTS_PASSWORD_FIELD_ID = "ctl00_PageDetails_uiPassword"
MYREQUESTS_LOGIN_BUTTON = "ctl00_PageDetails_uiLogin"
FIREFOX_DRIVER_OPTIONS = ["-headless"]
CREDENTIALS = authentication.fetch_credentials()


def get_soup_of_requests_table(credentials: Credentials) -> Tag:
    """Consumes a Credentials and produces the soup of the requests
table belonging to the corresponding BL user.

    """
    myrequests_soup = get_myrequests_soup(credentials)
    return myrequests_soup_get_requests_table(myrequests_soup)


def get_myrequests_soup(credentials: Credentials) -> Tag:
    """Consumes a Credentials and produces the soup of the requests page
belonging to the corresponding BL user.

    """
    driver = initialize_firefox_driver()
    myrequests_html = driver_get_myrequests_html(driver, credentials)
    return BeautifulSoup(myrequests_html, "html.parser")


def initialize_firefox_driver() -> webdriver:
    """Returns an initialized selenium firefox webdriver.

    """
    options = Options()
    for option in FIREFOX_DRIVER_OPTIONS:
        options.add_argument(option)
    return webdriver.Firefox(firefox_options=options)


def driver_get_myrequests_html(driver: webdriver, credentials: Credentials) -> str:
    """Consumes a Credentials and a selenium webdriver and produces the
    raw html of the requests page of the corresponding BL user.

    """
    driver.get(MYREQUESTS_LOGIN_URL)
    return driver_do_login(driver, credentials).page_source


def driver_do_login(driver: webdriver, credentials: Credentials) -> webdriver:
    """Consumes a selenium WebDriver pointed at the login page and a
Credentials and logs into the british library's MyRequests
service. Produces the consequent WebDriver.

    """
    user_field = driver.find_element_by_id(MYREQUESTS_USERNAME_FIELD_ID)
    pw_field = driver.find_element_by_id(MYREQUESTS_PASSWORD_FIELD_ID)
    login_button = driver.find_element_by_id(MYREQUESTS_LOGIN_BUTTON)
    username, password = credentials[0], credentials[1]
    user_field.send_keys(username)
    pw_field.send_keys(password)
    login_button.click()
    return driver
