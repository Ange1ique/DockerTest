import json

### list of urls to start with for json file
RSS_URLS = [
    "https://medium.com/feed/topic/artificial-intelligence",
    "https://stackoverflow.com/feeds",
    "https://www.djangoproject.com/rss/weblog/",
    "https://nu.nl/rss",
    "https://medium.com/feed/topic/machine-learning",
    ]
f = open("urls.json","w", encoding="utf-8")
json = json.dumps(RSS_URLS, ensure_ascii=False)
f.write(json)
f.close()
