import requests

def search_news(query, api_key):
    headers = {"Ocp-Apim-Subscription-Key": api_key}
    url = "https://api.bing.microsoft.com/v7.0/search"
    params = {"q": query, "count": 1,"freshness": "Day"}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    results = response.json().get("webPages", {}).get("value", [])
    return [{"title": r["name"], "url": r["url"], "snippet": r["snippet"]} for r in results]
