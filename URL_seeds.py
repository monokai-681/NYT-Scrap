import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Sitemap URL to start the crawl
sitemap_url = "https://cn.nytimes.com/sitemap/"

# Regular expression to match URLs
url_pattern = re.compile(r"https?://cn\.nytimes\.com/(world|china)/2023\d{4}/\S+/")

# Function to discover URLs from a given URL
def discover_urls(url):
    response = requests.get(url)
    discovered_urls = set()

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        links = soup.find_all("a", href=True)

        for link in links:
            href = link["href"]
            absolute_url = urljoin(url, href)
            if url_pattern.match(absolute_url):
                discovered_urls.add(absolute_url)

    return discovered_urls

# Discover section URLs from the sitemap
section_urls = discover_urls(sitemap_url)

# Discover matching URLs from each section URL
all_urls = set()
for section_url in section_urls:
    discovered_urls = discover_urls(section_url)
    all_urls.update(discovered_urls)
    print(f"Processed section: {section_url}")

# Print the total number of discovered URLs
print(f"\nTotal URLs discovered: {len(all_urls)}")