from bs4 import BeautifulSoup
import requests
  
class ReadRss:
    """
        Read Rss from given source
    """
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.5",
        "Alt-Used": "www.segodnya.ua",
        "Cache-Control" : "max-age=0",
        "Connection": "keep-alive",
        "Cookie": "_ga_WWD3WW3WCP=GS1.1.1649838491.11.0.1649838491.0; _ga=GA1.1.124747383.1649416465; __io_lv=1649579542940; __io=8cb71f4a5.5dee62cc6_1649416466730; __gfp_64b=2qQlkCqCuHOijL2DNzKTp8A7pma1MmVA5QS6Oy4UVML.i7|1649416467; _gid=GA1.2.973461271.1649790206",
        "Host": "www.segodnya.ua",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "TE": "trailers",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0"
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
