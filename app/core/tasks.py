from celery import Celery

from core.implemented import create_trending_news

app = Celery()

@app.task 
def create_trending_news_task(url, geo):
    r = create_trending_news.apply.run(
        url=url,
        geo=geo
    )