from django.views.generic import ListView

from core.models import News
from core.repository import repo


class HomePageView(ListView):
    template_name = "index.html"
    context_object_name = "all_news"
    
    def get_queryset(self):
        return repo.get_news()