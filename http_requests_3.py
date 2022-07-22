import requests
from datetime import date, timedelta

def main():
    url =  "https://api.stackexchange.com/2.3/questions"
    today = date.today()
    after_tomorrow = today - timedelta(days=2)

    response = requests.get(
        url, 
        params={
            'tagged': 'python',
            'fromdate': after_tomorrow, 
            'todate': today,
            'site': 'stackoverflow'
            }
    )

    for i, item in enumerate(response.json()['items'], 1):
        print(i, item['title'])

if __name__ == '__main__':
    main()