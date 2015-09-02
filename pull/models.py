from django.db import models, IntegrityError
from django.core import serializers
import json, feedparser, pytz
from datetime import datetime

UTC = pytz.utc
EDT = pytz.timezone('US/Eastern')
'''
Everything in DB stored as UTC (converted if necessary)
Make comparisons in UTC, show to user in EDT
UTC.localize(datetime) -> compare
EDT.localize(datetime) -> user
'''
# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    description = models.CharField(max_length=65535)
    date = models.DateTimeField("date published")    
    #unique id for feed item
    guid = models.CharField(max_length=63, unique=True, default=0)
    
class Getter(models.Manager):
    #using phys.org news rss feed 
    
    def getFeed(userLastDate):  
        #fields - title, link, description, pubDate
        allItems =  list(Item.objects.order_by("-date"))
        if (len(userLastDate) > 0):
        #user has items
            userDateObject = datetime.strptime(userLastDate, "%a, %d %b %Y %H:%M:%S %Z")
            lastItemDate = None
            try:
                #queryset -> list -> first element.date
                lastItemDate = allItems[0].date
                #lastItemDate = UTC.localize(lastItemDate)
                #.replace(tzinfo=None)
            except:
                lastItemDate = None
                
            if (lastItemDate != None):          
                #already have some items, check how many are actually new, add to DB, send to user
                newestDateTime = allItems[0].date         
                
                #newDateInt = int(newestDateTime.strftime("%Y%m%d%H%M%S"))          
                
                #Find out how many items new for this user
                k = 0
                while ((newestDateTime - userDateObject).total_seconds() > 0):
                    newestDateTime = allItems[k].date
                    k+=1                       
                toReturn = []             
                for i in range(0, k):
                    thisObj = {}                               
                    thisObj["title"] = allItems[i].title
                    thisObj["url"] = allItems[i].url
                    thisObj["description"] = allItems[i].description
                    thisObj["date"] = allItems[i].date.isoformat(" ")             
                    toReturn.append(thisObj)
                    
                return json.dumps(toReturn)        
            else:
                return "-"
        
        else:
            #user has no items
            toReturn = []             
            for i in range(0, len(allItems)):
                thisObj = {}                               
                thisObj["title"] = allItems[i].title
                thisObj["url"] = allItems[i].url
                thisObj["description"] = allItems[i].description
                thisObj["date"] = allItems[i].date.isoformat(" ")             
                toReturn.append(thisObj)
                
            return json.dumps(toReturn)     
        
    def pullFeed():        
        rssFeed = feedparser.parse("http://phys.org/rss-feed/")
        feedList = rssFeed.entries
        
        lastItemDate = None
        try:
            #queryset -> list -> first element.date
            lastItemDate = list(Item.objects.order_by("-date")[:1])[0].date            
        except:
            lastItemDate = None
            
        if lastItemDate == None:
            #no items yet, get full feed, save to DB
            for i in range(0, len(feedList)):            
                dateTime = datetime(*(feedList[i].published_parsed[0:6]))
                dateTime = UTC.localize(dateTime)           
                q = Item(title = feedList[i].title, url = feedList[i].link, description = feedList[i].description, date = dateTime, guid=feedList[i].guid)
               
                try:
                    q.save()
                except IntegrityError:
                    pass
            return len(feedList) 
        else:
            #items exist in DB
            nextItemDate = UTC.localize(datetime(*(feedList[0].published_parsed[0:6])))
            k = 0
            #let's find from which feed item the new (compared to current record) items begin
            while ((nextItemDate - lastItemDate).total_seconds() > 0):                
                nextItemDate = UTC.localize(datetime(*(feedList[k].published_parsed[0:6])))
                k+=1
            for i in range(0, k):
                dateTime = datetime(*(feedList[i].published_parsed[0:6]))
                dateTime = UTC.localize(dateTime)           
                q = Item(title = feedList[i].title, url = feedList[i].link, description = feedList[i].description, date = dateTime, guid=feedList[i].guid)
               
                try:
                    q.save()
                except IntegrityError:
                    pass
            return k
            
    
    pullFeed()
    

