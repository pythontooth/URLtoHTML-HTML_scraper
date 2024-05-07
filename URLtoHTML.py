import requests
import os
from urllib.parse import urlparse
import re
import time
import logging
import random
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from fake_useragent import UserAgent

logging.basicConfig(filename='scraper.log', level=logging.INFO)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def clean_filename(filename):
    # Replace invalid characters with underscores
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

def get_user_agent():
    ua = UserAgent()
    return ua.random

def scrape_page(url):
    try:
        headers = {'User-Agent': get_user_agent()}
        page = requests.get(url, headers=headers, timeout=10)
        page.raise_for_status()  # Raise an error for non-200 status codes
        return page.text
    except requests.RequestException as e:
        logging.error(f"Error occurred while fetching {url}: {e}")
        return None

def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    # Add your parsing logic here
    return soup

def save_html(html_content, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(html_content)
        logging.info(f"HTML source code has been saved to {filename}")
    except IOError as e:
        logging.error(f"Error occurred while writing to file {filename}: {e}")

def main():
    clear_screen()
    print("""
  _   _ _____ __  __ _         ____   ____ ____      _    ____  _____ ____  
 | | | |_   _|  \/  | |       / ___| / ___|  _ \    / \  |  _ \| ____|  _ \ 
 | |_| | | | | |\/| | |       \___ \| |   | |_) |  / _ \ | |_) |  _| | |_) |
 |  _  | | | | |  | | |___     ___) | |___|  _ <  / ___ \|  __/| |___|  _ < 
 |_| |_| |_| |_|  |_|_____|___|____/ \____|_| \_\/_/   \_\_|   |_____|_| \_\
                         |_____|    

    (ONLY FOR EDUCATIONAL PURPOSES)
    |----------|
    Author: @pythontooth
    Latest update: 06/05/2024
    v.1.0.1
    """)

    while True:
        ask_url = input("URL of the website: ").strip()
        if not ask_url.startswith("http://") and not ask_url.startswith("https://"):
            ask_url = "https://" + ask_url
        
        try:
            html_content = scrape_page(ask_url)
            if html_content:
                parsed_url = urlparse(ask_url)
                domain = parsed_url.netloc
                filename = clean_filename(domain) + '.html'
                save_html(html_content, filename)
                soup = parse_html(html_content)
                # Add your parsing and processing logic here
                print("HTML Source code has been saved and parsed.")
        except Exception as e:
            logging.error(f"Error occurred: {e}")

        choice = input("Would you like to continue? (y/n): ").strip().lower()
        clear_screen()
        if choice != "y":
            clear_screen()
            time.sleep(1)
            print("Thanks for using this program :D" + "\n" + "Goodbye!")
            time.sleep(2)
            break

if __name__ == "__main__":
    main()
