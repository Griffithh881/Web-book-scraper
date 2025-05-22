import requests
from bs4 import BeautifulSoup
import csv
import time

BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"

headers = {
    "User-Agent": "Mozilla/5.0 (compatible; SabaBot/1.0)"
}

def get_books_from_page(page_number):
    url = BASE_URL.format(page_number)
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    books = []

    for book in soup.select(".product_pod"):
        title = book.h3.a["title"]
        price = book.select_one(".price_color").text
        availability = book.select_one(".instock.availability").text.strip()
        books.append({
            "Title": title,
            "Price": price,
            "Availability": availability
        })

    return books

def scrape_all_books():
    all_books = []
    for page in range(1, 6):  # Scrape first 5 pages
        print(f"Scraping page {page}...")
        books = get_books_from_page(page)
        all_books.extend(books)
        time.sleep(1)  # be polite to the server

    return all_books

def save_to_csv(data, filename="books.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["Title", "Price", "Availability"])
        writer.writeheader()
        writer.writerows(data)
    print(f"Saved {len(data)} books to {filename}")

if __name__ == "__main__":
    books = scrape_all_books()
    save_to_csv(books)


