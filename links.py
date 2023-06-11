import requests
from bs4 import BeautifulSoup
import time
import re
import csv
import random

# Retrieve the HTML content of the website
base_url_china = "https://cn.nytimes.com/china/"  # 这里是否需要在往下写一层？
url_pattern_china = r"/(china|policy|china-ec|society|foreign-relations|hk-taiwan)/202[0|1|2|3]\d{4}/\S+/"
base_url_world = "https://cn.nytimes.com/world/"
url_pattern_world = r"/(world|asia-pacific|south-asia|usa|americas|europe|mideast|africa)/202[0|1|2|3]\d{4}/\S+/"

req_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/114.0',
}

print("getting links for china...")
total_china = 0
done_china = False

for i in range(100):
    matching_urls_china = []
    if done_china:
        break
    page = i + 1
    print("getting page ", page, "...")
    response = requests.get(f"{base_url_china}/{page}/")
    html_content = response.text

    # Create a BeautifulSoup object to parse the HTML
    soup = BeautifulSoup(html_content, "html.parser")

    # Define your regular expression pattern to match the URLs
    #url_pattern = r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+/your-pattern-here"
    #上面一行被我注释掉了，因为我不明白ChatGPT写了一个什么玩意儿正则。我重写一行，在下面。
    #这一行正则的目的是，找到纽约时报中文网上，world或者china板块的，2020-2023年的所有文章的链接。
    for anchor in soup.select("h3 > a"):
        url = anchor.get("href")
        if re.fullmatch(url_pattern_china, url) == None:
            continue
        if url in matching_urls_china:
            continue
        matching_urls_china.append([url])
        total_china += 1

    with open("links_china.csv", "a") as links_file:
        writer = csv.writer(links_file)
        writer.writerows(matching_urls_china)
        links_file.close()
        print("wrote", len(matching_urls_china), "to csv")

    if total_china >= 500:
        done_china = True
        break

    # sleep for a while
    sleep_duration = random.randint(0, 2)
    time.sleep(sleep_duration)

print("getting links for world...")
total_world = 0
done_world = False

for i in range(100):
    matching_urls_world = []
    if done_world:
        break
    page = i + 1
    print("getting page ", page, "...")
    response = requests.get(f"{base_url_world}/{page}/")
    html_content = response.text

    # Create a BeautifulSoup object to parse the HTML
    soup = BeautifulSoup(html_content, "html.parser")

    # Define your regular expression pattern to match the URLs
    #url_pattern = r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+/your-pattern-here"
    #上面一行被我注释掉了，因为我不明白ChatGPT写了一个什么玩意儿正则。我重写一行，在下面。
    #这一行正则的目的是，找到纽约时报中文网上，world或者china板块的，2020-2023年的所有文章的链接。
    for anchor in soup.select("h3 > a"):
        url = anchor.get("href")
        if re.fullmatch(url_pattern_world, url) == False:
            continue
        if url in matching_urls_world:
            continue
        matching_urls_world.append([url])
        total_world += 1

    with open("links_world.csv", "a") as links_file:
        writer = csv.writer(links_file)
        writer.writerows(matching_urls_world)
        links_file.close()
        print("wrote", len(matching_urls_world), "to csv")

    if total_world >= 500:
        done_world = True
        break

    # sleep for a while
    sleep_duration = random.randint(0, 2)
    time.sleep(sleep_duration)

