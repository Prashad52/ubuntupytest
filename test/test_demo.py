from selenium.webdriver.firefox.webdriver import WebDriver

import time


class TestDemo():

    driver: WebDriver

    def setup_method(self):
        self.driver.get("https://www.google.com")
        self.driver.set_window_size(1440, 813) 

    def test_demo(self):
        time.sleep(10)

    def teardown_method(self):
        self.driver.quit()
