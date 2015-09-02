from django.core.management.base import BaseCommand, CommandError
from pull.models import Item, Getter
import time

class Command(BaseCommand):
    help = "Checks for new RSS feed items, gets them and stores them"
    
    
        
    def handle(self, *args, **options):
        #check for new entries every 5 minutes
        #while True:
        result = Getter.pullFeed()
        if result == 0:
            self.stdout.write("No new RSS items")
        elif result == 1:
            self.stdout.write("Pulled 1 item successfully")
        else:
            self.stdout.write("Pulled " + str(result) + " items successfully")
            #time.sleep(30)