import requests
from bs4 import BeautifulSoup
import time

# Retrieve the HTML content of the website
base_url_china = "https://cn.nytimes.com/china/"  # 这里是否需要在往下写一层？
url_pattern_china = r"/(china|policy|china-ec|society|foreign-relations|hk-taiwan)/202[0|1|2|3]\d{4}/\S+/"
base_url_world = "https://cn.nytimes.com/world/"
url_pattern_china = r"/(world|asia-pacific|south-asia|usa|americas|europe|mideast|africa)/202[0|1|2|3]\d{4}/\S+/"

matching_urls_china = []
matching_urls_world = []

req_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/114.0',
}

print("getting links for china...")
for i in range(12):
    page = i + 1
    print("getting page ", page, "...")
    response = requests.get(base_url_china + "/", page, "/")
    html_content = response.text

    # Create a BeautifulSoup object to parse the HTML
    soup = BeautifulSoup(html_content, "html.parser")

    # Define your regular expression pattern to match the URLs
    #url_pattern = r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+/your-pattern-here"
    #上面一行被我注释掉了，因为我不明白ChatGPT写了一个什么玩意儿正则。我重写一行，在下面。
    #这一行正则的目的是，找到纽约时报中文网上，world或者china板块的，2020-2023年的所有文章的链接。
    pattern = re.compile(url_pattern_china)
    for anchor in soup.find_all("a", href=pattern):
        url = anchor.get("href")
        if url in matching_urls_china:
            continue
        matching_urls_china.append(url)

    # sleep for a while
    sleep_duration = random.randint(4, 18)
    time.sleep(sleep_duration)
