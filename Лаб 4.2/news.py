import requests
from bs4 import BeautifulSoup

def get_tass_news(query):
   # Получаем RSS-ленту ТАСС.
  response = requests.get("https://tass.ru/rss/v2.xml")
  soup = BeautifulSoup(response.content, "html.parser")

  # Получаем список новостей из RSS-ленты.
  news_items = soup.find_all("item")

  # Фильтруем новости по запросу.
  filtered_news_items = []
  for news_item in news_items:
    if query in news_item.find("title").text:
      filtered_news_items.append(news_item)

  return filtered_news_items


if __name__ == "__main__":
  # Запрашиваем новости об интересующейся теме.
  news_items = get_tass_news(str(input()))

  # Выводим список новостей.
  for news_item in news_items:
    print(news_item.find("title").text)
