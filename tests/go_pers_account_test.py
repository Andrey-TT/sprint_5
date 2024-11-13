from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from locators import TestLocators
from urls import authorization_page, profile_page
from data import my_email, my_password

class TestGo_pers_account:
    def test_click_on_Personal_Account(self, driver): # Тест переход по клику на «Личный кабинет»
        driver.get(authorization_page)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.INPUT_EMAIL)))
        driver.find_element(By.XPATH, TestLocators.INPUT_EMAIL).send_keys(my_email)
        driver.find_element(By.XPATH, TestLocators.INPUT_PASS).send_keys(my_password)
        driver.find_element(By.XPATH, TestLocators.ENTER_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.PERSONAL_ACCOUNT_BUTTON)))
        driver.find_element(By.XPATH, TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.EXIT_TEXT_BUTTON)))
        assert driver.current_url == profile_page and driver.find_element(By.XPATH, TestLocators.SAVE_BUTTON).text == 'Сохранить'

