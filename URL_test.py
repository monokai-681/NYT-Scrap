import re
from requests_html import HTMLSession

url = "https://cn.nytimes.com/"
regex_pattern = r"https?://cn\.nytimes\.com/(world|china)/2023\d{4}/\S+/"

session = HTMLSession()
response = session.get(url)

if response.status_code == 200:
    response.html.render()
    links = [a["href"] for a in response.html.find("a")]

    matched_links = []
    for link in links:
        if re.match(regex_pattern, link):
            matched_links.append(link)
            print(f"Found URL: {link}")

            if len(matched_links) >= 20:
                break

    if not matched_links:
        print("No URLs matched your regular expression.")
else:
    print(f"Error: Unable to fetch the website (Status Code: {response.status_code}).")