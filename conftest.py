import pytest
from selenium import webdriver
from helpers import new_name, new_email, new_password, fail_password

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture
def new_user():
    name = new_name
    email = new_email
    password = new_password
    f_password = fail_password
    return {'name':name, "email": email, "password": password, "f_password": f_password}