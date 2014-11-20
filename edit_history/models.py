from django.db import models
from django_fsm import FSMField, transition
from django.db.models.signals import pre_save
from django.dispatch import receiver

from celery import task
import string
import re


import urllib.request
from kombu import Connection,Exchange, Queue, Consumer,eventloop
from kombu.pools import producers




class Url(models.Model):

  class STATE:
    ERROR = '-1'
    NEW = '0'
    DOWNLOADING = '1'
    DOWNLOADED = '2'
    PROCESSING = '3'
    PROCESSED = '4'
    COMPLETED = '5'


  STATE_CHOICES = (
    (STATE.NEW,'New','Url'),
    (STATE.DOWNLOADING,'Downloading','Url'),
    (STATE.DOWNLOADED,'Downloading','Url'),
    (STATE.PROCESSING, 'Processing','Url'),
    (STATE.PROCESSED, 'Processing','Url'),
    (STATE.COMPLETED, 'Complete','Url'),
    (STATE.ERROR,'Failed','Url')
  )

  BASE_URL = string.Template("http://en.wikipedia.org/w/index.php?title=Special:Export&pages=$name%0ATalk:$name&offset=1&action=submit")

  title = models.CharField(max_length=100)
  language = models.CharField(max_length=4, default='en')
  url = models.CharField(max_length=100, unique=True)
  state = FSMField(default=STATE.NEW,state_choices=STATE_CHOICES)

  @receiver(pre_save)
  def generate_title_and_language(sender, instance, *args, **kwargs):
    rgx = re.compile(r"^http:\/\/([a-z][a-z])\.wikipedia\.com\/(.*)$")
    #instance.language, instance.title = rgx.search(instance.url).groups()

  def process(self):
    with Connection() as conn:
        wikipedia_exchange = Exchange('wikipedia', type='direct', durable=False)
        with producers[conn].acquire(block=True) as producer:
            producer.publish(self.title,
                             exchange=wikipedia_exchange,
                             declare=[wikipedia_exchange],
                             routing_key='jobs')

  @transition(field=state, source='*', target=STATE.DOWNLOADING)
  def downloading(self):
    pass

  @transition(field=state, source='*', target=STATE.DOWNLOADED)
  def downloaded(self):
    pass

  @transition(field=state, source='*', target=STATE.PROCESSING)
  def processing(self):
    pass

  @transition(field=state, source='*', target=STATE.PROCESSED)
  def processed(self):
    pass

  @transition(field=state, source='*', target=STATE.COMPLETED)
  def completed(self):
    pass

  @transition(field=state, source='*', target=STATE.COMPLETED)
  def failed(self):
    pass






  
