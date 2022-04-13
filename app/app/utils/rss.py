from bs4 import BeautifulSoup
import requests
  
class ReadRss:
    """
        Read Rss from given source
    """
    headers = {
        "Cookie": "__cf_bm=9p8aqTL_yLYxRe3E6mvwiAODHkzGpfqWZMV3QIn5nUs-1649841442-0-AfBF6eSjtXLE0gEicq9P47Mg+hW7ayhWo25d5MVvDOnn2TB/kCnBZnS3qRUTIOZA8xxZ2LDCxJjLMJrBHZ4Z6QM=",
        "User-Agent":"PostmanRuntime/7.29.0",
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    }
 
    def __init__(self, rss_url):
        self.url = rss_url
        try:
            self.r = requests.get(rss_url, headers=self.headers)
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
