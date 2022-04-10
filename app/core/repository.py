import unicodedata
from pytrends.request import TrendReq

from app.utils.rss import ReadRss
from core.models import News


class Repository:
    def fetch_trends(self, pn: str) -> None:
        pytrends = TrendReq(hl='uk-UA', tz=360)
        trends_arr = pytrends.trending_searches(pn=pn).values
        return trends_arr
    
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
            trend_name = unicodedata.normalize("NFKD", trend[0])
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