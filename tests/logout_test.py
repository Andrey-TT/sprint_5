from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from locators import TestLocators
from urls import authorization_page
from data import my_email, my_password

class TestLogout:
    def test_clicking_exit_button_in_personal_account(self, driver): # Тест выхода по кнопке «Выйти» в личном кабинете
        driver.get(authorization_page)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.INPUT_EMAIL)))
        driver.find_element(By.XPATH, TestLocators.INPUT_EMAIL).send_keys(my_email)
        driver.find_element(By.XPATH, TestLocators.INPUT_PASS).send_keys(my_password)
        driver.find_element(By.XPATH, TestLocators.ENTER_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.PERSONAL_ACCOUNT_BUTTON)))
        driver.find_element(By.XPATH, TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.EXIT_TEXT_BUTTON)))
        driver.find_element(By.XPATH, TestLocators.EXIT_TEXT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.ENTER_BUTTON)))
        assert driver.current_url == authorization_page and driver.find_element(By.XPATH, TestLocators.ENTER_BUTTON).text == 'Войти'

