import logging

import requests
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


def search_news(query: str, api_key: str) -> list[dict[str, str]]:
    """Bing Search APIを使ってニュースを検索する"""
    headers = {"Ocp-Apim-Subscription-Key": api_key}
    url = "https://api.bing.microsoft.com/v7.0/search"
    params = {"q": query, "count": 5, "freshness": "Day"}
    response = requests.get(url, headers=headers, params=params, timeout=10)
    response.raise_for_status()
    results = response.json().get("webPages", {}).get("value", [])
    return [{"title": r["name"], "url": r["url"], "snippet": r["snippet"]} for r in results]


def fetch_page_content(url: str) -> str:
    """指定されたURLのページ内容を取得する"""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # ページ内のテキストコンテンツを取得 (サイト構造によっては調整が必要)
        content = soup.get_text(separator="\n", strip=True)
        # OpenAI APIのトークン上限を避けるため、最初の3000文字のみ取得
        return content[:3000]
    except requests.RequestException:
        logger.exception("Failed to fetch %s", url)
        return ""
