import requests
from assistant.config import NEWS_API_KEY

def get_news():
    url = f"https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={NEWS_API_KEY}"

    response = requests.get(url)
    data = response.json()

    if data["status"] != "ok":
        return ["Sorry, I couldn't fetch the news."]

    headlines = []

    for article in data["articles"][:5]:
        headlines.append(article["title"])

    return headlines

    if __name__ == "__main__":
        print(get_news())