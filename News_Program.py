import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")
def headlines():
    url = "https://newsapi.org/v2/top-headlines"

    categories = [
        "business",
        "entertainment",
        "general",
        "health",
        "science",
        "sports",
        "technology"
    ]

    print("=" * 70)
    print("📰 WELCOME TO THE NEWS HEADLINES APP".center(70))
    print("=" * 70)

    print("\nAvailable Categories:\n")

    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category.title()}")


    # Category Selection


    while True:
        try:
            choice = int(input("\nChoose a category (1-7): "))

            if 1 <= choice <= len(categories):
                selected_category = categories[choice - 1]
                break

            print("Please enter a number between 1 and 7.")

        except ValueError:
            print("Please enter a valid number.")

    print("\nFetching latest news...\n")

    params = {
        "country": "us",
        "category": selected_category,
        "pageSize": 100,
        "apiKey": API_KEY
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()

        if data.get("status") != "ok":
            print("Something went wrong!")
            print(data.get("message"))
            return

        articles = data.get("articles", [])

        if not articles:
            print("No news articles are available for this category.")
            return

        available_articles = len(articles)

        print(f"✅ {available_articles} article(s) available.\n")

        
        # Number of Articles


        while True:
            try:
                number = int(
                    input(
                        f"How many articles would you like to read? (1-{available_articles}): "
                    )
                )

                if 1 <= number <= available_articles:
                    break

                print(f"Please enter a number between 1 and {available_articles}.")

            except ValueError:
                print("Please enter a valid number.")

        print("\n" + "=" * 70)
        print(f"📰 TOP {selected_category.upper()} NEWS".center(70))
        print("=" * 70)

        for count, article in enumerate(articles[:number], start=1):

            print(f"\nArticle {count}")
            print("-" * 70)

            print(f"Title        : {article.get('title', 'Not Available')}\n")
            print(f"Author       : {article.get('author') or 'Not Available'}\n")
            print(f"Source       : {article.get('source', {}).get('name', 'Unknown')}\n")
            print(f"Published At : {article.get('publishedAt', 'Not Available')}\n")
            print(f"Description  : {article.get('description') or 'Not Available'}\n")
            print(f"URL          : {article.get('url', 'Not Available')}\n")

            print("-" * 70)

        print("\nThanks for using the News Headlines App!")

    except requests.exceptions.RequestException as error:
        print("\nUnable to fetch news.")
        print(error)


if __name__ == "__main__":
    headlines()