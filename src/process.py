import openai


def summarize_text(content: str, api_key: str) -> str:
    """openaiを使ってテキストを要約する"""
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": "Summarize the following article in Japanese."},
            {"role": "assistant", "content": content},
        ],
        max_tokens=150,
    )
    return response.choices[0].message["content"]
