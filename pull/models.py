from django.db import models, IntegrityError
import feedparser

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    description = models.CharField(max_length=65535)
    date = models.CharField(max_length=255)
    #unique id for feed item
    guid = models.CharField(max_length=63, unique=True, default=0)
    
class Getter(models.Manager):
    #using phys.org news rss feed    
    def getFeed():
        rssFeed = feedparser.parse("http://phys.org/rss-feed/")
        feedList = rssFeed.entries
        #fields - title, link, description, pubDate
        appendStr = ""
        for i in range(0, len(feedList)):
            q = Item(title = feedList[i].title, url = feedList[i].link, description = feedList[i].description, date = feedList[i].published, guid=feedList[i].guid)
            appendStr = appendStr + feedList[i].title + " "
            try:
                q.save()
            except IntegrityError:
                pass
        return appendStr 
        
        #check every 5 minutes
        #threading.Timer(60*5, checkFeed).start()
        
        
    #getFeed()
    

