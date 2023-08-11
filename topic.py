import json
import requests
from bs4 import BeautifulSoup

class Topic:
    
    def getGoogleTrends(self):
        topicIdsListUrl = "https://trends.google.com/trends/api/realtimetrends?hl=tr&tz=-180&cat=all&fi=0&fs=0&geo=TR&ri=300&rs=20&sort=0"
        topicIdsList = requests.get(topicIdsListUrl)
        result = topicIdsList.text.replace(")]}'", "");
        trendingStories = json.loads(result)['storySummaries']['trendingStories']
        post = {
            'entityNames': trendingStories[0]['entityNames'][0]+' '+trendingStories[0]['entityNames'][1],
            'articleTitle': trendingStories[0]['articles'][0]['articleTitle'],
        }
        print(post)
        return post;


        url = "https://trends.google.com/trends/trendingsearches/realtime?geo=TR&hl=tr&category=all"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        trends = []
        items = soup.find_all('div', class_='md-list-block first-realtime-trends-item')  # Bu kısım sayfanın HTML yapısına göre değişiklik gösterebilir.
        
        for item in items:
            title = item.find('div', class_='details-top').text  # Bu kısım sayfanın HTML yapısına göre değişiklik gösterebilir.
            description = item.find('div', class_='details-bottom').text  # Bu kısım sayfanın HTML yapısına göre değişiklik gösterebilir.
            trends.append({
                'title': title,
                'description': description
            })
        
        return trends