import requests

def main():
    url =  "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"

    response = requests.get(url)

    json_data = response.json()

    max_intelligence = 0
    smartest_hero = ""

    for hero in json_data:
        if hero["name"] == "Hulk":
            if hero["powerstats"]["intelligence"] > max_intelligence:
                max_intelligence = hero["powerstats"]["intelligence"]
                smartest_hero = "Hulk"

        if hero["name"] == "Captain America":
            if hero["powerstats"]["intelligence"] > max_intelligence:
                max_intelligence = hero["powerstats"]["intelligence"]
                smartest_hero = "Captain America"

        if hero["name"] == "Thanos":
            if hero["powerstats"]["intelligence"] > max_intelligence:
                max_intelligence = hero["powerstats"]["intelligence"]
                smartest_hero = "Thanos"                

    print('smartest_hero -', smartest_hero)

if __name__ == '__main__':
    main()