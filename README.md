# Web-book-scraper
Python script that scraps infromation about books and their prices
# Book Price Scraper

This Python script scrapes book titles, prices, and availability from [books.toscrape.com](http://books.toscrape.com), a website built for practicing web scraping.

## Features
- Scrapes multiple pages
- Gathers title, price, and stock info
- Saves data into a clean CSV file
- Uses `requests`, `BeautifulSoup`, and `csv`

## How to Run
```bash
pip install beautifulsoup4 requests
python main.py

---

### **3. `.gitignore`**
```txt
__pycache__/
*.pyc
books.csv
