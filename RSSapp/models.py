from django.db import models
import datetime

# Create your models here.

class RSS_URLS(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=128, blank=True)

    def get_absolute_url(self):
        return reverse('goal_app:rss_urls')

    def __str__(self):
        return self.title
        # return "<b>" + self.title + "<b>\n" + self.url

class Feed(models.Model):
    url = models.ForeignKey(RSS_URLS, on_delete=models.CASCADE)
    title = models.CharField(max_length=128, blank=True)
    link = models.URLField(blank=True)
    summary = models.CharField(max_length=500, blank=True)
    published = models.DateField(null=True, blank=True)
    updated = models.DateField(null=True, blank=True)
    imported = models.DateField(default=datetime.date.today)

    # def __str__(self):
    #     return self.url
        # return '%s' % (self.url)
