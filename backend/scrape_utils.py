# utils.py

import requests
from bs4 import BeautifulSoup
import re
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
            print(f"⚠️ Skipping {current_url}: {e}")
            continue

        visited.add(current_url)

        for tag in soup.find_all('a', href=True):
            href = tag['href']
            full_url = urljoin(current_url, href)
            domain = urlparse(full_url).netloc

            # Internal links only, avoid mailto:, javascript:, etc.
            if domain == parsed_base and full_url.startswith("http") and "mailto:" not in full_url:
                if full_url not in visited and full_url not in to_visit:
                    to_visit.append(full_url)

        print(f"✅ Crawled: {current_url} ({len(visited)} links)")

    return list(visited)

def sanitize_filename(name):
    if not name:
        return None
    name = name.strip().lower()
    name = re.sub(r'[^\w\s-]', '', name)  # Remove special chars
    name = re.sub(r'[\s]+', '_', name)    # Replace spaces with underscores
    return name[:40]  # Limit length for safety
