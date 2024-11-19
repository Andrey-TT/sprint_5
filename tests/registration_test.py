from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver, new_user
from locators import TestLocators
from urls import main_page, register_page

class TestRegistration:
    def test_registration(self, driver, new_user): # Тест регистрации
        driver.get(main_page)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.ENTER_ACCOUNT_BUTTON)))
        driver.find_element(By.XPATH, TestLocators.ENTER_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.REGISTER_TEXT_BUTTON)))
        driver.find_element(By.XPATH, TestLocators.REGISTER_TEXT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.INPUT_NAME)))
        driver.find_element(By.XPATH, TestLocators.INPUT_NAME).send_keys(new_user['name'])
        driver.find_element(By.XPATH, TestLocators.INPUT_EMAIL).send_keys(new_user['email'])
        driver.find_element(By.XPATH, TestLocators.INPUT_PASS).send_keys(new_user['password'])
        driver.find_element(By.XPATH, TestLocators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.ENTER_BUTTON)))
        driver.find_element(By.XPATH, TestLocators.INPUT_EMAIL).send_keys(new_user['email'])
        driver.find_element(By.XPATH, TestLocators.INPUT_PASS).send_keys(new_user['password'])
        driver.find_element(By.XPATH, TestLocators.ENTER_BUTTON).click()
        assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.PLACE_ORDER_BUTTON))) and driver.current_url == main_page

    def test_error_incorrect_password(self, driver, new_user): # Тест ошибки при некорректном пароле
        driver.get(register_page)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.INPUT_NAME)))
        driver.find_element(By.XPATH, TestLocators.INPUT_NAME).send_keys(new_user['name'])
        driver.find_element(By.XPATH, TestLocators.INPUT_EMAIL).send_keys(new_user['email'])
        driver.find_element(By.XPATH, TestLocators.INPUT_PASS).send_keys(new_user['f_password'])
        driver.find_element(By.XPATH, TestLocators.REGISTER_BUTTON).click()
        assert driver.find_element(By.XPATH, TestLocators.ERROR_PASS).is_displayed() and driver.current_url == register_page