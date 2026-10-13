
import time
import logging

from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    StaleElementReferenceException
)

from .driver_manager import DriverManager
from .data_models import Product
from .utils import (
    wait_for_element,
    robust_click,
    save_data_to_json,
    scroll_to_bottom
)


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class ScraperAgent:

    def __init__(self, config, browser="chrome", headless=True):
        self.config = config
        self.driver_manager = DriverManager(
            browser_name=browser,
            headless=headless
        )
        self.driver = None
        self.scraped_products = []
        self.max_pages = config.get("max_pages", 5)

        logging.info(
            f"Scraper Agent initialized for {config['start_url']}"
        )

    def _get_element_text(
        self, parent_element, selector,
        selector_type=By.CSS_SELECTOR
    ):
        if not selector:
            return None

        try:
            element = parent_element.find_element(
                selector_type, selector
            )
            return element.text.strip()

        except (
            NoSuchElementException,
            StaleElementReferenceException
        ):
            return None

    def _get_element_attribute(
        self, parent_element, selector,
        attribute, selector_type=By.CSS_SELECTOR
    ):
        if not selector:
            return None

        try:
            element = parent_element.find_element(
                selector_type, selector
            )
            value = element.get_attribute(attribute)
            return value.strip() if value else None

        except (
            NoSuchElementException,
            StaleElementReferenceException
        ):
            return None

    def _parse_product_data(self, item_element):
        selectors = self.config["item_data_selectors"]

        name = self._get_element_attribute(
            item_element, selectors.get("name"), "title"
       )

        price = self._get_element_text(
            item_element, selectors.get("price")
        )

        description = self._get_element_text(
            item_element, selectors.get("description")
        )

        url = self._get_element_attribute(
            item_element, selectors.get("url"), "href"
        )

        image_url = self._get_element_attribute(
            item_element, selectors.get("image_url"), "src"
        )

        if name and price:
            return Product(
                name=name,
                price=price,
                description=description,
                url=url,
                image_url=image_url
            )

        return None

    def scrape_page(self):
        logging.info(
            f"Scraping page: {self.driver.current_url}"
        )

        try:
            selector = self.config["item_container_selector"]

            item_elements = self.driver.find_elements(
                By.CSS_SELECTOR, selector
            )

            if not item_elements:
                item_elements = self.driver.find_elements(
                    By.XPATH, selector
                )

            logging.info(
                f"Found {len(item_elements)} potential products."
            )

            for item_element in item_elements:
                product = self._parse_product_data(item_element)

                if product:
                    self.scraped_products.append(
                        product.to_dict()
                    )
                else:
                    logging.warning(
                        "Could not parse product data."
                    )

        except Exception as e:
            logging.error(
                f"Error while scraping page: {e}"
            )

    def run(self):
        self.driver = self.driver_manager.get_driver()

        if not self.driver:
            logging.error(
                "Failed to initialize WebDriver."
            )
            return

        try:
            self.driver.get(self.config["start_url"])
            current_page = 1

            while current_page <= self.max_pages:
                logging.info(
                    f"Processing page {current_page}"
                )

                # Wait for products to appear
                selector = self.config[
                    "item_container_selector"
                ]

                wait_for_element(
                    self.driver,
                    By.CSS_SELECTOR,
                    selector,
                    timeout=10
                )

                self.scrape_page()

                time.sleep(
                    self.config.get(
                        "delay_between_pages", 2
                    )
                )

                # Stop at maximum page limit
                if current_page >= self.max_pages:
                    break

                pagination_selector = self.config[
                    "pagination_selector"
                ]

                if not pagination_selector:
                    logging.info(
                        "No pagination configured."
                    )
                    break

                next_button = wait_for_element(
                    self.driver,
                    By.CSS_SELECTOR,
                    pagination_selector,
                    timeout=5
                )

                selector_type = By.CSS_SELECTOR

                if not next_button:
                    next_button = wait_for_element(
                        self.driver,
                        By.XPATH,
                        pagination_selector,
                        timeout=5
                    )
                    selector_type = By.XPATH

                if not next_button:
                    logging.info(
                        "No more pages found."
                    )
                    break

                if (
                    next_button.is_displayed()
                    and next_button.is_enabled()
                ):
                    previous_url = self.driver.current_url

                    clicked = robust_click(
                        self.driver,
                        selector_type,
                        pagination_selector
                    )

                    if not clicked:
                        logging.warning(
                            "Failed to click next page."
                        )
                        break

                    # Wait until navigation changes the URL
                    from selenium.webdriver.support.ui import WebDriverWait

                    try:
                        WebDriverWait(
                            self.driver, 10
                        ).until(
                            lambda d:
                            d.current_url != previous_url
                        )
                    except TimeoutException:
                        logging.warning(
                            "Page URL did not change."
                        )
                        break

                    current_page += 1

                else:
                    logging.info(
                        "Next page button unavailable."
                    )
                    break

        except Exception as e:
            logging.critical(
                f"Unhandled scraping error: {e}"
            )

        finally:
            self.driver_manager.quit_driver()

            logging.info(
                f"Scraping finished. Total products: "
                f"{len(self.scraped_products)}"
            )

            save_data_to_json(
                self.scraped_products,
                "scraped_products.json"
            )
