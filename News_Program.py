import requests

def headlines() : 
    url1 = "https://newsapi.org/v2/top-headlines?"

    params1 = {"q": "politics" , "apikey" : "1ff8e0e2f54c4ed1b182bc93664aff75" }

    response = requests.get(url = url1 , params = params1)

    data = response.json()

    sequence = [2,3,4,7] 

    for content in range(len(data["articles"])) : 
        print("="*50)
        for index,(key,value) in enumerate(data["articles"][content].items()) :
            for j in range(4):
                if index == sequence[j]:
                    print(key.title(),":",value)
                    break
        
    
headlines()


 
