
# My API Data Fetcher CLI (Week 10)

A command-line interface (CLI) application demonstrating basic interaction with Web APIs.
This project uses the `requests` library to fetch and process JSON data from the
[JSONPlaceholder](https://jsonplaceholder.typicode.com/) fake API.

## Features

* **Fetch Single TODO**: Retrieve details of a specific TODO item by its ID.
* **Fetch All Posts**: Get a list of all fake blog posts.
* **Fetch User TODOs**: Retrieve all TODO items associated with a particular user ID.
* **Error Handling**: Includes basic error handling for network issues and API response errors.
* **JSON Processing**: Demonstrates how to parse and extract data from JSON responses.

## Core Concepts Demonstrated

* **APIs (Application Programming Interfaces)**: Understanding how applications communicate.
* **HTTP GET Requests**: Making requests to retrieve data from web servers.
* **`requests` Library**: The standard Python library for making HTTP requests.
* **JSON Data Format**: Parsing and navigating JSON structures.
* **Dependency Management**: Using `pip` and `requirements.txt`.

## How to Run

1. **Clone the repository:**

   ```bash
   git clone [https://github.com/YOUR_USERNAME/my-api-fetcher.git](https://github.com/YOUR_USERNAME/my-api-fetcher.git)
   cd my-api-fetcher
   ```
2. **Install dependencies:**
   This project requires the `requests` library. It's good practice to install it in a virtual environment.

   ```bash
   # Create a virtual environment (optional, but recommended)
   python -m venv venv
   # Activate the virtual environment
   # On Windows: .\venv\Scripts\activate
   # On macOS/Linux: source venv/bin/activate

   # Install dependencies from requirements.txt
   pip install -r requirements.txt
   ```
3. **Run the application:**

   ```bash
   python main.py
   ```

## Project Structure

my-api-fetcher/
├── src/
│ ├── init.py # Makes 'src' a Python package
│ └── api_client.py # Encapsulates API interaction logic
├── main.py # The main entry point of the application
├── .gitignore # Specifies files/folders to ignore in Git
├── README.md # This file!
└── requirements.txt # Lists project dependencies

## Extension Ideas

* **More API Endpoints**: Add functions to `api_client.py` to fetch other resources (e.g., comments, albums, photos) from JSONPlaceholder or other public APIs.
* **Error Logging**: Implement logging to capture API errors more systematically.
* **User Authentication (Advanced)**: Explore APIs that require API keys or tokens for access. (Requires handling headers).
* **Data Filtering/Sorting**: Allow users to specify query parameters (e.g., `?completed=true` for todos).
* **Data Saving**: Save fetched data to a local file (e.g., CSV, JSON).
* **CLI Enhancements**: Use a library like `Typer` or `Click` for more robust CLI arguments.
* **Web Scraping (Next Step)**: If an API isn't available, explore using `BeautifulSoup4` for scraping HTML.

## Contributing

Feel free to fork this repository, add features, or improve existing ones!

## License

This project is open source. (You might add a specific license here later, e.g., MIT)
