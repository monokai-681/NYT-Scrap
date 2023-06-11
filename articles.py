#主体是GPT写的。这个代码的目的是获取纽约时报中文网上，world或者china板块的，2020-2023年的所有文章body部分的文本。

import re
import time
import csv
import random

from cleantext import clean
import requests
from bs4 import BeautifulSoup

visited_urls = []
base_url = "https://cn.nytimes.com/"  # 这里是否需要在往下写一层？

def crawl(links_file):
    csv_reader = csv.reader(links_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        url = row[0]
        if url in visited_urls:
            continue

        response = requests.get(base_url + url + 'dual/')
        visited_urls.append(url)
        print(response.status_code)

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

        with open("corpus.csv", "a") as corpus:
            writer = csv.writer(corpus)
            writer.writerows(rows)
            corpus.close()
            print(len(rows), " rows written")

        sleep_duration = random.randint(0, 3)
        time.sleep(sleep_duration)

print("crawling china links...")
with open('./links_china.csv', 'r') as links_file:
    crawl(links_file)

print("crawling world links...")
with open('./links_world.csv', 'r') as links_file:
    crawl(links_file)

print("all done")
