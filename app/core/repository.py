import unicodedata, requests, json
from datetime import datetime, timedelta

from app.utils.rss import ReadRss
from core.models import News


class Repository:    
    def fetch_cleaned_data(self, url: str) -> None:
        fetched_data = requests.get(url).text[6::]
        cleaned_data = json.loads(fetched_data)

        return cleaned_data
    
    def fetch_last_7_days_trends(self, geo: str):
        data_arr = []

        for i in range(8):
            date = datetime.now() - timedelta(days=i)
            date = date.strftime('%Y%m%d')
            data = self.fetch_cleaned_data(f'https://trends.google.com/trends/api/dailytrends?hl=en&ed={date}&geo={geo}')

            for item in data["default"]["trendingSearchesDays"][0]["trendingSearches"]:
                data_arr.append(item["title"]["query"])
            
        return data_arr

    def fetch_news(self, url: str) -> None:
        data = ReadRss(url)
        return data

    def is_news_created(self, source_url: str) -> bool:
        news = News.objects.filter(source_url=source_url)
        if news:
            return True
        return False
    
    def check_trends(self, description: str, trends_arr: list) -> None:
        for trend in trends_arr:
            trend_name = unicodedata.normalize("NFKD", trend)
            if trend_name.lower() in description.lower():
                return (True, trend_name)
        return (False, None)
        
    def create_bulk_news(
        self,
        data: object,
        trends_arr: list, 
        ) -> None:
        for article in data.articles_dicts:
            is_news_created = self.is_news_created(article['link'])

            if is_news_created is False:
                is_trend, trend_name = self.check_trends(article['description'], trends_arr)
                if is_trend:
                    news = News.objects.create(
                        headline=article['title'],
                        source_url=article['link'],
                        publication_date=article['pub_date'],
                        trend_name=trend_name,
                    )
    
    def get_news(self):
        return News.objects.order_by('-publication_date')

repo = Repository()