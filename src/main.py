import logging
import os

from dotenv import load_dotenv

from process import summarize_text
from search import fetch_page_content, search_news
from slack import post_to_slack
from tts import generate_audio

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    load_dotenv(override=True)  # 環境変数を読み込む
    query = "typescript"
    search_results = search_news(query, os.getenv("BING_API_KEY"))

    for result in search_results:
        title = result["title"]
        url = result["url"]
        snippet = result["snippet"]

        page_content = fetch_page_content(result["url"])
        if page_content:
            summary = summarize_text(page_content, os.getenv("OPENAI_API_KEY"))
            news_text = f"{title}\n{summary}"

            # 音声生成
            audio_file = "news.mp3"
            generate_audio(news_text, audio_file)
            # Slackに投稿
            post_to_slack(audio_file, os.getenv("SLACK_BOT_TOKEN"))
        else:
            logger.warning("ページの内容を取得できませんでした。")
