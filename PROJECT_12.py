# project 12 is a news app which fetches news from an API and displays it to the user
# the API used is NewsAPI (https://newsapi.org/)
# the user can enter a topic and the app will fetch news related to that topic

import requests
import warnings
warnings.filterwarnings('ignore', message='Unverified HTTPS request')

your_api_key = "c0170c4db199479bab35539ef03e1d1f"
query = input("Enter the topic you want news about: ")


url= f"https://newsapi.org/v2/everything?q={query}&sortBy=popularity&apiKey={your_api_key}"
print(url)

response = requests.get(url, verify=False, timeout=10)
data=response.json()
articles = data['articles']

for article in articles:
    print(f"Title: {article['title']}")
    print(f"Description: {article['description']}")
    print(f"URL: {article['url']}")
    print("\n")