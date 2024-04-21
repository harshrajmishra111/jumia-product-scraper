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

python jumia_scraper.py

Notes
Make sure you have a stable internet connection while running the script.
The script may take some time to execute depending on the internet speed and the number of products found.
Ensure that the country code provided is correct to get accurate results.


<img width="781" alt="Screenshot 2024-04-19 at 11 04 38 AM" src="https://github.com/harshrajmishra111/jumia-product-scraper/assets/142572814/050190f5-1057-4395-bc33-b74167de3d38">

<img width="1395" alt="Screenshot 2024-04-19 at 11 08 48 AM" src="https://github.com/harshrajmishra111/jumia-product-scraper/assets/142572814/099837a4-0df3-430d-810b-2999e20c3387"># Jumia-product-scraper


