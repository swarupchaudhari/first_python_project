import requests  # pip install requests

query = input("What type of news are you interested in today? : ")

api = ""

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-02-08&sortBy=publishedAt&apiKey={api}"

print("\nFetching news...\n")

r = requests.get(url)
data = r.json()

articles = data["articles"]

for index, article in enumerate(articles):
    print(index + 1)
    print("Title:", article["title"])
    print("URL:", article["url"])
    print("\n*********************\n")