from core.usecases import CreateTrendingNews
from core.repository import repo

# Usecase 1: Create Trending News
create_trending_news = CreateTrendingNews()
create_trending_news.repo = repo