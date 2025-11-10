import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_and_teardown")
class Testlogin:
    def test_login_with_valid_credentials(self):
        self.driver.find_element(By.XPATH, "//a[@title='My Account']").click()
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
        time.sleep(5)
        self.driver.find_element(By.NAME, "email").send_keys("amotooricap9@gmail.com")
        self.driver.find_element(By.ID, "input-password").send_keys("12345")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        actual_text = self.driver.find_element(By.CSS_SELECTOR, "div.alert.alert-danger").text
        expected_text = "Warning: No match for E-Mail Address and/or Password."
        assert expected_text in actual_text

