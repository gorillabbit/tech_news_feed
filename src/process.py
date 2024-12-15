import openai

def summarize_text(content, api_key):
    print("open-ai", api_key)
    openai.api_key = api_key
    print(content)
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": "Summarize the following article in Japanese."},
            {"role": "assistant", "content": content},
        ],
        max_tokens=150
    )
    return response.choices[0].message['content']
