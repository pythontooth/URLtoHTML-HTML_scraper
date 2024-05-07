import tkinter as tk
from tkinter import messagebox
import requests
import os
from urllib.parse import urlparse
import re
import logging
from bs4 import BeautifulSoup

logging.basicConfig(filename='scraper.log', level=logging.INFO)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def clean_filename(filename):
    # Replace invalid characters with underscores
    return re.sub(r'[<>:"/\\|?*]', '_', filename)


def scrape_page(url):
    try:
        page = requests.get(url, timeout=10)
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


def scrape_and_save():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a URL.")
        return

    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url

    try:
        html_content = scrape_page(url)
        if html_content:
            parsed_url = urlparse(url)
            domain = parsed_url.netloc
            filename = clean_filename(domain) + '.html'
            save_html(html_content, filename)
            soup = parse_html(html_content)
            # Add your parsing and processing logic here
            messagebox.showinfo("Success", "HTML Source code has been saved and parsed.")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error occurred: {e}")
        messagebox.showerror("Error", f"An error occurred: {e}")


def exit_program():
    root.destroy()


root = tk.Tk()
root.title("URLtoHTML - v1.1.0")

# Set window size and position
window_width = 350
window_height = 100
window_x = (root.winfo_screenwidth() - window_width) // 2
window_y = (root.winfo_screenheight() - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

# Make window non-resizable
root.resizable(False, False)

root.configure(bg="#100c08")

url_label = tk.Label(root, text="Enter URL:", bg="#100c08", fg="white")
url_label.grid(row=0, column=0, padx=(10, 5), pady=5, sticky="e")

url_entry = tk.Entry(root, width=40)
url_entry.grid(row=0, column=1, padx=(0, 10), pady=4)

scrape_button = tk.Button(root, text="Scrape and Save", command=scrape_and_save, bg="#4CAF50", fg="white",
                          relief="flat")
scrape_button.grid(row=1, column=1, pady=8, sticky="e")

author_label = tk.Label(root, text="@pythontooth", bg="#100c08", fg="white")
author_label.grid(row=2, columnspan=2, pady=5)

root.mainloop()
