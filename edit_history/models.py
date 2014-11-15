from django.db import models
from django_fsm import FSMField, transition

# Create your models here.

class Url(models.Model):

  class STATE:
    ERROR = -1
    NEW = 0
    DOWNLOADING = 1
    PROCESSING = 2
    COMPLETE = 3

  STATE_CHOICES = (
    (STATE.NEW,"New","New"),
    (STATE.DOWNLOADING,"Downloading","Downloading"),
    (STATE.PROCESSING, "Processing","Processing"),
    (STATE.COMPLETE, "Complete","Complete"),
    (STATE.ERROR,"Failed","Failed")
  )

  title = models.CharField(max_length=100, unique=True)
  state = FSMField(default=STATE.NEW,state_choices=STATE_CHOICES)

  @transition(field=state, source=STATE.NEW, target=STATE.DOWNLOADING)
  def schedule_download(self):
      """ hta"""

  
