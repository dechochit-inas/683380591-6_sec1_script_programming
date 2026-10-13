
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class DriverManager:
    def __init__(self, browser_name="chrome", headless=True):
        self.browser_name = browser_name.lower()
        self.headless = headless
        self.driver = None

    def get_driver(self):
        if self.driver:
            return self.driver

        if self.browser_name == "chrome":
            options = webdriver.ChromeOptions()

            if self.headless:
                options.add_argument("--headless")

            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--log-level=3")

            try:
                service = ChromeService(ChromeDriverManager().install())
                self.driver = webdriver.Chrome(
                    service=service,
                    options=options
                )
            except Exception as e:
                print(f"Error setting up Chrome driver: {e}")
                return None

        elif self.browser_name == "firefox":
            options = webdriver.FirefoxOptions()

            if self.headless:
                options.add_argument("--headless")

            try:
                service = FirefoxService(GeckoDriverManager().install())
                self.driver = webdriver.Firefox(
                    service=service,
                    options=options
                )
            except Exception as e:
                print(f"Error setting up Firefox driver: {e}")
                return None

        else:
            raise ValueError(
                f"Unsupported browser: {self.browser_name}"
            )

        self.driver.implicitly_wait(10)
        return self.driver

    def quit_driver(self):
        if self.driver:
            self.driver.quit()
            self.driver = None
            print("WebDriver quit successfully.")
