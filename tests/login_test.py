from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from locators import TestLocators
from urls import main_page, register_page, recovery_pass_page
from data import my_email, my_password

class TestLogin:
    def test_authorization_on_main_page(self, driver): # Тест вход по кнопке «Войти в аккаунт» на главной
        driver.get(main_page)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.ENTER_ACCOUNT_BUTTON)))
        driver.find_element(By.XPATH, TestLocators.ENTER_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.INPUT_EMAIL)))
        driver.find_element(By.XPATH, TestLocators.INPUT_EMAIL).send_keys(my_email)
        driver.find_element(By.XPATH, TestLocators.INPUT_PASS).send_keys(my_password)
        driver.find_element(By.XPATH, TestLocators.ENTER_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.PLACE_ORDER_BUTTON)))
        assert driver.current_url == main_page and driver.find_element(By.XPATH, TestLocators.PLACE_ORDER_BUTTON).text == 'Оформить заказ'

    def test_authorization_personal_account_button(self, driver): # Тест вход через кнопку «Личный кабинет»
        driver.get(main_page)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.PERSONAL_ACCOUNT_BUTTON)))
        driver.find_element(By.XPATH, TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.INPUT_EMAIL)))
        driver.find_element(By.XPATH, TestLocators.INPUT_EMAIL).send_keys(my_email)
        driver.find_element(By.XPATH, TestLocators.INPUT_PASS).send_keys(my_password)
        driver.find_element(By.XPATH, TestLocators.ENTER_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.PLACE_ORDER_BUTTON)))
        assert driver.current_url == main_page and driver.find_element(By.XPATH, TestLocators.PLACE_ORDER_BUTTON).text == 'Оформить заказ'

    def test_authorization_button_in_registration_form(self, driver): # Тест вход через кнопку в форме регистрации
        driver.get(register_page)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.ENTER_TEXT_BUTTON)))
        driver.find_element(By.XPATH, TestLocators.ENTER_TEXT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.INPUT_EMAIL)))
        driver.find_element(By.XPATH, TestLocators.INPUT_EMAIL).send_keys(my_email)
        driver.find_element(By.XPATH, TestLocators.INPUT_PASS).send_keys(my_password)
        driver.find_element(By.XPATH, TestLocators.ENTER_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.PLACE_ORDER_BUTTON)))
        assert driver.current_url == main_page and driver.find_element(By.XPATH, TestLocators.PLACE_ORDER_BUTTON).text == 'Оформить заказ'

    def test_authorization_button_in_password_recovery(self, driver): # Тест вход через кнопку в форме восстановления пароля
        driver.get(recovery_pass_page)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.ENTER_TEXT_BUTTON)))
        driver.find_element(By.XPATH, TestLocators.ENTER_TEXT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.INPUT_EMAIL)))
        driver.find_element(By.XPATH, TestLocators.INPUT_EMAIL).send_keys(my_email)
        driver.find_element(By.XPATH, TestLocators.INPUT_PASS).send_keys(my_password)
        driver.find_element(By.XPATH, TestLocators.ENTER_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.PLACE_ORDER_BUTTON)))
        assert driver.current_url == main_page and driver.find_element(By.XPATH, TestLocators.PLACE_ORDER_BUTTON).text == 'Оформить заказ'