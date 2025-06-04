import random
from typing import List

import requests
from bs4 import BeautifulSoup

NAVER_NEWS_URL = "https://news.naver.com"


def fetch_article_titles() -> List[str]:
    """Fetch article titles from Naver News front page."""
    response = requests.get(NAVER_NEWS_URL)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    titles = []
    for a in soup.find_all("a"):
        text = a.get_text(strip=True)
        if 5 <= len(text) <= 60:  # heuristic to skip navigation labels
            titles.append(text)
    return titles


def random_title(titles: List[str]) -> str:
    return random.choice(titles)


def main() -> None:
    titles = fetch_article_titles()
    if not titles:
        print("No article titles found.")
        return
    print(random_title(titles))


if __name__ == "__main__":
    main()
