from bs4 import BeautifulSoup
import requests
  
class ReadRss:
    """
        Read Rss from given source
    """
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    }
 
    def __init__(self, rss_url):
        self.url = rss_url
        try:
            self.session = requests.Session()
            self.r = self.session.get(rss_url, headers=self.headers)
            self.status_code = self.r.status_code
        except Exception as e:
            print('Error fetching the URL: ', rss_url)

        self.soup = BeautifulSoup(self.r.text, 'xml')

        self.articles = self.soup.findAll('item')
        self.articles_dicts = [{
            'title': article.title.text, 
            'link': article.link.text,
            'description': article.description.text,
            'content': article.find('content:encoded').text,
            'pub_date': article.pubDate.text}
            for article in self.articles
        ]
        self.descriptions = [d['description'] for d in self.articles_dicts if 'description' in d]
