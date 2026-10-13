# Agentic Web Scraper

## 1. Project Overview

Agentic Web Scraper is a configuration-driven web scraping project developed using Python and Selenium.

The program extracts book information from [Books to Scrape](https://books.toscrape.com/) and saves the collected data in JSON format.

## 2. Features

- Automated browser control using Selenium WebDriver
- Configuration-driven scraping using JSON
- Product data extraction
- Automatic pagination
- Explicit waits and retry mechanisms
- JSON data export
- Modular Python project structure

## 3. Technologies Used

- Python 3
- Selenium
- BeautifulSoup4 (installed dependency)
- WebDriver Manager
- JSON

## 4. Project Structure

```text
agentic-web-scraper/
│
├── configs/
│   └── example_site_config.json
│
├── data/
│   └── scraped_products.json
│
├── docs/
│   └── ETHICS.md
│
├── src/
│   ├── __init__.py
│   ├── config_parser.py
│   ├── data_models.py
│   ├── driver_manager.py
│   ├── scraper_agent.py
│   └── utils.py
│
├── main.py
├── README.md
├── .gitignore
└── venv/
```

## 5. Installation

### Step 1: Create a virtual environment

```bash
python -m venv venv
```

### Step 2: Activate the virtual environment

Windows CMD:

```cmd
venv\Scripts\activate.bat
```

### Step 3: Install dependencies

```bash
pip install selenium beautifulsoup4 webdriver-manager
```

Google Chrome must be installed to run the default configuration.

## 6. Configuration

Edit `configs/example_site_config.json` to configure the scraper.

The configuration includes:

- `start_url`: Starting website URL
- `max_pages`: Maximum number of pages to scrape
- `delay_between_pages`: Delay between pages in seconds
- `item_container_selector`: CSS selector for product containers
- `pagination_selector`: CSS selector for the next-page button
- `item_data_selectors`: Selectors for product attributes

## 7. Running the Program

Run the following command from the project directory:

```bash
python main.py
```

The program will launch Chrome, navigate through the configured pages, extract book information, and save the results.

## 8. Output

The scraped data is saved to:

`data/scraped_products.json`

Each product contains:

- `name`
- `price`
- `description`
- `url`
- `image_url`

## 9. Test Results

The scraper was successfully tested using Books to Scrape.

| Test | Result |
|---|---|
| Pages processed | 3 |
| Products per page | 20 |
| Total products collected | 60 |
| JSON export | Successful |
| Pagination | Successful |
| Full book title extraction | Successful |

## 10. Ethical Considerations

This project is intended for educational purposes. Scraping should respect website policies, avoid excessive requests, and collect only appropriate public information.

See `docs/ETHICS.md` for further details.