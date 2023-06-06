#主体是GPT写的。这个代码的目的是获取纽约时报中文网上，world或者china板块的，2020-2023年的所有文章body部分的文本。

import requests
from bs4 import BeautifulSoup
import re

# Retrieve the HTML content of the website
url = "https://cn.nytimes.com"  # 这里是否需要在往下写一层？
response = requests.get(url)
html_content = response.text

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html_content, "html.parser")

# Define your regular expression pattern to match the URLs
#url_pattern = r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+/your-pattern-here"
#上面一行被我注释掉了，因为我不明白ChatGPT写了一个什么玩意儿正则。我重写一行，在下面。
#这一行正则的目的是，找到纽约时报中文网上，world或者china板块的，2020-2023年的所有文章的链接。
url_pattern = r"https?://cn.nytimes.com/[world|china]/202[0|1|2|3]\d{4}/\S+/"
pattern = re.compile(url_pattern)

# Extract the URLs that match the pattern
matching_urls = []
for anchor in soup.find_all("a", href=pattern):
    url = anchor.get("href")
    matching_urls.append(url)

# Extract the body text from the pages with matching URLs
for url in matching_urls:
    response = requests.get(url)
    page_content = response.text

    # Create a BeautifulSoup object to parse the page content
    page_soup = BeautifulSoup(page_content, "html.parser")

    # Extract the body text (assuming it is within a specific HTML tag like <body>)
    body_text = page_soup.body.get_text()

    # Print or process the extracted body text as needed
    print(body_text)
