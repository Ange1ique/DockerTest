from django.contrib import admin
from .models import RSS_URLS, Feed


# Register your models here.
admin.site.register(RSS_URLS)
admin.site.register(Feed)
