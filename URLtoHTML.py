import requests
import os
from urllib.parse import urlparse
import re
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def clean_filename(filename):
    # Replace invalid characters with underscores
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

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
    Lastest update: 06/05/2024
    v.1.0.1
    """)
    
    while True:
        ask_url = input("URL of the website: ").strip()
        if not ask_url.startswith("http://") and not ask_url.startswith("https://"):
            ask_url = "https://" + ask_url
        
        try:
            page = requests.get(ask_url)
            page.raise_for_status()  # Raise an error for non-200 status codes
            parsed_url = urlparse(ask_url)
            domain = parsed_url.netloc
            name = clean_filename(domain) + '.html'
            with open(name, 'w', encoding='utf-8') as file:
                file.write(page.text)
            print(f"HTML Source code has been saved to {name}")
        except requests.RequestException as e:
            print("Error occurred while fetching the page:", e)
        except IOError as e:
            print("Error occurred while writing to file:", e)
        else:
            print("IMPORTANT: use the program only for educational purposes.")
        
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
