from django.db import models
from django_fsm import FSMField, transition
from celery import task
import string


import urllib.request


# Create your models here.

class Url(models.Model):

  class STATE:
    ERROR = '-1'
    NEW = '0'
    DOWNLOADING = '1'
    PROCESSING = '2'
    COMPLETE = '3'


  STATE_CHOICES = (
    (STATE.NEW,'New','Url'),
    (STATE.DOWNLOADING,'Downloading','Url'),
    (STATE.PROCESSING, 'Processing','Url'),
    (STATE.COMPLETE, 'Complete','Url'),
    (STATE.ERROR,'Failed','Url')
  )

  BASE_URL = string.Template("http://en.wikipedia.org/w/index.php?title=Special:Export&pages=$name%0ATalk:$name&offset=1&action=submit")

  title = models.CharField(max_length=100, unique=True)
  state = FSMField(default=STATE.NEW,state_choices=STATE_CHOICES)


  @task()
  @transition(field=state, source=STATE.NEW, target=STATE.DOWNLOADING)
  def download_page_history(self): 
    urllib.request.urlretrieve(self.BASE_URL.substitute(name=self.title), filename=string.Template("/tmp/$name.xml").substitute(name=self.title), data=b'none=none')
    self.save()
      


  
