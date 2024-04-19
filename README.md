# jumia-product-scraper

#Jumia Product Scraper

Overview
This Python script allows you to scrape product data from Jumia, an online marketplace, based on a specified product name and country.

Requirements
Python 3.x
requests library
BeautifulSoup library
Internet connection
Installation
Install Python if you haven't already. You can download it from the official website.
Install the required libraries by running:
Copy code
pip install requests beautifulsoup4
Usage
Run the script jumia_scraper.py.
Enter the product name when prompted.
Enter the country code (e.g., ng for Nigeria) when prompted.
The script will scrape the Jumia website for the specified product in the specified country.
If data is found, it will be saved to a CSV file with the format <product_name>_data.csv.
The CSV file will contain the following columns: "Product Name", "Price", "Rating Count".
Example
Here's an example of how to run the script:

Copy code
python jumia_scraper.py
Notes
Make sure you have a stable internet connection while running the script.
The script may take some time to execute depending on the internet speed and the number of products found.
Ensure that the country code provided is correct to get accurate results.
