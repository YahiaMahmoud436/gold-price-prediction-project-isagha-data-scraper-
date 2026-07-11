# Gold Price Scraper 🪙

This is a simple Python script that collects daily gold prices from the iSagha website and saves them into a CSV file. 

I built this project to practice web scraping on a real website and to build a continuous dataset that I can use later for data analysis and machine learning projects.

## Features

- Safe from Crashes: The code uses try...except so it won't crash if the internet drops or if the website changes its design.
- Tracks Changes: It automatically catches whether the gold price went up or down, including the percentage.
- No Repeated Headers: It appends new data daily without repeating the column titles in the Excel file.
- Filters Data: It only takes the categories we need (Gold 24K, 22K, 21K, 18K, Gold Pound, and Ounce).
- Clean Data: It removes words like ج.م and $ so the numbers are ready for math and analysis.

## Technologies

- Python
- Requests
- BeautifulSoup4
- CSV & OS modules

## Installation

git clone https://github.com/YahiaMahmoud436/gold-price-prediction-project-isagha-data-scraper-.git

cd gold-price-prediction-project-isagha-data-scraper-

pip install -r requirements.txt

## Usage

To fetch today's prices and add them to your dataset, just run the command: python gold_web_scraping.py

The script will update or create a file named #gold_web_scraping.csv.

## What I plan to do next

Since I am focused on data science and automation, my next steps are:
- Move the data from the CSV file into an SQLite database.
- Create a simple dashboard to visualize price changes over time.
- Clean the historical data using Pandas.
- Train a machine learning model to try and predict future gold prices.

## Automatic Scheduling

This project runs once and exits. If you want to collect data automatically, you can schedule it using:

- Windows Task Scheduler
- Linux/macOS cron
- GitHub Actions
- Any server or cloud platform that supports scheduled jobs

---
Made with by ❤️ Yahia Mahmoud ❤️
