import csv
import requests
from bs4 import BeautifulSoup

def scrape_jumia_product(product_name, country):
    url = f"https://www.jumia.{country}/catalog/?q={product_name.replace(' ', '+')}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        products = soup.find_all('article', class_='prd _fb col c-prd')

        if not products:
            print("No products found for the specified search criteria.")
            return None

        data = []
        for product in products:
            name = product.find('h3', class_='name').text.strip()
            price = product.find('div', class_='prc').text.strip()

            # Additional details
            rating_count = product.find('div', class_='rev').text.strip().split()[0] if product.find('div', class_='rev') else ""

            data.append([name, price, rating_count])

        return data
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Product Name", "Price", "Rating Count"])
        writer.writerows(data)
    print(f"Data has been saved to {filename}")

if __name__ == "__main__":
    product_name = input("Enter the product name: ")
    country = input("Enter the country code (e.g., ng for Nigeria): ")

    scraped_data = scrape_jumia_product(product_name, country)

    if scraped_data:
        filename = f"{product_name.replace(' ', '_')}_data.csv"
        save_to_csv(scraped_data, filename)
    else:
        print("No data scraped. Exiting !!!")
        
