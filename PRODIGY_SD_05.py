import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the e-commerce website category page
url = "https://www.example.com/category/page"

# Send a request to the website
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the relevant sections containing product information
    products = soup.find_all('div', class_='product')  # Example class name, change based on the site

    product_list = []

    for product in products:
        # Extract product name
        name = product.find('h2', class_='product-title').text.strip()

        # Extract product price
        price = product.find('span', class_='product-price').text.strip()

        # Extract product rating
        rating = product.find('span', class_='product-rating').text.strip()

        # Append the product information to the list
        product_list.append({
            'Name': name,
            'Price': price,
            'Rating': rating
        })

    # Convert the list to a DataFrame
    df = pd.DataFrame(product_list)

    # Save the DataFrame to a CSV file
    df.to_csv('products.csv', index=False)
    print("Data saved to products.csv")
else:
    print(f"Failed to retrieve the web page. Status code: {response.status_code}")