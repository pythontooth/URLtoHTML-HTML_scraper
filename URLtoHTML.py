import requests
import os


# Lastest update: 06/05/2024
# Author: @pythontooth
# This project is fully open-source and free to use/modify.


def cls():
    os.system('cls')

def main():
    cls()
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
    v.1.0.0
    """)
    https = "https://"
    http = "http://"

    askUrl = input("URL of the website: ")
    URL = askUrl

    if https or http not in URL:
        URL = https + URL
    
    page = requests.get(URL)
    name = askUrl+'.html'

    with open(name, 'w', encoding='utf-8') as file:  # Dodano encoding='utf-8'
        file.write(page.text)
        print(f"{URL} ||| Source code has been saved to {name}")
        print("IMPORTANT: use the program only for educational purposes.")

main()
while True:
    x = input("Would you like to continue? (y/n): ")
    if x.lower() == "y":
        main()
    else:
        break