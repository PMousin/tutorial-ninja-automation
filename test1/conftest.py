import pytest
from selenium import webdriver

@pytest.fixture()
def setup_and_teardown(request):
    # Setup: Initialize WebDriver
    driver = webdriver.Chrome()  # or Firefox, Edge, etc.
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    request.cls.driver = driver
    yield
    driver.quit()
