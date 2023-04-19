import csv
from bs4 import BeautifulSoup
import requests

DOWNLOAD_URL = 'https://finance.yahoo.com/trending-tickers'


def download_page(url):
    """
    Reference: https://www.scrapehero.com/scrape-yahoo-finance-stock-market-data/
    """
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-GB,en;q=0.9,en-US;q=0.8,ml;q=0.7",
        "cache-control": "max-age=0",
        "dnt": "1",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "none",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36",
    }
    response = requests.get(url, headers=headers, timeout=30)
    return response.text


# print(download_page(DOWNLOAD_URL))


def parse_html(html):
    """
    Analyze the html page, find the information and return the list of tuples (stock_name, symbol, price, change, change_percent, volume, market_cap)
    """
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup.prettify())
    stock_table = soup.find('tbody')
    stock_list = []
    print(stock_table.prettify())
    for stock_row in stock_table.find_all('tr'):
        symbol = stock_row.find('td', attrs={'aria-label': 'Symbol'})
        symbol_text = symbol.find('a').string
        name = stock_row.find('td', attrs={'aria-label': 'Name'}).string
        print(symbol_text, name)
    return stock_list


parse_html(download_page(DOWNLOAD_URL))


def main():
    """"""


if __name__ == '__main__':
    main()