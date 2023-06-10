#主体是GPT写的。这个代码的目的是获取纽约时报中文网上，world或者china板块的，2020-2023年的所有文章body部分的文本。

import requests
from bs4 import BeautifulSoup
import re
import time
import csv
import random
from cleantext import clean




# Extract the URLs that match the pattern
matching_urls = []

print(matching_urls)

visited_urls = []
# Extract the body text from the pages with matching URLs
for url in matching_urls:
    if url in visited_urls:
        continue

    response = requests.get(base_url + url + 'dual/')
    visited_urls.append(url)
    print(url, ": ", response.status_code)
    page_content = response.text

    # Create a BeautifulSoup object to parse the page content
    page_soup = BeautifulSoup(page_content, "html.parser")

    # Extract the text from the div with class "article-paragraph"
    rows = []
    current_row = []
    index = 0

    # Extract the text from the div with class "article-paragraph"
    for div in page_soup.find_all("div", class_="article-paragraph"):
        text = div.get_text()

        if index % 2 == 0:
            # english paragraph
            text = clean(text, lang="en", lower=False, no_line_breaks=True)
            current_row.append(text.strip())
        else:
            text = clean(text, to_ascii=False, lower=False, no_line_breaks=True)
            text = re.sub(',', '，', text)
            current_row.append(text.strip())
            rows.append(current_row)
            current_row = []
        index += 1

    print(url, ": writing csv...")
    with open("corpus.csv", "a") as corpus:
        writer = csv.writer(corpus)
        writer.writerows(rows)
        corpus.close()
        print(url, ": csv written")

    sleep_duration = random.randint(4, 18)
    time.sleep(sleep_duration)

