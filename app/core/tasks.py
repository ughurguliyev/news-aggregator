import random
from django.contrib.auth import get_user_model
from celery import Celery, shared_task
from celery.schedules import crontab
from datetime import date, timedelta 

from core.implemented import create_trending_news

app = Celery()

@app.task 
def create_trending_news_task(url, pn):
    r = create_trending_news.apply.run(
        url=url,
        pn=pn
    )