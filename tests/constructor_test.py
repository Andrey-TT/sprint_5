from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from locators import TestLocators
from urls import main_page

class TestConstructor:
    def test_transitions_to_sections_buns(self, driver): # Тест перехода к разделу «Булки»
        driver.get(main_page)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.FILLINGS_TEXT_BUTTON)))
        driver.find_element(By.XPATH, TestLocators.FILLINGS_TEXT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.FILLINGS_TEXT)))
        assert 'tab_tab_type_current' in driver.find_element(By.XPATH, TestLocators.FILLINGS_TEXT_BUTTON + "/..").get_attribute('class')
        driver.find_element(By.XPATH, TestLocators.BUNS_TEXT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.BUNS_TEXT)))
        assert 'tab_tab_type_current' in driver.find_element(By.XPATH, TestLocators.BUNS_TEXT_BUTTON + "/..").get_attribute('class')

    def test_transitions_to_sections_sauces(self, driver): # Тест перехода к разделу «Соусы»
        driver.get(main_page)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.SAUCES_TEXT_BUTTON)))
        driver.find_element(By.XPATH, TestLocators.SAUCES_TEXT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.SAUCES_TEXT)))
        assert 'tab_tab_type_current' in driver.find_element(By.XPATH, TestLocators.SAUCES_TEXT_BUTTON + "/..").get_attribute('class')

    def test_transitions_to_sections_fillings(self, driver): # Тест перехода к разделу «Соусы»
        driver.get(main_page)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.FILLINGS_TEXT_BUTTON)))
        driver.find_element(By.XPATH, TestLocators.FILLINGS_TEXT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, TestLocators.FILLINGS_TEXT)))
        assert 'tab_tab_type_current' in driver.find_element(By.XPATH, TestLocators.FILLINGS_TEXT_BUTTON + "/..").get_attribute('class')