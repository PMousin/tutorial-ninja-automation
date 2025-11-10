import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup_and_teardown")
class TestRegister:
    def test_register_validation_from(self):
        self.driver.find_element(By.XPATH, "//a[@title='My Account']").click()
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()
        time.sleep(5)
        self.driver.find_element(By.ID, "input-firstname").send_keys("Pinjari")
        self.driver.find_element(By.ID, "input-lastname").send_keys("Mousin")
        unique_email = f"pinjari{int(time.time())}@gmail.com"
        self.driver.find_element(By.ID, "input-email").send_keys(unique_email)

        self.driver.find_element(By.ID, "input-telephone").send_keys("9876543210")
        self.driver.find_element(By.ID, "input-password").send_keys("password123")
        self.driver.find_element(By.ID, "input-confirm").send_keys("password123")
        self.driver.find_element(By.NAME, "agree").click()
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        wait = WebDriverWait(self.driver, 10)
        success_msg = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//h1[normalize-space()='Your Account Has Been Created!']")))
        assert success_msg.text == "Your Account Has Been Created!"
        print("\n✅ Registration successful with email:", unique_email)
