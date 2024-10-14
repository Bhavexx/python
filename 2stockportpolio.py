import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Function to fetch stock data
def fetch_stock_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

# Function to add a stock to the portfolio
def add_stock(portfolio, ticker, quantity):
    # ... implementation

# Function to calculate portfolio returns
def calculate_returns(portfolio):
    # ... implementation

# ... other functions for removing stocks, visualizing data, etc.

# Main loop
while True:
    print("1. Add stock")
    print("2. Remove stock")
    print("3. View portfolio")
    print("4. Calculate returns")
    print("5. Quit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        # ... add stock
    elif choice == 2:
        # ... remove stock
    # ... other choices