import requests

def headlines():


    category = input("Enter Category : \n1.)Politics\n2.)Technology\n3.)Sports\n4.)Business\n5.)Health\n6.)Entertainment\n: ").lower()

    url1 = "https://newsapi.org/v2/top-headlines"

    params1 = {"q": category,"apiKey": "1ff8e0e2f54c4ed1b182bc93664aff75"}

    response = requests.get(url=url1, params=params1)

    data = response.json()

    if "articles" not in data:
        print("Error :", data.get("message", "Unable to fetch news."))
        return

    sequence = [2, 3, 4, 7]

    news_count = 1

    for content in range(min(5, len(data["articles"]))):

        print(f"\nNEWS #{news_count}")
        print("-" * 50)

        for index, (key, value) in enumerate(data["articles"][content].items()):

            for j in range(4):

                if index == sequence[j]:

                    if key.lower() == "title":
                        print(f"Title       : {value}\n")

                    elif key.lower() == "description":
                        print(f"Description :\n{value}\n")

                    elif key.lower() == "url":
                        print(f"🔗 URL         :\n{value}\n")

                
                    break

        print("=" * 50)

        news_count += 1

headlines()
