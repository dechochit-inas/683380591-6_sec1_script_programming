
import os
import logging

from src.config_parser import ConfigParser
from src.scraper_agent import ScraperAgent


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():
    config_path = os.path.join(
        "configs",
        "example_site_config.json"
    )

    try:
        # Step 1: Load configuration
        logging.info("Loading scraper configuration...")

        parser = ConfigParser(config_path)
        config = parser.load_config()

        # Step 2: Initialize Scraper Agent
        logging.info("Initializing Scraper Agent...")

        agent = ScraperAgent(
            config=config,
            browser="chrome",
            headless=False
        )

        # Step 3: Start scraping
        logging.info("Starting web scraping...")
        agent.run()

        logging.info("Web scraping process completed.")

    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
