from django.test import TestCase

from core.implemented import create_trending_news


class TestTrendingNews(TestCase):
    def setUp(self):
        self.created_news = create_trending_news.apply.run(
            url="https://www.segodnya.ua/xml/rss",
            geo="UA"
        )
    
    def test_created_news(self):
        self.assertEqual(self.created_news.is_success, True)