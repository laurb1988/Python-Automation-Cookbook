import feedparser
import datetime
import delorean
import requests
import base64

rss = feedparser.parse('http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml')
#print(rss.channel.updated)
time_limit = delorean.parse(rss.channel.updated) - datetime.timedelta(hours=6)
entries = [entry for entry in rss.entries if delorean.parse(entry.published) > time_limit]
print(len(entries))
print(entries[18]['title'])