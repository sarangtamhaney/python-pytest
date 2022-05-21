import pytest
from pages.GooglePage import GooglePage


@pytest.mark.usefixtures("test_setup")
class TestGoogle:

    def test_google(self):
        driver = self.driver
        google = GooglePage(driver)
        google.open("https://google.com")
        self.logger.info("Entering keyword in test 1")
        google.search("selenium")

    def test_google_french(self):
        driver = self.driver
        google = GooglePage(driver)
        google.open("https://google.fr")
        self.logger.info("Entering keyword in test 2")
        google.search("selenium")
        assert False, "Failed test"

