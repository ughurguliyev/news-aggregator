from django.contrib import admin

from core.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('headline', 'source_url', 'publication_date')
    list_filter = ('publication_date',)
    search_fields = ('headline',)