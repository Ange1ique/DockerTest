import feedparser
import json
import time
import datetime


# get urls from json file
with open("urls.json", "r", encoding="utf-8") as f:
    RSS_URLS = json.load(f)
    f.close()

# get first day of previous month
now = time.localtime()
last = datetime.date(now.tm_year, now.tm_mon, 1) - datetime.timedelta(1)
first = last.replace(day=1)
first = first.timetuple()

# get feed of all urls
posts = []
for url in RSS_URLS:
    posts.extend(feedparser.parse(url).entries)

# get list of titles
titles = []
for post in posts:
    # select posts published or updated since the 1st of previous month
    if first <= post.published_parsed or first <= post.updated_parsed:
        title = post.title
        titles.append(title)

# save titles in json file, named with current date
file_now = str(datetime.date(now.tm_year, now.tm_mon, now.tm_mday)) + ".json"

f = open(file_now, "w", encoding="utf-8")
json = json.dumps(titles, ensure_ascii=False)
f.write(json)
f.close()



# result1 = feed1.entries[0].title
# result1 = feed1.entries[2].summary
# result1 = feed1.entries[0].published

# print(result1)
#
# if 'created' in feed1.entries[0]:
#     result = feed1.entries[0].created
#     print(result)
# else:
#     print("no 'created' in post")

# print(feed1.entries[0])
