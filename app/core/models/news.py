from django.db import models

from app.utils.base_model import BaseModel


class News(BaseModel):
    """
    News model
    """
    headline = models.CharField(max_length=255, verbose_name='Headline')
    source_url = models.URLField(verbose_name='Source URL', unique=True)
    publication_date = models.CharField(
        max_length=255, 
        verbose_name='Publication date'
    )
    trend_name = models.CharField(
        max_length=255,
        verbose_name='Trend name',
        null=True, blank=True
    )
    
    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"

    def __str__(self):
        return self.headline