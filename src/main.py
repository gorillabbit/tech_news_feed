from search import search_news
from process import summarize_text
from tts import generate_audio
from slack import post_to_slack
import os
from dotenv import load_dotenv

if __name__ == "__main__":
    # 環境変数の読み込み
    load_dotenv(override=True)  # 環境変数を読み込む

    query = "typescript"
    news_results = search_news(query, os.getenv("BING_API_KEY"))

    for i, news in enumerate(news_results):
        title = news["title"]
        url = news["url"]
        snippet = news["snippet"]

        # 翻訳・要約
        summary = summarize_text(snippet, os.getenv("OPENAI_API_KEY"))
        news_text = f"{title}\n{summary}"

        # 音声生成
        audio_file = f"news_{i+1}.mp3"
        generate_audio(news_text, audio_file)

        # Slackに投稿
        post_to_slack(audio_file, title, f"{summary}\n詳細はこちら: {url}", os.getenv("SLACK_BOT_TOKEN"))
