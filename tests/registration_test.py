from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from locators import TestLocators
from urls import main_page, register_page
from helpers import new_name, new_email, new_password, fail_password

class TestRegistration:
    def test_registration(self, driver): # Тест регистрации
        driver.get(main_page)
        name = new_name
        email = new_email
        password = new_password
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.ENTER_ACCOUNT_BUTTON)))
        driver.find_element(By.XPATH, TestLocators.ENTER_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.REGISTER_TEXT_BUTTON)))
        driver.find_element(By.XPATH, TestLocators.REGISTER_TEXT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.INPUT_NAME)))
        driver.find_element(By.XPATH, TestLocators.INPUT_NAME).send_keys(name)
        driver.find_element(By.XPATH, TestLocators.INPUT_EMAIL).send_keys(email)
        driver.find_element(By.XPATH, TestLocators.INPUT_PASS).send_keys(password)
        driver.find_element(By.XPATH, TestLocators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.ENTER_BUTTON)))
        driver.find_element(By.XPATH, TestLocators.INPUT_EMAIL).send_keys(email)
        driver.find_element(By.XPATH, TestLocators.INPUT_PASS).send_keys(password)
        driver.find_element(By.XPATH, TestLocators.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.PLACE_ORDER_BUTTON)))
        assert driver.current_url == main_page and driver.find_element(By.XPATH, TestLocators.PLACE_ORDER_BUTTON).text == 'Оформить заказ'

    def test_error_incorrect_password(self, driver): # Тест ошибки при некорректном пароле
        driver.get(register_page)
        name = new_name
        email = new_email
        password = fail_password
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.INPUT_NAME)))
        driver.find_element(By.XPATH, TestLocators.INPUT_NAME).send_keys(name)
        driver.find_element(By.XPATH, TestLocators.INPUT_EMAIL).send_keys(email)
        driver.find_element(By.XPATH, TestLocators.INPUT_PASS).send_keys(password)
        driver.find_element(By.XPATH, TestLocators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.ERROR_PASS)))
        assert driver.find_element(By.XPATH, TestLocators.ERROR_PASS).text == 'Некорректный пароль' and driver.current_url == register_page