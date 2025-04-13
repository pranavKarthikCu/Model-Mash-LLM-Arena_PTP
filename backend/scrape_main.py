import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def get_all_internal_links(base_url, max_links=100):
    visited = set()
    to_visit = [base_url]
    parsed_base = urlparse(base_url).netloc

    while to_visit and len(visited) < max_links:
        current_url = to_visit.pop(0)
        if current_url in visited:
            continue

        try:
            response = requests.get(current_url, timeout=5)
            if response.status_code != 200:
                continue
            soup = BeautifulSoup(response.text, 'html.parser')
        except Exception as e:
            print(f"Skipping {current_url}: {e}")
            continue

        visited.add(current_url)

        for tag in soup.find_all('a', href=True):
            href = tag['href']
            full_url = urljoin(current_url, href)
            domain = urlparse(full_url).netloc

            if domain == parsed_base and full_url.startswith("http") and "mailto:" not in full_url:
                if full_url not in visited and full_url not in to_visit:
                    to_visit.append(full_url)

        print(f"Crawled: {current_url} ({len(visited)} links)")

    return list(visited)

def scrape_and_save(urls, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    for i, url in enumerate(urls, start=1):
        try:
            response = requests.get(url, timeout=5)
            soup = BeautifulSoup(response.text, 'html.parser')

            for tag in soup(['script', 'style', 'nav', 'footer', 'header']):
                tag.decompose()

            text = soup.get_text(separator='\n', strip=True)
            filename = f"page_{i}.txt"
            path = os.path.join(output_dir, filename)

            with open(path, "w", encoding="utf-8") as f:
                f.write(text)

            print(f"Saved: {filename}")

        except Exception as e:
            print(f"Error scraping {url}: {e}")

def main():
    base_url = "https://uta.edu"
    max_links = 100

    print("Starting crawl...")
    urls = get_all_internal_links(base_url, max_links=max_links)

    print(f"Found {len(urls)} internal links. Now scraping...")
    scrape_and_save(urls, output_dir="data/scraped_pages")

    print("Done!")

if __name__ == "__main__":
    main()
